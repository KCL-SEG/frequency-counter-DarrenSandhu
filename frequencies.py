"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    newlist = []
    for item in items:
        newlist.append(str(item))
    for items in newlist:
        frequencies[items] = frequencies.get(item,0) + 1
    print(frequencies)
