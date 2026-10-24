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
