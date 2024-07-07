#!/usr/bin/python3

def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key not in unlocked:
                unlocked.add(new_key)
                keys.append(new_key)
    return len(unlocked) == n
