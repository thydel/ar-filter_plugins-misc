def choose(l, k):
    return reduce(lambda l, d: l if k not in d else l + [d], l, [])

class FilterModule(object):
    def filters(self):
        return { 'choose': choose }
