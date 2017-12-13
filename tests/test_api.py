import os
import json
import mock
import unittest
from datetime import datetime
from onelya_railway_sdk.api import API
from onelya_railway_sdk.exceptions import OnelyaAPIError
from onelya_railway_sdk.search import TrainPricing, TrainPriceInfo, Schedule
from onelya_railway_sdk.reservation.requests import (OrderFullCustomerRequest, RailwayReservationRequest,
                                                     RailwayPassengerRequest, ServiceAddUpsaleRequest, ProductRequest)
from onelya_railway_sdk.wrapper.types import (CarType, DocumentType, Sex, CabinGenderKind, AdditionalPlaceRequirements,
                                              CarGrouping, CarStorey, CabinPlaceDemands, ProviderPaymentForm,
                                              PricingTariffType, RailwayPassengerCategory, OperationType)

PDF_PATH = 'tests/data/Order/Reservation/Blank.pdf'
HTML_PATH = 'tests/data/Railway/Reservation/BlankAsHtml.html'


class MockSession(object):
    def __init__(self):
        self.headers = {}
        self.auth = None
        self.mock_json = None

    def post(self, url, data=None, timeout=None):
        self.mock_json = json.loads(open('tests/data/{}.json'.format(url[url.index('.ru/') + len('.ru/'):].
                                                                     replace('/V1', '')), 'r', encoding='utf8').read())
        return self

    def json(self):
        return self.mock_json


class MockFileSession(object):
    def __init__(self):
        self.headers = {}
        self.auth = None
        self.__content = None

    def post(self, url, data=None, timeout=None):
        self.headers['Content-Type'] = 'application/pdf'
        self.__content = open(PDF_PATH, 'rb').read()
        return self

    def json(self):
        raise ValueError

    @property
    def content(self):
        return self.__content


