## Links

* [Slides](https://goo.gl/3zve4E)
* [Links, Infos and Resources](https://goo.gl/SRw1nd) <-- this document has a lot of information and links, be sure to take a look!
* [Workshop Agenda](https://github.com/CityOfZion/python-smart-contract-workshop/blob/master/Workshop-Agenda.md)

If you have any issues or ideas for improvements, please leave your feedback on the [GitHub repository](https://github.com/CityOfZion/python-smart-contract-workshop) and on the [NEO Discord](https://discord.gg/R8v48YA).


## Steps

1. Setup [neo-python](https://github.com/CityOfZion/neo-python) and [neo-privatenet-docker](https://hub.docker.com/r/metachris/neo-privnet-with-gas/)
2. First smart contract using `print`, `Runtime.Log` and `Runtime.Notify`, using neo-python's `build` command with the `test` argument.
3. Basic smart contract using storage.
4. A domain registration smart contract, where users can query, register, transfer and delete domains (important concept: checking of ownership).


## Recommended Setup

Linux or Mac is recommended, and you need Python 3.5 at the moment. If you are using Windows, either setup a VM or use the Linux Subsystem (see also [here](https://docs.google.com/document/d/1hALKjz76U2asbKdrJfUtYF6WN5gKBVSPRGI064UaftI/edit) for more infos).

Clone neo-python and setup everything as described in the README. Then create a symlink of this workshop folder to `neo-python/sc`, which makes it easier to import, build and execute the smart contracts in this workshop.


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
    neo> build sc/2-storage.py test 07 05 True False main
    neo> build sc/3-domain.py test 0710 05 True False query ["test.com"]


## Useful code snippets

* [neo-boa examples](https://github.com/CityOfZion/neo-boa/tree/master/boa/tests/src)
* https://github.com/neonexchange/neo-ico-template
* Storage helper: [nex-ico-template/nex/common/storage.py](https://github.com/neonexchange/neo-ico-template/blob/master/nex/common/storage.py)
* Get info about attached NEO or GAS: [nex-ico-template/nex/common/tx_io.py](https://github.com/neonexchange/neo-ico-template/blob/master/nex/common/txio.py)
* https://github.com/CityOfZion/neo-boa/blob/master/boa/tests/src/OpCallTest.py
* https://github.com/neo-project/neo/wiki/Network-Protocol


#### Timestamps

You can get the last block timestamp from the blockchain with this code.

    def now():
        height = GetHeight()
        current_block = GetHeader(height)
        return current_block.Timestamp

Might not work with neo-boa 0.2.2, downgrade to 0.2.1 (see also https://github.com/CityOfZion/neo-boa/issues/35).


#### Random numbers

See https://medium.com/proof-of-working/coz-first-dapps-competition-dapp-review-3a6b284afaef#414c
