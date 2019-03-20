class OrderedMap(dict):

    # make a new dictionary
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # when it is iterated upon, make sure that that dictionary is in order
    def __iter__(self):
        return iter(sorted(super().__iter__()))


class OrderedSet(set):
    # make a new set
    def __init__(self, lst=[]):
        super().__init__(lst)

    # when iterated, return a sorted set
    def __iter__(self):
        return iter(sorted(super().__iter__()))


class OrderedFrozenSet(frozenset):

    def __init__(self, lst=[]):
        self = frozenset(lst)

    def __iter__(self):
        return iter(sorted(super().__iter__()))
