Docker containers files like `dev.yml` and `prod.yml` determines how your containers should behave, and docker compose
file like `(integration|frontend|testnet...etc).yml` determines how containers are linked with each other.

For example: In `unit` mode all systems are mocked and the only thing that we need it `postgres` and the service itself.

* Docker containers are divided on three types:
    * `dev` - images are created for development:
        * work directories are mounted in order to have fast code update.
        * libraries `core` and `ethwallet` are installed in development mode in order to have fast code update.
    * `prod` - images are created for production:
        * work directories are copied from the source directory rather than mounted.
        * libraries `core` and `ethwallet` are installed not in development mode.
        * installed additionals libraries like `gunicorn` in `backend` service and all unnecessary libraries in `fronted` service are pruned.
    * `base` - images which serve as base for dev and prod.
        
* Docker compose files are divided on four types:
    * `unit`:
        * external systems like `coinbase` and `ethwallet` are mocked.
        * internal systems like `router` are mocked.
        * generally, only `postgres` service  is required to be up in order to start tests.
        * celery workers are not working and code is executing in main process.
    * `integration`:
        * external systems like `coinbase` are mocked.
        * `ethwallet` service might working in private net or might be mocked (it dependence).
        * `postgres`, `rabbitmq`, `celery`, `router` services are required to be up in order to start tests.
        * celery workers are working and celery tasks are executing in another processes.
    * `frontend`:
        * external systems like `coinbase` and `ethwallet` are mocked.
        * `postgres`, `rabbitmq`, `celery`, `router` services are required to be up in order to celery task work.
        * celery workers are working and celery tasks are executing like in real system.
        * (NOT EXIST YET) special service `walletnotifier` is working and emulating money notification from `coinbase` and `ethwallet` 
    * `testnet`:
        * `coinbase` working in sandbox environment (testnet)
        * `ethwallet` working in testnet, creating non real addresses and transfer non real money.
        * all necessary containers are up.         
    * `realnet`:
        * `coinbase` working in real net.
        * `ethwallet` working in the real net, creating real addresses and transfer real money.
        * all necessary containers are up.


In order to to init your mode - compose file, type in shell `dcinit <frontend|unit|integration|testnet|realnet>`, containers type will be detected automatically. Alias `dcinit` is determined in `useful/docker-compose.sh` directory.