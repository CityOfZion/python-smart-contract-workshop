* Present: Overview
    * what are smart contracts, dev restrictions
    * Development tools: neo-boa & neo-python

* Hands-On 1
    * Check that Python 3.5.2 is installed
    * Clone and setup neo-python and neo-boa
    * Pull the privnet Docker image
    * Run Docker privnet and connect neo-python to it
        * use help, open wallet & rebuild

* Present: Smart contract internals 1
    * Supported Python built-ins and functions by neo-boa
        * https://github.com/CityOfZion/neo-boa/blob/master/boa/code/vmtoken.py#L735 // boa.code.builtins
    * Runtime.Log + Notify
        * print —> Neo.Runtime.Log
    * Parameter & return value types: https://github.com/neo-project/docs/blob/master/en-us/sc/tutorial/Parameter.md
    * neo-python `build` command

* Hands-On 2
    * Very simple Print example
    * neo-python build & test process
        * See also: Smart Contract Parameters and Return Values

* Present: Smart contract internals 2
    * Costs for deploying and running smart contracts: http://docs.neo.org/en-us/sc/systemfees.html
    * Storage
        * you can only store a bytearray, int, and strings in storage.
        * if you want to store more complex objects i'd take a look at the serialization example ([[1]](https://github.com/CityOfZion/neo-boa/blob/master/boa/tests/src/SerializationTest.py), [[2]](https://github.com/CityOfZion/neo-boa/blob/master/boa/tests/src/SerializationTest2.py))

* Hands On 3
    * Domain registration system
    * Deploy to privnet, invoke methods

* Present: Smart contract internals 3
    * checkwitness
    * TriggerType.Verification and TriggerType.Application
    * timestamps + random numbers
        * timestamps/block time: boa/src/tests/blockchain // from boa.blockchain.vm.Neo.Header import GetTimestamp
        * random numbers: docs from ambethia on first dapp comp project ([reference](https://medium.com/proof-of-working/coz-first-dapps-competition-dapp-review-3a6b284afaef#414c))
    * how to deal with bytearrays, int and string and so on, and that it really is only bytes

* Hands-On 4
    * NEX ICO template
