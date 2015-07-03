def zipy(l, m):
    return zip(l, m)

class FilterModule(object):
    def filters(self):
        return { 'zip': zipy }
