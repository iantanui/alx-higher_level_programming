#!/usr/bin/python3
class LockedClass:
    try:
        def __init__(self, first_name=""):
            self.first_name = first_name
    except:
        AttributeError("'LockedClass' object has no attribute {}")
