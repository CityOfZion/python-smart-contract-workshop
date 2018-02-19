## Links

* [Slides](https://goo.gl/3zve4E)
* [Links, Infos and Resources](https://goo.gl/SRw1nd) <-- this document has a lot of information and links, be sure to take a look!
* [Workshop Agenda](https://github.com/CityOfZion/python-smart-contract-workshop/blob/master/Workshop-Agenda.md)

If you have any issues or ideas for improvements, please leave your feedback on the [GitHub repository](https://github.com/CityOfZion/python-smart-contract-workshop) and on the [NEO Discord](https://discord.gg/R8v48YA).


## Steps in the workshop

1. Setup [neo-python](https://github.com/CityOfZion/neo-python) and [neo-privatenet-docker](https://hub.docker.com/r/metachris/neo-privnet-with-gas/)
2. First smart contract using `print`, `Runtime.Log` and `Runtime.Notify`: [1-print.py](https://github.com/CityOfZion/python-smart-contract-workshop/blob/master/1-print.py)
   * Learn using neo-python's `build` command with the `test` argument
   * Test differences between Log and Notify
3. Basic smart contract using storage: [2-storage.py](https://github.com/CityOfZion/python-smart-contract-workshop/blob/master/2-storage.py)
   * Storage is one of the key components of most smart contracts
   * Everything is handled as bytes
   * Learn about `debugstorage on/off/reset`
4. A domain registration smart contract: [3-domain.py](https://github.com/CityOfZion/python-smart-contract-workshop/blob/master/3-domain.py)
   * users can query, register, transfer and delete domains
   * important concept: checking of ownership
5. NEX ICO template: https://github.com/neonexchange/neo-ico-template

Note: You probably need to execute `config sc-events on` inside neo-python's `prompt.py` to see any kind of notifications of the examples.

## Recommended Setup

Linux or Mac is recommended, and you need Python 3.5 at the moment. If you are using Windows, either setup a VM or use the Linux Subsystem (see also [here](https://medium.com/@gubanotorious/installing-and-running-neo-python-on-windows-10-284fb518b213) for more infos).

Clone neo-python and setup everything as described in the README. Then create a symlink of this workshop folder to `neo-python/sc`, which makes it easier to import, build and execute the smart contracts in this workshop.

Always work with a private network with this Docker image: https://hub.docker.com/r/metachris/neo-privnet-with-gas/


## Typical method signatures

    # These two are just examples for playing around and experimenting:
    def Main():
    def Main(operation):

    # This is how most real smart contracts look like:
    def Main(operation, args):

See also: [parameter & return value types](https://github.com/neo-project/docs/blob/master/en-us/sc/tutorial/Parameter.md)

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
