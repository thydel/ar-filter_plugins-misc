# useful to access results of register
#
# make a dict of of dict from a result list of dict
#
# - { set_fact: { lst: [ foo, bar ] }}
# - { command: tst "{{ item }}", register: tsts, with_items: lst }
# - { set_fact: { tsts_d: "{{ tsts.results|dictify }}" }
# - { command: cmd, with_items: lst, when: tsts_d[item].rc == 0 }
# 
# tsts.results: [ { item: foo, rc: 0, stdout: OK, ... },      { item: bar, rc: 1, stdout: KO, ... } ]
# tsts_d: { foo:  { item: foo, rc: 0, stdout: OK, ... }, bar: { item: foo, rc: 1, stdout: KO, ... } }
#
# or
#
# make a dict of dict of dict from a result list of dict of dict
#
# find item to use as key in n.item
#
# - { set_fact: { lst: [ { name: foo, attr: some }, { name: bar, attr: other } ] }}
# - { command: tst {{ item.name }} {{ item.attr }}, register: tsts, with_items: lst }
# - { set_fact: { tsts_d: "{{ tsts.results|dictify }}" }
# - { command: cmd, with_items: lst, when: tsts_d[item.name].rc == 0 }
#
# tsts.results: [ { item: { name: foo, attr: some  }, rc: 0, stdout: OK, ... },
#                 { item: { name: bar, attr: other }, rc: 1, stdout: KO, ... } ]
# tsts_d: { foo:  { item: { name: foo, attr: some  }, rc: 0, stdout: OK, ... },
#           bar:  { item: { name: bar, attr: other }, rc: 1, stdout: KO, ... },

def dictify(l, n='name'):
    r = {}
    for i in l:
        if type(i['item']) == type(dict()):
            r[i['item'][n]] = i
        else:
            r[i['item']] = i

    return r

class FilterModule(object):
    def filters(self):
        return { 'dictify': dictify }
