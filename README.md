## Links

* [Slides](https://goo.gl/3zve4E)
* [Links, Infos and Resources](https://goo.gl/SRw1nd)

## Typical method signatures

    def Main():
    def Main(operation):
    def Main(operation, args):

## Often used imports

    from boa.blockchain.vm.Neo.Runtime import Log, Notify
    from boa.blockchain.vm.Neo.Runtime import GetTrigger, CheckWitness

    from boa.blockchain.vm.Neo.TriggerType import Application, Verification
    from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete

    from boa.code.builtins import concat

## Often used `build` commands

    neo> build sc/1-print.py test 07 05 True False main
    neo> build sc/2-domain.py test 0710 05 True False query ["test.com"]
    neo> build sc/3-trigger.py test 0710 05 True False main []


## Useful code snippets

* https://github.com/neonexchange/neo-ico-template
* Storage helper: [nex-ico-template/nex/common/storage.py](https://github.com/neonexchange/neo-ico-template/blob/master/nex/common/storage.py)
* Get info about attached NEO or GAS: [nex-ico-template/nex/common/tx_io.py](https://github.com/neonexchange/neo-ico-template/blob/master/nex/common/txio.py)
* https://github.com/CityOfZion/neo-boa/blob/master/boa/tests/src/OpCallTest.py


#### Timestamps

You can get the last block timestamp from the blockchain with this code.

    def now():
        height = GetHeight()
        current_block = GetHeader(height)
        return current_block.Timestamp

Might not work with neo-boa 0.2.2, downgrade to 0.2.1 (see also https://github.com/CityOfZion/neo-boa/issues/35).


#### Random numbers

See https://medium.com/proof-of-working/coz-first-dapps-competition-dapp-review-3a6b284afaef#414c