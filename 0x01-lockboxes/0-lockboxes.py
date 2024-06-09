#!/usr/bin/python3
"""
Contains a function that checks if all boxes are unlockable
"""


def canUnlockAll(boxes):
    """Function to return true or false if all boxes can
    be unlocked

    Args:
        boxes (box): a list of list to check

    Returns:
        _type_: True if all box can be unlocked or False if not
    """
    # Number of boxes
    n = len(boxes)

    # A set to keep track of which boxes have been opened
    opened_boxes = set()

    # A queue to manage keys we have to use to open other boxes
    keys = [0]

    while keys:
        # Get a key (box number) from the queue
        current_key = keys.pop()

        # If we haven't already opened this box
        if current_key not in opened_boxes:
            # Mark this box as opened
            opened_boxes.add(current_key)

            # Add all the keys from this box to the queue
            for key in boxes[current_key]:
                if key < n and key not in opened_boxes:
                    keys.append(key)

    # If we've opened all the boxes, return True
    return len(opened_boxes) == n
