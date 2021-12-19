"""
An exploration/guide to python's collections module.

"""

import collections
import random


def main():
    # Counter - maintain counts of items in a list/dict
    count = collections.Counter([1, 2, 3, 2, 1, 1, 1, 2, 3, 4, 4, 2, 2, 2])
    count.update({2: 2, 3: 1, 1: 0, 5: 2})
    count.most_common()
    count.subtract({1: 1})
    count.clear()

    # Ordered dict - a dictionary but ordered
    odict = collections.OrderedDict()
    for i in range(5, -1, -1):
        # printing out these values will have keys: 5, 4, 3, 2, 1
        odict.update({i: random.randint(0, 10)})

    # keys: 5, 3, 2, 1, 4
    odict.move_to_end(4)

    odict.clear()

    # Default Dict - a dictionary that is initialized with defaults
    ddict = collections.defaultdict(int)
    ddict[3] += 4                           # 0 to 4
    ddict[3] += 1                           # 4 to 5

    ddict.setdefault(1, 1)

    # ChainMap - A list of dictionaries
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 3, 'd': 4, 'e': 5}
    d3 = {'f': 6, 'g': 7}

    cm = collections.ChainMap(d1, d2, d3)
    # print(cm['a']) print(cm['b']) print(cm['e'])

    cm = cm.new_child({'h': 8, 'i': 9})
    cm.keys(), cm.values(), cm.maps
    cm.update({'b': 5})                     # update first dictionary in chain

    # Named Tuple - lightweight "data class" with named slots
    # Declare type:
    Employee = collections.namedtuple('Employee', ["name", "badge", "title"])

    Employee("Joe Smith", 123, "Engineer")
    empl2 = Employee("Jane Smith", 456, "Manager 2")

    # print(empl2.name)
    # print(empl1.badge)

    empl2._asdict()

    # Deque (double ended queue)
    deq = collections.deque()
    deq.append(0)
    deq.extend([1, 2, 3, 4])
    deq.appendleft(-1)
    deq.extendleft([-2, -3, -4])

    deq.pop()
    deq.popleft()
    deq.rotate(1)
    deq.clear()


class MyDict (collections.UserDict):
    pass


class MyList (collections.UserList):
    pass


class MyString (collections.UserString):
    pass


if __name__ == '__main__':
    main()
