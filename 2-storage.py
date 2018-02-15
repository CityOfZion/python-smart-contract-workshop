"""
This example shows how to write, read and manipulate value in storage.

It is also a good example of using neo-python's `debugstorage`, which
allows you to test `Put` operations with `build .. test` commands.
Debugstorage is enabled by default, you can disable it with
`debugstorage off` and, more importantly, reset it with
`debugstorage reset`.

Test & Build: neo> build sc/2-storage.py test 07 05 True False main
Import:       neo> import contract sc/2-storage.avm 07 05 True False
Invoke:       neo> testinvoke <hash> main
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify
from boa.blockchain.vm.Neo.Storage import Get, Put, Delete, GetContext

def Main():
    context = GetContext()
    Notify(context)

    # This is the storage key
    item_key = 'test-storage-key'

    # Try to get a value for this key from storage
    item_value = Get(context, item_key)
    Notify("Value read from storage:")
    Notify(item_value)

    if len(item_value) == 0:
        print("Storage key not yet set. Setting to 0")
        item_value = 0

    else:
        print("Storage key already set. Incrementing by 1")
        item_value += 1

    # Store the new value
    Put(context, item_key, item_value)
    Notify("New value written into storage:")
    Notify(item_value)

    return item_value
