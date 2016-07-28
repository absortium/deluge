Content
=================

* [Concept](#concept)
* [For programmers](#for-programmers)
   * [parts](#parts)
   * [technologies](#technologies)
   * [interaction](#interaction)
   * [contributing](#contributing)

* [For clients](#for-clients)
    * widget integration
    * widget statistic

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
`Absortium` - is a service which allows to pay for `Ethereum` smart contracts by `BTC`. We are very excited by new technologies, built on blockchain and we believe in the future of it and particulary in `Ethereum` and smart contracts, we want to be part of the future. We love the openness and believe that it is the only way to achieve true security and transparency, so that is why all our sources are publicly available, and you can watch our activity and check all the code we produce.

For programmers
=================
## Parts
* [frontend](https://github.com/absortium/frontend) - UI for creating the ETH/BTC addresses exchange BTC on Eterheum and visa versa.
    * `react`
    * `redux`
    * `webpack`
    * `nodejs`
    * `material-ui`
* [backend](https://github.com/absortium/backend) - backend for creating/canceling/updating/appoving orders.
    * `django`
    * `postgresql`
    * `celery`
    * `rabbitmq`
    * `crossbar.io`
* [ethwallet](https://github.com/absortium/ethwallet) - service which acts as coinbase ETH wallet (no longet needed because coinbase anounce ETH integration)
    * `postgresql`
    * `celery`
    * `rabbitmq`
    * `geth`
* [poloniexbot](https://github.com/absortium/poloniexbot) - service which is retranslate orders from Absortium to Poloniex.
    * `asyncio`
    * `postgresql`
    * `celery`
    * `rabbitmq`

For clients
=================

For users
=================

For investors
=================


Todo
=================
- [x] Create system for exchange `BTC`on `ETH` and visa versa. ([backend](https://github.com/absortium/backend))
- [x] Make integration with [Poloniex](http://poloniex.com) to get liquidity. ([poloniexbot](https://github.com/absortium/poloniexbot))
- [ ] Create widget.
