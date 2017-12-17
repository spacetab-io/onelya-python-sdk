Onelya Python SDK [![master](https://circleci.com/gh/tmconsulting/onelya-python-sdk/tree/master.svg?style=shield)](https://circleci.com/gh/tmconsulting/onelya-python-sdk/tree/master)
---------------

This SDK is used to connect to the Onelya and use it methods(Railway and Aeroexpress) for a 3-d party API.

* [Installation](#installation)
* [Get started](#get-started)
* [Api Reference](#api-reference)
* [Contact us](#contact-us)
* [License](#license)


### Installation
```
pip3 install onelya_sdk
```

### Get started

To start you will need to have credentials for the Onelya. <br>
Example of api initializing

```python
from onelya_sdk import API

api = API('username', 'password', 'pos')

```

After that, include the wrappers for requests to Railway Reservation

```python
from onelya_sdk.railway import *
```

Now you can use all the methods of the Onelya Railway.

If field type in docs represented as datetime, then you need to pass it as datetime object, **not** str

For example:

E.g [Railway/Search for route pricing](https://test.onelya.ru/ApiDocs/Api?apiId=Railway-V1-Search-RoutePricing):

```python
from datetime import datetime

date = datetime.now()
route_pricing = api.railway_search.route_pricing('2000000', '2078750', date)
```

Now the result will be an instance of RoutePricing

#### Request with wrappers
```python
product_request = ProductRequest('AccidentAndLuggageLossAndDamage')
service_add_upsale_request = ServiceAddUpsaleRequest('Igs', [1389, 1390], product_request)
add_upsale = api.railway_reservation.add_upsale(51978, 52919, service_add_upsale_request)
```

#### Results
All methods, except the `railway_reservation.return_amount`, return instance of class that contains all fields as a class variables and json_data variable with response json

E.g. [References for balances](https://test.onelya.ru/ApiDocs/Api?apiId=Partner-V1-Info-Balances)

```python
api = API(self.username, self.password, self.pos)
balances = api.partner_balances()

balances.account_balances #array of AgentAccount

balances.account_balances[0].current_balance # 1 902 157,38
balances.account_balances[0].account_name # ???? ???? (??????????????)1

balances.account_balances[1].current_balance # 17 991 136,47
balances.account_balances[1].account_name # ?? ???? (????????)2
```
`balances.json_data`
```json
{
  "AccountBalances": [
    {
      "CurrentBalance": "1 902 157,38",
      "AccountName": "???? ???? (??????????????)1"
    },
    {
      "CurrentBalance": "17 991 136,47",
      "AccountName": "?? ???? (????????)2"
    }
  ]
}
```



#### Handling errors

Every method returns an objects with result or raise an error fo OnelyaAPIError

Onelya contains all data about error as in [docs](https://test.onelya.ru/ApiDocs/ErrorCodes)

Additionally returns docs url for method which raised an error

E.g.
```python
blank_as_html = api.railway_search.route_pricing(-1, -1, None)
```
OnelyaAPIError output
```
onelya_railway_sdk.exceptions.OnelyaAPIError: Code: 43
  Message: ???????????? ???????? ?????????(??) 'DepartureDate'
  MessageParams: {'DepartureDate': None}
  Docs: https://test.onelya.ru/ApiDocs/Api?apiId=Railway-V1-Search-RoutePricing

```

### API Reference

To use any of methods, you have to create an instance of Onelya.
Described [here](#get-started)

Currently available methods:

* [Railway](https://test.onelya.ru/ApiDocs/Railway)
* [References](https://test.onelya.ru/ApiDocs/References).

### Contact us.

If you have any issues or questions regarding the API or the SDK it self, you are welcome to create an issue, or
You can write an Email to `artyom.slobodyan@gmail.com` or `roquie0@gmail.com`

### License.

SDK is released under the [MIT License](./LICENSE).
