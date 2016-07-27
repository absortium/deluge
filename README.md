Content
=================

* [Concept](#concept)
* [For programmers](#for-programmers)
   * from which parts application consists?
   * which technologies we use?
   * how they interact?
   * how to contribute?
* [For clients](#for-clients)
    * how to integrate widget on the site?
    * how to get the widget statistics?
* [For users](#for-users)
    * how pay for smart contracts with BTC?
    * how I get money back from smart contract?
    * do you take any fee?

* [For investors](#for-investors)
    * how you will get the money?
    * what volume of smart contracts transactions today?
    * how long the development may take?
    * how many clients already want to integrate this solution?
    * how many users struggles from being not able to pay for smart contract with BTC?
* [Todo](#todo)

Concept
=================
`Absortium` - is a service which allows to pay for `Ethereum` smart contracts by `BTC`, and later with the `USD`, `EUR`, `RUB`. We are very excited by new technologies, built on blockchain and we believe in the future of it and particulary in `Ethereum` and smart contracts, we want to be part of the future and help companies like [Slock.it](https://slock.it/), [Augur](https://www.augur.net/) to achieve their goals. We love the openness and believe that it is the only way to achieve true security and transparency, so that is why all our sources are publicly available, and you can watch our activity and check all the code we produce.

Todo
=================

- [x] Create system for exchange `BTC`on `ETH` and visa versa. ([backend](https://github.com/absortium/backend))
- [x] Make integration with [Poloniex](http://poloniex.com) to get liquidity. ([poloniexbot](https://github.com/absortium/poloniexbot))
- [ ] Create widget for sites like [Augur](https://www.augur.net/) to deposit money on the smart contract with `BTC`.
- [ ] Add exchange `USD` on `ETH` and visa versa.
- [ ] Create solution for `Slock.it` for receiving payments on their smart contract with bank cards.

For programmers
=================

For clients
=================

For users
=================

For investors
=================


from which parts application consists?

## Parts
* [frontend](https://github.com/absortium/frontend)
    * `react`
    * `redux`
    * `webpack`
    * `nodejs`
    * `material-ui`
    * `docker`
* [backend](https://github.com/absortium/backend)
    * `django`
    * `postgresql`
    * `celery`
    * `rabbitmq`
    * `crossbar.io`
    * `docker`
* [ethwallet](https://github.com/absortium/ethwallet)
    * `postgresql`
    * `celery`
    * `rabbitmq`
    * `geth`
    * `docker`
* [poloniexbot](https://github.com/absortium/poloniexbot)
    * `asyncio`
    * `postgresql`
    * `celery`
    * `rabbitmq`
    * `docker`
