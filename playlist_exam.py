```python
# COMP 271 midterm: a singly linked music playlist.
#
# Name:
# Date:

# Complete Song and LinkedPlaylist.
# Add three tests to main.
# Keep PlaylistADT and Node unchanged.
# Add pseudocode comments explaining your approach where required.

from __future__ import annotations

from abc import ABC, abstractmethod


class Song:
    """Represent a song with a title and duration in seconds."""

    def __init__(self, title: str, duration: int) -> None:
        """Validate and store the song's title and duration."""
        # Remove extra whitespace from the title.
        title = title.strip()

        # Reject an empty title or an invalid duration.
        if title == "":
            raise ValueError("Title cannot be empty")
        if type(duration) is not int or duration <= 0:
            raise ValueError("Duration must be a positive integer")

        self.__title = title
        self.__duration = duration

    @property
    def title(self) -> str:
        """Return the song's title."""
        return self.__title

    @property
    def duration(self) -> int:
        """Return the song's duration in seconds."""
        return self.__duration

    def __str__(self) -> str:
        """Return the song's readable description."""
        return f"{self.__title} - {self.__duration} seconds"

      def __eq__(self, other: object) -> bool:
        """Compare the title and duration of two songs."""
        equal = False
        if isinstance(other, Song):
            equal = (
                self.__title == other.__title
                and self.__duration == other.__duration
            )
        return equal


class PlaylistADT(ABC):
    """Declare the operations supported by a playlist (supplied code)."""

    @abstractmethod
    def add(self, song: Song) -> None:
        """Append a song, allowing duplicates."""
        pass

    @abstractmethod
    def contains(self, song: Song) -> bool:
        """Return whether an equal song is present."""
        pass

    @abstractmethod
    def add_unique(self, song: Song) -> bool:
        """Append only if absent; return whether added."""
        pass

    @abstractmethod
    def remove_all(self, song: Song) -> int:
        """Remove every equal song; return the number removed."""
        pass

    @abstractmethod
    def total_duration(self) -> int:
        """Return the total playing time in seconds."""
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of songs."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Return a readable representation in playlist order."""
        pass


class Node:
    """Store one song and a next-node reference (supplied code)."""

    def __init__(self, song: Song, next_node: Node | None = None) -> None:
        """Initialize a node containing a song."""
        self.song = song
        self.next = next_node


class LinkedPlaylist(PlaylistADT):
    """Implement a playlist using a head reference and singly linked nodes."""

    def __init__(self) -> None:
        """Initialize an empty playlist."""
        # Start with no nodes and a size of zero.
        # Do not maintain a tail reference.
        self.__head: Node | None = None
        self.__size = 0

    def add(self, song: Song) -> None:
        """Append a song, allowing duplicates."""
        # Create a node for the new song.
        new_node = Node(song)

        # If the playlist is empty, make the new node the head.
        if self.__head is None:
            self.__head = new_node
        else:
            # Traverse to the last node and attach the new node.
            current = self.__head
            while current.next is not None:
                current = current.next

            current.next = new_node

        self.__size += 1

        def contains(self, song: Song) -> bool:
        """Check whether an equal song exists in the playlist."""
        found = False
        current = self.__head
        while current is not None and not found:
            found = current.song == song
            current = current.next
        return found

        def add_unique(self, song: Song) -> bool:
        """Add a song only when an equal song is absent."""
        added = False
        if not self.contains(song):
            self.add(song)
            added = True
        return added

    def remove_all(self, song: Song) -> int:
        """Remove every equal song in one iterative traversal."""
        # Track the current node, previous node, and removal count.
        current = self.__head
        previous = None
        removed = 0

        while current is not None:
            if current.song == song:
                # Bypass the matching node.
                if previous is None:
                    self.__head = current.next
                else:
                    previous.next = current.next

                # Advance without moving previous, so consecutive
                # matching nodes can also be removed.
                current = current.next
                self.__size -= 1
                removed += 1
            else:
                previous = current
                current = current.next

        return removed

    def __len__(self) -> int:
        """Return the stored size without traversing nodes."""
        return self.__size

        def __str__(self) -> str:
        """Return the songs in order, or an empty-playlist message."""
        result = "(empty playlist)"
        if self.__head is not None:
            descriptions = []
            current = self.__head
            while current is not None:
                descriptions.append(str(current.song))
                current = current.next
            result = "\n".join(descriptions)
        return result

    def total_duration(self) -> int:
        """Return total playing time using the recursive helper."""
        return self.__total_duration_from(self.__head)

        def __total_duration_from(self, node: Node | None) -> int:
        """Recursively sum durations from the given node."""
        duration = 0
        if node is not None:
            duration = (
                node.song.duration
                + self.__total_duration_from(node.next)
            )
        return duration
      
def main() -> None:
    """Run supplied basic tests; add the three required edge-case tests."""
    playlist = LinkedPlaylist()

    print("--- Empty playlist ---")
    print("Length:", len(playlist), "| Expected: 0")
    print("Total duration:", playlist.total_duration(), "| Expected: 0")
    print("Display:", str(playlist), "| Expected: (empty playlist)")
    print(
        "Remove missing song:",
        playlist.remove_all(Song("Missing", 100)),
        "| Expected: 0"
    )

    print("\n--- Song properties and equality ---")
    first = Song("  First Light  ", 180)

    print("Title:", first.title, "| Expected: First Light")
    print("Duration:", first.duration, "| Expected: 180")
    print("Description:", str(first), "| Expected: First Light - 180 seconds")
    print("Equal song:", first == Song("First Light", 180), "| Expected: True")
    print(
        "Different duration:",
        first == Song("First Light", 181),
        "| Expected: False"
    )
    print("Compare with a string:", first == "First Light", "| Expected: False")

    print("\n--- Adding songs ---")
    playlist.add(first)
    playlist.add(Song("Blue Sky", 240))
    playlist.add(Song("First Light", 180))

    print("Length:", len(playlist), "| Expected: 3")
    print("Total duration:", playlist.total_duration(), "| Expected: 600")
    print("Actual playlist:")
    print(playlist)
    print("Expected playlist:")
    print("First Light - 180 seconds")
    print("Blue Sky - 240 seconds")
    print("First Light - 180 seconds")

    print("\n--- Searching and preventing duplicates ---")
    print(
        "Contains First Light:",
        playlist.contains(Song("First Light", 180)),
        "| Expected: True"
    )
    print(
        "Contains Missing:",
        playlist.contains(Song("Missing", 100)),
        "| Expected: False"
    )
    print(
        "Add duplicate Blue Sky:",
        playlist.add_unique(Song("Blue Sky", 240)),
        "| Expected: False"
    )
    print("Length:", len(playlist), "| Expected: 3")

    print("\n--- Removing songs ---")
    print(
        "Remove all First Light songs:",
        playlist.remove_all(Song("First Light", 180)),
        "| Expected: 2"
    )
    print("Display:", str(playlist), "| Expected: Blue Sky - 240 seconds")
    print("Length:", len(playlist), "| Expected: 1")
    print("Total duration:", playlist.total_duration(), "| Expected: 240")
    print(
        "Remove missing song:",
        playlist.remove_all(Song("Missing", 100)),
        "| Expected: 0"
    )
    print("Length:", len(playlist), "| Expected: 1")

    print("\n--- Adding a new unique song ---")
    print(
        "Add Evening:",
        playlist.add_unique(Song("Evening", 120)),
        "| Expected: True"
    )
    print("Length:", len(playlist), "| Expected: 2")
    print("Total duration:", playlist.total_duration(), "| Expected: 360")
    print("Actual playlist:")
    print(playlist)
    print("Expected playlist:")
    print("Blue Sky - 240 seconds")
    print("Evening - 120 seconds")

    print("\n--- Invalid title ---")
    invalid_title_rejected = False
    try:
        Song("   ", 180)
    except ValueError:
        invalid_title_rejected = True

    print("Invalid title rejected:", invalid_title_rejected, "| Expected: True")

    # Test 1: remove consecutive duplicates at the head.
    print("\n--- Test 1: Consecutive duplicates at the head ---")
    duplicate_playlist = LinkedPlaylist()
    duplicate_playlist.add(Song("Echo", 60))
    duplicate_playlist.add(Song("Echo", 60))
    duplicate_playlist.add(Song("Final", 90))

    removed_duplicates = duplicate_playlist.remove_all(Song("Echo", 60))
    print("Removed:", removed_duplicates, "| Expected: 2")
    print("Remaining playlist:")
    print(duplicate_playlist)
    print("Expected: Final - 90 seconds")
    print("Length:", len(duplicate_playlist), "| Expected: 1")

    # Test 2: remove the final remaining song.
    print("\n--- Test 2: Remove the final song ---")
    final_playlist = LinkedPlaylist()
    final_playlist.add(Song("Last Song", 45))

    removed_final = final_playlist.remove_all(Song("Last Song", 45))
    print("Removed:", removed_final, "| Expected: 1")
    print(
        "Display:",
        str(final_playlist),
        "| Expected: (empty playlist)"
    )
    print("Length:", len(final_playlist), "| Expected: 0")
    print("Total duration:", final_playlist.total_duration(), "| Expected: 0")

    # Test 3: verify that duration zero raises ValueError.
    print("\n--- Test 3: Zero duration ---")
    zero_duration_rejected = False
    try:
        Song("Zero", 0)
    except ValueError:
        zero_duration_rejected = True

    print(
        "Zero duration rejected:",
        zero_duration_rejected,
        "| Expected: True"
    )


if __name__ == "__main__":
    main()
```

# Performance analysis:
# Let n be the number of songs in the playlist.
#
# Song.__init__: O(1) time and O(1) auxiliary space.
# Song.__eq__: O(1) time and O(1) auxiliary space.
# LinkedPlaylist.add: O(n) time and O(1) auxiliary space.
# LinkedPlaylist.contains: O(n) time and O(1) auxiliary space.
# LinkedPlaylist.add_unique: O(n) time and O(1) auxiliary space.
# LinkedPlaylist.remove_all: O(n) time and O(1) auxiliary space.
# LinkedPlaylist.__len__: O(1) time and O(1) auxiliary space.
# LinkedPlaylist.__str__: O(n) time and O(n) auxiliary space.
# LinkedPlaylist.total_duration: O(n) time and O(n) call-stack space.
# The recursive helper takes O(n) time and O(n) call-stack space.
