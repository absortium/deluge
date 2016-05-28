* Docker containers are divided on two types:
    * dev - containers are created for development:
        * work directories are mounted in order to have fast code update.
        * libraries 'core' and 'ethwallet' are installed in development mode.
    * prod - containers are created for production:
        * work directories are copied from the source directory rather than mounted, like in dev mode.
        * libraries 'core' and 'ethwallet' are installed in normal mode.
    
* Docker compose files are divided on four types:
    * unit tests:
        * external systems like 'coinbase' and 'ethwallet' are mocked.
        * internal systems like 'router' are mocked.
        * generally, only 'postgres' service  is required to be up in order to start tests.
        * celery workers are not working and code is executing in main process.
    * integration tests:
        * external systems like 'coinbase' are mocked.
        * 'ethwallet' service might working in private net or might be mocked (it dependence).
        * 'postgres', 'rabbitmq', 'celery', 'router' services are required to be up in order to start tests.
        * celery workers are working and celery tasks are executing in another processes.
    * frontend development:
        * external systems like 'coinbase' and 'ethwallet' are mocked.
        * 'postgres', 'rabbitmq', 'celery', 'router' services are required to be up in order to celery task work.
        * celery workers are working and celery tasks are executing like in real system.
        * (NOT EXIST YET) special service 'walletnotifier' is working and emulating money notification from 'coinbase' and 'ethwallet' 
    * testnet:
        * 'coinbase' working in sandbox environment (testnet)
        * 'ethwallet' working in testnet, creating non real addresses and transfer non real money.
        * all necessary containers are up.         
    * realnet:
        * 'coinbase' working in real net.
        * 'ethwallet' working in the real net, creating real addresses and transfer real money.
        * all necessary containers are up.

        