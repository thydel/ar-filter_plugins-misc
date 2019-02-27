def hide(l, k='hide'):
    return reduce(lambda l, d: l if k in d else l + [d], l, [])

class FilterModule(object):
    def filters(self):
        return { 'hide': hide }
