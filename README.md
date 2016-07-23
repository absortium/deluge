### About
`Absortium` - is a service which allows to pay for `Ethereum` smart contracts by `BTC`, and later with the `USD`, `EUR`, `RUB`. We are very excited by new technologies, built on blockchain and we believe in the future of it and particulary in `Ethereum` and smart contracts, we want to be part of the future and help companies like [Slock.it](https://slock.it/), [Augur](https://www.augur.net/) to achieve their goals. We love the openness and believe that it is the only way to go to achieve trully security and transparency, so that is why all our sources are publicly available, and you can watch our activity and check all the code we produce.

### What we want to do?
- [x] Create system for exchange `BTC`on `ETH` and visa versa. ([backend](https://github.com/absortium/backend))
- [x] Make integration with `Poloniex` and `Kraken` for get liquidity. ([poloniexbot](https://github.com/absortium/poloniexbot))
- [ ] Create widget for sites like `Augur` to deposit money on the smart contract with `BTC`.
- [ ] Add exchange `USD` on `ETH` and visa versa.
- [ ] Create solution for `Slock.it` for receiving payments on their smart contract with bank cards.


[Trello](https://trello.com/absortium).

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
    * `django`
    * `postgresql`
    * `celery`
    * `rabbitmq`
    * `docker`
