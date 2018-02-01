"""
Test & Build: neo> build sc/1-print.py test 07 05 True False main
Import:       neo> import contract sc/1-print.avm 07 05 True False
Invoke:       neo> testinvoke <hash> main
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify

def Main():
    print("log via print (1)")
    Log("normal log (2)")
    Notify("notify (3)")

    # Sending multiple arguments as notify payload:
    msg = ["a", 1, 2, b"3"]
    Notify(msg)
