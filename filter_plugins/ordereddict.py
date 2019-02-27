from collections import OrderedDict

def sort_dict_of_dict(d, k, r=False):
    return OrderedDict(sorted(d.items(), key= lambda x: x[1][k], reverse=r))

class FilterModule(object):
    def filters(self):
        return { 'sort_dict_of_dict': sort_dict_of_dict }