class MockHTMLSession(object):
    def __init__(self):
        self.headers = {}
        self.auth = None
        self.__content = None

    def post(self, url, data=None, timeout=None):
        self.__content = open(HTML_PATH, 'r').read()
        return self

    def json(self):
        raise ValueError

    @property
    def text(self):
        return self.__content


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.datetime = datetime.fromtimestamp(0).replace(hour=3)

        self.username = os.environ.get('USERNAME', None)
        self.password = os.environ.get('PASSWORD', None)
        self.pos = os.environ.get('POS', None)

    @mock.patch('requests.Session', MockSession)
    def test_json_railway_train_pricing(self):
        api = API(self.username, self.password, self.pos)
        train_pricing = api.search.train_pricing('Москва', '2004000', self.datetime, 12, 24, CarGrouping.GROUP)

        input_data = json.loads(open('tests/data/Railway/Search/TrainPricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(train_pricing)

    @mock.patch('requests.Session', MockSession)
    def test_json_railway_car_pricing(self):
        api = API(self.username, self.password, self.pos)
        car_pricing = api.search.car_pricing('2000000', '2004000', self.datetime, '054Ч', None, PricingTariffType.FULL)

        input_data = json.loads(open('tests/data/Railway/Search/CarPricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(car_pricing)

    @mock.patch('requests.Session', MockSession)
    def test_railway_schedule(self):
        api = API(self.username, self.password, self.pos)
        schedule = api.search.schedule('Москва', '2004000', 12, 24)

        input_data = json.loads(open('tests/data/Railway/Search/Schedule.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(schedule)

    @mock.patch('requests.Session', MockSession)
    def test_train_route(self):
        api = API(self.username, self.password, self.pos)
        train_route = api.search.train_route('054', 'Москва', '2004000', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/TrainRoute.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(train_route)

    @mock.patch('requests.Session', MockSession)
    def test_rotes(self):
        api = API(self.username, self.password, self.pos)
        routes = api.search.routes('2000000', '2004000', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/Routes.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(routes)

    @mock.patch('requests.Session', MockSession)
    def test_rote_pricing(self):
        api = API(self.username, self.password, self.pos)
        rote_pricing = api.search.route_pricing('2000000', '2078750', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/RoutePricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(rote_pricing)

    @mock.patch('requests.Session', MockSession)
    def test_search_meal(self):
        api = API(self.username, self.password, self.pos)
        search_meal = api.search.search_meal(CarType.UNKNOWN, 'sample string 1', 'sample string 2',
                                                     'sample string 4', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/SearchMeal.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(search_meal)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_create(self):
        api = API(self.username, self.password, self.pos)

        customers = OrderFullCustomerRequest("4601123450", DocumentType.RUSSIAN_PASSPORT, 'Иван', 'Иванов',
                                             Sex.MALE, 1, 'Иванович', None, 'RU', None, self.datetime)

        passengers = [RailwayPassengerRequest(RailwayPassengerCategory.ADULT, 1, is_invalid=False)]

        reservation_items = RailwayReservationRequest('2006004', '2004001', self.datetime, '054Ч',
                                                      CarType.LUXURY, passengers, 1, '07', 1, 0, CabinGenderKind.NO_VALUE,
                                                      CarStorey.NO_VALUE, (1, 5), None, CabinPlaceDemands.NO_VALUE,
                                                      True, '1Л', AdditionalPlaceRequirements.NO_VALUE, None,
                                                      ProviderPaymentForm.CARD, None, None)

        create = api.reservation.create([customers], [reservation_items], '+79123456789', ['test@test.ru'])

        input_data = json.loads(open('tests/data/Order/Reservation/Create.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(create)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_prolong_reservation(self):
        api = API(self.username, self.password, self.pos)
        prolong_reservation = api.reservation.prolong_reservation(51978, None)

        input_data = json.loads(open('tests/data/Order/Reservation/ProlongReservation.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(prolong_reservation)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_confirm(self):
        api = API(self.username, self.password, self.pos)
        confirm = api.reservation.confirm(51978, provider_payment_form=ProviderPaymentForm.CARD)

        input_data = json.loads(open('tests/data/Order/Reservation/Confirm.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(confirm)

    @mock.patch('requests.Session', MockFileSession)
    def test_reservation_blank(self):
        api = API(self.username, self.password, self.pos)
        blank = api.reservation.blank(1, 2)

        input_data = json.loads(open('tests/data/Order/Reservation/Blank.in.json', 'r', encoding='utf8').read())
        pdf_file = open(PDF_PATH, 'rb').read()

        self.assertEquals(input_data, api.last_request)
        self.assertEquals(blank.content, pdf_file)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_cancel(self):
        api = API(self.username, self.password, self.pos)
        cancel = api.reservation.cancel(51978)

        input_data = json.loads(open('tests/data/Order/Reservation/Cancel.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assertTrue(cancel)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_return_amount(self):
        api = API(self.username, self.password, self.pos)
        return_amount = api.reservation.return_amount('4601123450', 52159, [51948])

        input_data = json.loads(open('tests/data/Order/Reservation/ReturnAmount.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(return_amount)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_auto_return(self):
        api = API(self.username, self.password, self.pos)
        auto_return = api.reservation.auto_return('4601123450', 52157, [51946])

        input_data = json.loads(open('tests/data/Order/Reservation/AutoReturn.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(auto_return)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_add_upsale(self):
        api = API(self.username, self.password, self.pos)
        product_request = ProductRequest('AccidentAndLuggageLossAndDamage')
        service_add_upsale_request = ServiceAddUpsaleRequest('Igs', [1389, 1390], product_request)
        add_upsale = api.reservation.add_upsale(51978, 52919, service_add_upsale_request)

        input_data = json.loads(open('tests/data/Order/Reservation/AddUpsale.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(add_upsale)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_refuse_upsale(self):
        api = API(self.username, self.password, self.pos)
        refuse_upsale = api.reservation.refuse_upsale(1, 2, [1, 2])

        input_data = json.loads(open('tests/data/Order/Reservation/RefuseUpsale.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(refuse_upsale)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_update_blanks(self):
        api = API(self.username, self.password, self.pos)
        update_blanks = api.reservation.update_blanks(52159)

        input_data = json.loads(open('tests/data/Railway/Reservation/UpdateBlanks.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(update_blanks)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_electronic_registration(self):
        api = API(self.username, self.password, self.pos)
        electronic_registration = api.reservation.electronic_registration(52159, True, [51946])

        input_data = json.loads(open('tests/data/Railway/Reservation/ElectronicRegistration.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(electronic_registration)

    @mock.patch('requests.Session', MockSession)
    def test_reservation_meal_option(self):
        api = API(self.username, self.password, self.pos)
        meal_option = api.reservation.meal_option(52159, 'Б', 51946)

        input_data = json.loads(open('tests/data/Railway/Reservation/MealOption.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(meal_option)

    @mock.patch('requests.Session', MockHTMLSession)
    def test_reservation_blank_as_html(self):
        api = API(self.username, self.password, self.pos)
        blank_as_html = api.reservation.blank_as_html(1)

        input_data = json.loads(open('tests/data/Railway/Reservation/BlankAsHtml.in.json', 'r', encoding='utf8').read())
        html_file = open(HTML_PATH, 'r').read()

        self.assertEquals(input_data, api.last_request)
        self.assertEquals(blank_as_html.html, html_file)

    @mock.patch('requests.Session', MockSession)
    def test_order_info(self):
        api = API(self.username, self.password, self.pos)
        order_info = api.info.info(51978)

        input_data = json.loads(open('tests/data/Order/Info/OrderInfo.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(order_info)

    @mock.patch('requests.Session', MockSession)
    def test_order_list(self):
        api = API(self.username, self.password, self.pos)
        order_list = api.info.list(self.datetime, OperationType.PURCHASE)

        input_data = json.loads(open('tests/data/Order/Info/OrderList.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(order_list)

    @mock.patch('requests.Session', MockSession)
    def test_references_transport_nodes(self):
        api = API(self.username, self.password, self.pos)
        transport_nodes = api.references.transport_nodes()

        input_data = json.loads(open('tests/data/Info/References/TransportNodes.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(transport_nodes)

    @mock.patch('requests.Session', MockSession)
    def test_references_cities(self):
        api = API(self.username, self.password, self.pos)
        cities = api.references.cities()

        input_data = json.loads(open('tests/data/Info/References/Cities.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(cities)

    @mock.patch('requests.Session', MockSession)
    def test_references_countries(self):
        api = API(self.username, self.password, self.pos)
        countries = api.references.countries()

        input_data = json.loads(open('tests/data/Info/References/Countries.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(countries)

    @mock.patch('requests.Session', MockSession)
    def test_references_regions(self):
        api = API(self.username, self.password, self.pos)
        regions = api.references.regions()

        input_data = json.loads(open('tests/data/Info/References/Regions.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, api.last_request)
        self.assert_json_with_class(regions)

    @mock.patch('requests.Session', MockSession)
    def test_partner_balances(self):
        api = API(self.username, self.password, self.pos)
        balances = api.balances()

        self.assertEquals({}, api.last_request)
        self.assert_json_with_class(balances)

    def test_empty_message_params(self):
        error_data = {'Code': 1, 'Message': 'Message'}
        self.assertTrue(OnelyaAPIError('Test/Test', error_data, {}).message_params is None)

    def test_empty_json_for_train_pricing(self):
        self.assertTrue(TrainPricing({}).json_data == {})

    def test_empty_json_for_train_price_info(self):
        self.assertTrue(TrainPriceInfo({}).json_data == {})

    def test_empty_json_for_schedule(self):
        self.assertTrue(Schedule({}).json_data == {})

    def assert_json_with_class(self, wrapper):
        for key in wrapper.json_data.keys():
            var = wrapper.__getattribute__(self.get_var_name(key))
            if type(var) not in(bool, int, float, datetime, str, type(None)):
                if type(var) is list:
                    self.check_data_with_list(var, wrapper.json_data[key])
                elif type(var) is dict:
                    self.assertTrue(wrapper.json_data[key] == var)
                else:
                    self.assertTrue(var.json_data == wrapper.json_data[key])
                    self.assert_json_with_class(var)
            else:
                value = self.get_value(var)
                self.assertTrue(wrapper.json_data[key] == value)

    def check_data_with_list(self, wrapper_array, data):
        for var_item, data_item in zip(wrapper_array, data):
            if type(data_item) not in [dict, list]:
                value = self.get_value(data_item)
                self.assertTrue(value == data_item)
            else:
                for key in data_item.keys():
                    var = var_item.__getattribute__(self.get_var_name(key))
                    if type(var) not in (bool, int, float, datetime, str, type(None)):
                        if type(var) is list:
                            self.check_data_with_list(var, data_item[key])
                        elif type(var) is dict:
                            self.assertTrue(data_item[key] == var)
                        else:
                            self.assertTrue(var.json_data == data_item[key])
                            self.assert_json_with_class(var)
                    else:
                        value = self.get_value(var)
                        self.assertTrue(data_item[key] == value)

    @staticmethod
    def get_var_name(json_key):
        var_name = json_key
        var_name = (var_name[0].lower() if var_name[0].isupper() else var_name[0]) + var_name[1:]
        var_name = ''.join([item if not item.isupper() else ('_%s' % item.lower()) for item in var_name])
        return var_name.replace('$', '')

    @staticmethod
    def get_value(var):
        value = var
        if type(value) == datetime:
            value = value.strftime('%Y-%m-%dT%X')
        return value
