#!/usr/bin/python3
import dis
import marshal

if __name__ == "__main__":
    with open('hidden_4.pyc', 'rb') as fd:
        fd.seek(16)
        d = marshal.load(fd)
        names = list(d.co_names)
        names.remove("__init__")
        for name in sorted(names):
            print(name)

#  methods/attributes in marshal object (bytes-like object)

#  || ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
#  '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#  '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code',
#  'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars',
#  'co_kwonlyargcount', 'co_lines', 'co_linetable', 'co_lnotab', 'co_name',
#  'co_names', 'co_nlocals', 'co_posonlyargcount', 'co_stacksize',
#  'co_varnames', 'replace']
