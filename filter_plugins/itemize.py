# make a list of dict from a dict of dict
# remember keys of original dict via added key
# useful to keep generic template when using dict
#
# set_fact: { foo: { ip: 1.2.3.4, port: 1234 } }
# with_items: dict | itemize -> [ { name: foo, ip: 1.2.3.4, port: 1234 }
# with_items: dict | itemize('host') -> [ { host: foo, ip: 1.2.3.4, port: 1234 }
# 
#
# http://www.danielhall.me/category/computing/linux/system-administration/ansible/

def itemize(d, n='name'):
    l = []
    for k in d:
        if d[k] is None:
            d[k] = {}
        d[k][n] = k
        l.append(d[k])

    return l
 
class FilterModule(object):
    def filters(self):
        return { 'itemize': itemize }
