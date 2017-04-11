def flatten(l):
    return [y for x in l for y in x]

class FilterModule(object):
    def filters(self):
        return { 'flatten': flatten }
