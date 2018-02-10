"""
Test & Build: neo> build sc/2-storage.py test 07 05 True False main
Import:       neo> import contract sc/2-storage.avm 07 05 True False
Invoke:       neo> testinvoke <hash> main
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext

def Main():
    context = GetContext()
    Notify(context)

    # Store a value, read it out, and add a number to it:
    item_key = 'hello'
    item_val = 123
    Put(context, item_key, item_val)

    out = Get(context, item_key)
    out = out + 10
    Notify(out)

    return out
