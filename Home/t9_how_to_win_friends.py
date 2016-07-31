"""
Sophia's drones are not soulless and stupid drones; they can make and have friends.
In fact, they already are working for their own social network just for drones!
Sophia has received the data about the connections between drones and she wants to know more about relations between them.

We have an array of straight connections between drones.
Each connection is represented as a string with two names of friends separated by hyphen.
For example: "dr101-mr99" means what the dr101 and mr99 are friends.
You should write a function that allows to determine more complex connection between drones.
You are given two names also. Try to determine if they are related through common bonds by any depth.
For example: if two drones have a common friends or friends who have common friends and so on.

Input: Three arguments:
Information about friends as a tuple of strings; first name as a string; second name as a string.
Output: Are these drones related or not as a boolean.

Example:
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False

How it is used: This concept will help you find not too obvious connections with the building of bond networks.
And how to work social networks.
"""


def check_connection(network, first, second):
    union1 = set()
    union2 = set()
    count = 0
    while count < len(network):
        for connection in network:
            connection = connection.split('-')
            if first in connection:
                union1.update(connection)
            union2.update(union1)
            for node in union2:
                if node in connection:
                    union1.update(connection)
        count += 1
    if second in union1:
        return True
    return False

# Examples:
print(check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3"))
print()
print(check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2"))
print()
print(check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout"))

