
from collections import deque


def time_to_buy(tickets: list[int], k: int) -> int:
    """Return the seconds until person k finishes buying tickets."""
    remaining = list(tickets)
    line = deque()
    for person in range(len(remaining)):
        line.append(person)

    seconds = 0
    while remaining[k] > 0:
        person = line.popleft()
        remaining[person] -= 1
        seconds += 1
        if remaining[person] > 0:
            line.append(person)

    return seconds


if __name__ == "__main__":
    print(time_to_buy([2, 3, 2], 2))
    print(time_to_buy([5, 1, 1, 1], 0))
