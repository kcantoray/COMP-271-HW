from__future__ import annotations

from abc import ABC, abstractmethod


class LookupTableADT(ABC):
    """A collection of entries, each made of a unique key and a value.

    Keys and values are strings. Keys are matched exactly (case matters).
    The table remembers the order in which keys were first added.
    """

    @abstractmethod
    def put(self, key: str, value: str) -> None:
        """Store value under key.

        If key is new, a new entry is added after all existing entries.
        If key is already present, only its value is replaced: the size
        and the position of the key do not change.
        Raise TypeError if key or value is not a string.
        Raise ValueError if key is the empty string.
        A rejected put leaves the table unchanged.
        """

    @abstractmethod
    def get(self, key: str) -> str:
        """Return the value stored under key; raise KeyError if absent."""

    @abstractmethod
    def contains(self, key: str) -> bool:
        """Return True if key is in the table, False otherwise."""

    @abstractmethod
    def remove(self, key: str) -> str:
        """Remove the entry for key and return its value.

        Raise KeyError if the key is absent; the table remains unchanged.
        """

    @abstractmethod
    def size(self) -> int:
      """Return the number of entries in the table."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the table has no entries."""

    @abstractmethod
    def keys(self) -> list[str]:
        """Return a NEW list of the keys, oldest entry first.

        Changing the returned list must not change the table.
        """


class _Entry:
    """One key-value pair stored in an ArrayLookupTable."""

    def __init__(self, key: str, value: str) -> None:
        """Initialize an entry with a key and value."""
        self.key = key
        self.value = value


class ArrayLookupTable(LookupTableADT):
    """A lookup table stored in a Python list of _Entry objects."""

    NOT_FOUND = -1

    def __init__(self) -> None:
        """Initialize an empty lookup table."""
        self.__entries = []

    def __find(self, key: str) -> int:
        """Return the index of key's entry, or NOT_FOUND."""
        found_index = self.NOT_FOUND

        for index in range(len(self.__entries)):
            if self.__entries[index].key == key:
                found_index = index

        return found_index

    def put(self, key: str, value: str) -> None:
        """Add a new entry or replace the value of an existing key."""
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Key and value must be strings.")

        if key == "":
            raise ValueError("Key cannot be empty.")

        found_index = self.__find(key)

        if found_index == self.NOT_FOUND:
            self.__entries.append(_Entry(key, value))
        else:
            self.__entries[found_index].value = value

    def get(self, key: str) -> str:
        """Return the value stored under key; raise KeyError if absent."""
        found_index = self.__find(key)

        if found_index == self.NOT_FOUND:
            raise KeyError(key)

        value = self.__entries[found_index].value
        return value

    def contains(self, key: str) -> bool:
        """Return True if key is in the table, False otherwise."""
        found_index = self.__find(key)
        result = found_index != self.NOT_FOUND

        return result

    def remove(self, key: str) -> str:
        """Remove the entry for key and return its value."""
        found_index = self.__find(key)

        if found_index == self.NOT_FOUND:
            raise KeyError(key)

        value = self.__entries[found_index].value
        del self.__entries[found_index]

        return value

    def size(self) -> int:
        """Return the number of entries in the table."""
        return len(self.__entries)

    def is_empty(self) -> bool:
        """Return True if the table has no entries."""
        result = len(self.__entries) == 0

        return result

    def keys(self) -> list[str]:
        """Return a NEW list of the keys, oldest entry first."""
        key_list = []

        for entry in self.__entries:
            key_list.append(entry.key)

        return key_list




    
        

  
