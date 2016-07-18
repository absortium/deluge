#!/bin/bash

touch .sensitive

echo "export DJANGO_SECRET_KEY='52i_r%4p#xfHj*tzt8g_^(=85as23lK!m$u*t42#2fdawyqzp)'" >> .sensitive
echo "export POSTGRES_PASSWORD='postgres'" >> .sensitive

echo "export DATADOG_API_KEY='db9c2e6759a10091c8c49ab875d420aa'" >> .sensitive

echo "export COINBASE_API_KEY='cZPOTCakDGcqJudY'" >> .sensitive
echo "export COINBASE_API_SECRET='aB8ld1lqbHyww3klJ6VehSVqu2kg5MRa'" >> .sensitive

echo "export ETH_NOTIFICATION_TOKEN='xTcj3y9bZk2423WTZgBZYog7y190PyRT1vT1r2NfJvptRfeu6YAcQPsSKfQKfRQ'" >> .sensitive
echo "export BTC_NOTIFICATION_TOKEN='Vl3ZunmugFVp2323NG70oiRx3UlODLk4UdxN7zqcSGx1dzhzXkHHRp58IXXAdqI'" >> .sensitive

echo "export AUTH0_SECRET_KEY='uxq7IoFhU2cWm0Lq0SXotcOrnuSyN9XDB2PiOpThxjTDPtW3KN-w5h4GMfKprVa5'" >> .sensitive
echo "export AUTH0_API_KEY='JmIrPzSo0nixk13ohk8Bf7C2OZ7Hd1RI'" >> .sensitive

echo "export ETHWALLET_API_KEY='8299831eabc1db2b012j691a8c5c1f1d9c7b8517'" >> .sensitive
echo "export ETHWALLET_API_SECRET='ec7fa071ee9c7fla176093036bc7eae4ef6764f2'" >> .sensitive

echo "export POLONIEX_API_KEY='DWEBL3SB-2I9IL6ZR-A6SW5U2K-7UIVPGHA'" >> .sensitive
echo "export POLONIEX_API_SECRET='8bd68eb9093e74ffb84c88088564b53ada30e5af5efdd385610af588dfb780244406fe90a67e001546071c7f7b315e6520b25e78b8f511b06afd8b25285ec7ab'" >> .sensitive

echo "export ABSORTIUM_API_KEY='8c90b0b7da17f792ac0f8b17b70e1451ca7bd472'" >> .sensetive
echo "export ABSORTIUM_API_SECRET='529cbd8419fa99898da1ca395eb43d1d0ffec28c'" >> .sensetive

cat .sensitive