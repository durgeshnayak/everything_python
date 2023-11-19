class EnhancedList(list):
    def __setitem__(self, key, value):
        list.__setitem__(self, key, value)

    def append(self, __object):
        list.append(self, __object)

