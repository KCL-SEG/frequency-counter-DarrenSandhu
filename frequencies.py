"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    newlist = []
    for item in items:
        newlist.append(str(item))
    for item in newlist:
        frequencies[item] = frequencies.get(item,0) + 1
    return frequencies
