# make a dict of dict of dict from a result list of dict of dict
# find item to use as key in n.item
# useful to access results of register
#
# - { command: tst "{{ item }}", register: tsts, with_items: lst }
# - { set_facts: { tsts_d: "{{ tsts.results|dictify }}" }
# - { command: cmd, with_items: lst, when: tsts_d[item].rc == 0 }

# 
# results: [ *: *, item: { name: foo, ip: 1.2.3.4 }, ... ]
#       -> { foo: *: *, item: { name: foo, ip: 1.2.3.4 }, ... }

def dictify(l, n='name'):
    r = {}
    for i in l:
        r[i['item'][n]] = i

    return r

class FilterModule(object):
    def filters(self):
        return { 'dictify': dictify }
