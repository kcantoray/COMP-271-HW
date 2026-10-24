from __future__ import annotations

from abc import ABC, abstractmethod


class StackADT(ABC):
    """A last-in, first-out collection of strings."""

    @abstractmethod
    def push(self, item: str) -> None:
        """Add item to the top of the stack."""

    @abstractmethod
    def pop(self) -> str:
        """Remove and return the top item; raise IndexError if empty."""

    @abstractmethod
    def peek(self) -> str:
        """Return the top item without removing it; IndexError if empty."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the stack has no items."""

    @abstractmethod
    def size(self) -> int:
        """Return the number of items in the stack."""


class QueueADT(ABC):
    """A first-in, first-out collection of strings."""

    @abstractmethod
    def enqueue(self, item: str) -> None:
        """Add item to the rear of the queue."""

    @abstractmethod
    def dequeue(self) -> str:
        """Remove and return the front item; raise IndexError if empty."""

    @abstractmethod
    def peek(self) -> str:
        """Return the front item without removing it; IndexError if empty."""

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if the queue has no items."""

    @abstractmethod
    def size(self) -> int:
        """Return the number of items in the queue."""

class FileStack(StackADT):
    """Implement a stack whose only persistent storage is a text file."""

    def __init__(self, path: str) -> None:
        """Create an empty stack file at path."""
        self.__path = path
        with open(self.__path, "w") as file:
            file.write("")

    def push(self, item: str) -> None:
        """Add string to the top of the stack."""
        if not isinstance(item, str):
            raise TypeError("Stack items must be strings")
        if "\n" in item:
            raise ValueError("Stack items cannot contain newlines")
        with open(self.__path, "a") as file:
            file.write(item + "\n")

def pop(self) -> str:
        """Remove and return the top string."""
        with open(self.__path, "r") as file:
            contents = file.read()
        if contents == "":
            raise IndexError("pop from an empty stack")
        end = len(contents) - 1
        start = contents.rfind("\n", 0, end)
        item = contents[start + 1:end]
        contents = contents[:start + 1]
        with open(self.__path, "w") as file:
            file.write(contents)
        return item

def peek(self) -> str:
        """Return the top string without removing it."""
        with open(self.__path, "r") as file:
            contents = file.read()
        if contents == "":
            raise IndexError("peek at an empty stack")
        end = len(contents) - 1
        start = contents.rfind("\n", 0, end)
        item = contents[start + 1:end]
        return item

def is_empty(self) -> bool:
        """Return True when the stack file has no items."""
        empty = self.size() == 0
        return empty

    def size(self) -> int:
        """Count the lines, including lines storing empty strings."""
        with open(self.__path, "r") as file:
            contents = file.read()
        count = contents.count("\n")
        return count

class FileQueue(QueueADT):
    """Implement a queue whose only persistent storage is a text file."""

    def __init__(self, path: str) -> None:
        """Create an empty queue file at path."""
        self.__path = path
        with open(self.__path, "w") as file:
            file.write("")

    def enqueue(self, item: str) -> None:
        """Add a string to the rear of the queue."""
        if not isinstance(item, str):
            raise TypeError("Queue items must be strings")
        if "\n" in item:
            raise ValueError("Queue items cannot contain newlines")
        with open(self.__path, "a") as file:
            file.write(item + "\n")

def dequeue(self) -> str:
        """Remove and return the front string."""
        with open(self.__path, "r") as file:
            contents = file.read()
        if contents == "":
            raise IndexError("dequeue from an empty queue")
        end = contents.find("\n")
        item = contents[:end]
        contents = contents[end + 1:]
        with open(self.__path, "w") as file:
            file.write(contents)
        return item

def peek(self) -> str:
        """Return the front string without removing it."""
        with open(self.__path, "r") as file:
            contents = file.read()
        if contents == "":
            raise IndexError("peek at an empty queue")
        end = contents.find("\n")
        item = contents[:end]
        return item

    def is_empty(self) -> bool:
        """Return True when the queue file has no items."""
        empty = self.size() == 0
        return empty

    def size(self) -> int:
        """Count the lines, including lines storing empty strings."""
        with open(self.__path, "r") as file:
            contents = file.read()
        count = contents.count("\n")
        return count

def main() -> None:
    """Run the required stack and queue scenarios."""
    stack = FileStack("stack.txt")
    for word in ("first", "second", "third"):
        stack.push(word)
    print("Stack size:", stack.size())
    print("Stack peek:", stack.peek())
    print("Stack pop:", stack.pop())
    print("Stack pop:", stack.pop())
    print("Stack size:", stack.size())
    print()

    queue = FileQueue("queue.txt")
    for word in ("first", "second", "third"):
        queue.enqueue(word)
    print("Queue size:", queue.size())
    print("Queue peek:", queue.peek())
    print("Queue dequeue:", queue.dequeue())
    print("Queue dequeue:", queue.dequeue())
    print("Queue size:", queue.size())
    print()

try:
        FileStack("empty_stack.txt").pop()
        print("ERROR: pop from an empty stack was accepted")
    except IndexError as error:
        print("Empty pop rejected:", error)

    try:
        FileQueue("empty_queue.txt").dequeue()
        print("ERROR: dequeue from an empty queue was accepted")
    except IndexError as error:
        print("Empty dequeue rejected:", error)

    try:
        FileStack("peek_stack.txt").peek()
        print("ERROR: peek at an empty stack was accepted")
    except IndexError as error:
        print("Empty stack peek rejected:", error)

    try:
        FileQueue("peek_queue.txt").peek()
        print("ERROR: peek at an empty queue was accepted")
    except IndexError as error:
        print("Empty queue peek rejected:", error)

    try:
        FileStack("newline_stack.txt").push("two\nlines")
        print("ERROR: newline in stack item was accepted")
    except ValueError as error:
        print("Newline push rejected:", error)

    try:
        FileQueue("type_queue.txt").enqueue(42)
        print("ERROR: non-string queue item was accepted")
    except TypeError as error:
        print("Non-string enqueue rejected:", error)

    try:
        StackADT()
        print("ERROR: abstract StackADT was instantiated")
