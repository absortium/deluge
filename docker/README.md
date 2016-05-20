* Docker containers are divided on to types:
    * dev - containers are created for development:
        * work directories are mounted in order to have fast code update.
        * libraries like 'core' and 'ethwallet' are installed in development mode.
    * prod - containers are created for production:
        * work directories are copied from the source directory rather than mounted, like in dev mode.
        * libraries like 'core' and 'ethwallet' are installed in normal mode.
    
* Docker compose files are divided on four types:
    * unit tests:
        * external systems like 'coinbase' and 'ethwallet' are mocked.
        * internal systems like 'router' are mocked.
        * generally, is only required  that 'postgres' service to be up in order to start.
        * celery workers are not working and code is excuting in main process django.
    * integrity tests:
        * external systems like 'coinbase' are mocked.
        * 'ethwallet' service might working in private net or might be mocked (it dependence).
        * 'postgres', 'rabbitmq', 'celery', 'router' services are required to be up in order to start.
        * celery workers are working and celery tasks are executing in another processes.
    * testnet:
        * 'coinbase' working in sandbox environment
        * 'ethwallet' working in testnet, creating non real addresses and transfer non real money.
        * all necessarry containers are up.         
    * realnet:
        * external systems like 'coinbase' are NOT mocked.
        * 'ethwallet' working in the real net, creating real addresses and transfer real money.
        * all necessarry containers are up.

        