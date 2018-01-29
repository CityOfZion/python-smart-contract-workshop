"""
Example which allows calls from the owner, or from users if at least 1 GAS is attached

Verification only happens on the blockchain with deployed contracts.
The `build` command only does the Appication portion.

neo> build sc/3-trigger.py test 0710 05 True False main []
neo> import contract sc/3-trigger.avm 0710 05 True False
neo> testinvoke e2f8eabbb31323569e5071e9fc88f4eeaddb8aa4 main []
"""
from boa.blockchain.vm.Neo.Runtime import Log, Notify
from boa.blockchain.vm.Neo.Runtime import GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from utils.txio import get_asset_attachments

OWNER = b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'


def Main(operation, args):
    trigger = GetTrigger()

    if trigger == Verification:
        print("doing verification!")
        Notify("doing verification notify!")

        # is_owner = CheckWitness(OWNER)
        # if is_owner:
        #     return True

        # Check that at least 1 GAS is attached
        attachment = get_asset_attachments()
        if attachment.gas_attached >= 1:
            return True
        return False

    elif trigger == Application:
        print("doing application!")

    return 1
