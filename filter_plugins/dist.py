def dist(l, o):
    r = []
    for i in l:
        r.append([o, i])

    return r

class FilterModule(object):
    def filters(self):
        return { 'dist': dist }
