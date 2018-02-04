"""
Example which allows calls from the owner, or from users if at
least 1 GAS is attached. THIS IS WORK IN PROGRESS AND NOT WORKING.

The Verification trigger is basically only called when using the
mintToken method in neo-python, so the only really good example
is a NEP-5 ICO smart contract such as the NEX template.

To do an invoke with verification and token, first you'll have
to import the token to the wallet and then use `tkn_mint`:

    import token {contract_hash}
    wallet tkn_mint {token_symbol} {ADDR} --attach-neo=X

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
