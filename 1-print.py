"""
neo> build sc/1-print.py test 07 05 True False main
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify

def Main():
    print("log via print 1")  # using pythonic print(), this is tranlated to Neo.Runtime.Log
    Log("log real 2")
    Notify("notify2", 2)
