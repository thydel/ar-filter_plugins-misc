# make a list of dict suitable for with_subelements
#
# set_facts: { ugroups: { admins: [ joe, bill ], devs: [ sam, phil, ted ] } }
#
# ugroups | subelementize("group", "user") ->
# [ { group: admins, users: [ joe, bill ] }, { group: devs, users: [ sam, phil, ted ] } ]

def subelementize_(d, nk, nv):
    l = []
    for k in d:
        t = {}
        t[nk] = k
        t[nv] = d[k]
        l.append(t)

    return l
 
def subelementize(d, nk, nv):
    l = []
    for k, v in d.iteritems():
        l.append({nk: k, nv: v})

    return l
 
class FilterModule(object):
    def filters(self):
        return { 'subelementize': subelementize }
