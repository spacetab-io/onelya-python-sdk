import json
import os
import unittest
from datetime import datetime

import mock

from onelya_sdk.api import API
from onelya_sdk.exceptions import OnelyaAPIError
from onelya_sdk.railway import (OrderFullCustomerRequest, RailwayReservationRequest,
                                RailwayPassengerRequest, ServiceAddUpsaleRequest, ProductRequest)
from onelya_sdk.aeroexpress import (AeroexpressReservationRequest)
from onelya_sdk.wrapper.types import (CarType, DocumentType, Sex, CabinGenderKind, AdditionalPlaceRequirements,
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


class MockAeroexpressSession(object):
    def __init__(self):
        self.headers = {}
        self.auth = None
        self.mock_json = None

    def post(self, url, data=None, timeout=None):
        self.mock_json = json.loads(open('tests/data/Aeroexpress/{}.json'.format(url[url.index('.ru/') + len('.ru/'):].
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

        self.railway_api = self.railway_api()
        self.aeroexpress_api = self.aeroexpress_api()

    @mock.patch('requests.Session', MockSession)
    def railway_api(self):
        return API(self.username, self.password, self.pos)

    @mock.patch('requests.Session', MockAeroexpressSession)
    def aeroexpress_api(self):
        return API(self.username, self.password, self.pos)

    def test_json_railway_train_pricing(self):
        train_pricing = self.railway_api.railway_search.train_pricing('Москва', '2004000', self.datetime, 12, 24, CarGrouping.GROUP)

        input_data = json.loads(open('tests/data/Railway/Search/TrainPricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(train_pricing)

    def test_json_railway_car_pricing(self):
        car_pricing = self.railway_api.railway_search.car_pricing('2000000', '2004000', self.datetime, '054Ч', None, PricingTariffType.FULL)

        input_data = json.loads(open('tests/data/Railway/Search/CarPricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(car_pricing)

    def test_railway_schedule(self):
        schedule = self.railway_api.railway_search.schedule('Москва', '2004000', 12, 24)

        input_data = json.loads(open('tests/data/Railway/Search/Schedule.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(schedule)

    def test_train_route(self):
        train_route = self.railway_api.railway_search.train_route('054', 'Москва', '2004000', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/TrainRoute.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(train_route)

    def test_routes(self):
        routes = self.railway_api.railway_search.routes('2000000', '2004000', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/Routes.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(routes)

    def test_route_pricing(self):
        route_pricing = self.railway_api.railway_search.route_pricing('2000000', '2078750', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/RoutePricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(route_pricing)

    def test_search_meal(self):
        search_meal = self.railway_api.railway_search.search_meal(CarType.UNKNOWN, 'sample string 1', 'sample string 2',
                                                     'sample string 4', self.datetime)

        input_data = json.loads(open('tests/data/Railway/Search/SearchMeal.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(search_meal)

    def test_reservation_create(self):

        customers = OrderFullCustomerRequest("4601123450", DocumentType.RUSSIAN_PASSPORT, 'Иван', 'Иванов',
                                             Sex.MALE, 1, 'Иванович', None, 'RU', None, self.datetime)

        passengers = [RailwayPassengerRequest(RailwayPassengerCategory.ADULT, 1, is_invalid=False)]

        reservation_items = RailwayReservationRequest('2006004', '2004001', self.datetime, '054Ч',
                                                      CarType.LUXURY, passengers, 1, '07', 1, 0, CabinGenderKind.NO_VALUE,
                                                      CarStorey.NO_VALUE, (1, 5), None, CabinPlaceDemands.NO_VALUE,
                                                      True, '1Л', AdditionalPlaceRequirements.NO_VALUE, None,
                                                      ProviderPaymentForm.CARD, None, None)

        create = self.railway_api.railway_reservation.create([customers], [reservation_items], '+79123456789', ['test@test.ru'])

        input_data = json.loads(open('tests/data/Order/Reservation/Create.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(create)

    def test_reservation_prolong_reservation(self):
        prolong_reservation = self.railway_api.railway_reservation.prolong_reservation(51978, None)

        input_data = json.loads(open('tests/data/Order/Reservation/ProlongReservation.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(prolong_reservation)

    def test_reservation_confirm(self):
        confirm = self.railway_api.railway_reservation.confirm(51978, provider_payment_form=ProviderPaymentForm.CARD)

        input_data = json.loads(open('tests/data/Order/Reservation/Confirm.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(confirm)

    @mock.patch('requests.Session', MockFileSession)
    def test_reservation_blank(self):
        api = API(self.username, self.password, self.pos)
        blank = api.railway_reservation.blank(1, 2)

        input_data = json.loads(open('tests/data/Order/Reservation/Blank.in.json', 'r', encoding='utf8').read())
        pdf_file = open(PDF_PATH, 'rb').read()

        self.assertEquals(input_data, api.last_request)
        self.assertEquals(blank.content, pdf_file)

    def test_reservation_cancel(self):
        cancel = self.railway_api.railway_reservation.cancel(51978)

        input_data = json.loads(open('tests/data/Order/Reservation/Cancel.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assertTrue(cancel)

    def test_reservation_return_amount(self):
        return_amount = self.railway_api.railway_reservation.return_amount('4601123450', 52159, [51948])

        input_data = json.loads(open('tests/data/Order/Reservation/ReturnAmount.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(return_amount)

    def test_reservation_auto_return(self):
        auto_return = self.railway_api.railway_reservation.auto_return('4601123450', 52157, [51946])

        input_data = json.loads(open('tests/data/Order/Reservation/AutoReturn.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(auto_return)

    def test_reservation_add_upsale(self):
        product_request = ProductRequest('AccidentAndLuggageLossAndDamage')
        service_add_upsale_request = ServiceAddUpsaleRequest('Igs', [1389, 1390], product_request)
        add_upsale = self.railway_api.railway_reservation.add_upsale(51978, 52919, service_add_upsale_request)

        input_data = json.loads(open('tests/data/Order/Reservation/AddUpsale.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(add_upsale)

    def test_reservation_refuse_upsale(self):
        refuse_upsale = self.railway_api.railway_reservation.refuse_upsale(1, 2, [1, 2])

        input_data = json.loads(open('tests/data/Order/Reservation/RefuseUpsale.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(refuse_upsale)

    def test_reservation_update_blanks(self):
        update_blanks = self.railway_api.railway_reservation.update_blanks(52159)

        input_data = json.loads(open('tests/data/Railway/Reservation/UpdateBlanks.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(update_blanks)

    def test_reservation_electronic_registration(self):
        electronic_registration = self.railway_api.railway_reservation.electronic_registration(52159, True, [51946])

        input_data = json.loads(open('tests/data/Railway/Reservation/ElectronicRegistration.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(electronic_registration)

    def test_reservation_meal_option(self):
        meal_option = self.railway_api.railway_reservation.meal_option(52159, 'Б', 51946)

        input_data = json.loads(open('tests/data/Railway/Reservation/MealOption.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(meal_option)

    @mock.patch('requests.Session', MockHTMLSession)
    def test_reservation_blank_as_html(self):
        api = API(self.username, self.password, self.pos)
        blank_as_html = api.railway_reservation.blank_as_html(1)

        input_data = json.loads(open('tests/data/Railway/Reservation/BlankAsHtml.in.json', 'r', encoding='utf8').read())
        html_file = open(HTML_PATH, 'r').read()

        self.assertEquals(input_data, api.last_request)
        self.assertEquals(blank_as_html.html, html_file)

    def test_order_info(self):
        order_info = self.railway_api.railway_info.info(51978)

        input_data = json.loads(open('tests/data/Order/Info/OrderInfo.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(order_info)

    def test_order_list(self):
        order_list = self.railway_api.railway_info.list(self.datetime, OperationType.PURCHASE)

        input_data = json.loads(open('tests/data/Order/Info/OrderList.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(order_list)

    def test_references_transport_nodes(self):
        transport_nodes = self.railway_api.references.transport_nodes()

        input_data = json.loads(open('tests/data/Info/References/TransportNodes.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(transport_nodes)

    def test_references_cities(self):
        cities = self.railway_api.references.cities()

        input_data = json.loads(open('tests/data/Info/References/Cities.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(cities)

    def test_references_countries(self):
        countries = self.railway_api.references.countries()

        input_data = json.loads(open('tests/data/Info/References/Countries.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(countries)

    def test_references_regions(self):
        regions = self.railway_api.references.regions()

        input_data = json.loads(open('tests/data/Info/References/Regions.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(regions)

    def test_partner_balances(self):
        balances = self.railway_api.partner_balances()

        self.assertEquals({}, self.railway_api.last_request)
        self.assert_json_with_class(balances)

    def test_search_pricing(self):
        search_pricing = self.railway_api.railway_search_pricing()

        input_data = json.loads(open('tests/data/Insurance/Search/Pricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.railway_api.last_request)
        self.assert_json_with_class(search_pricing)

    def test_aeroexpress_search_tariff_pricing(self):
        tariff_pricing = self.aeroexpress_api.aeroexpress_search.tariff_pricing(self.datetime)

        input_data = json.loads(open('tests/data/Aeroexpress/Aeroexpress/Search/TariffPricing.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assert_json_with_class(tariff_pricing)

    def test_aeroexpress_search_tariff_price_info(self):
        tariff_price_info = self.aeroexpress_api.aeroexpress_search.tariff_price_info(self.datetime, '2')

        input_data = json.loads(open('tests/data/Aeroexpress/Aeroexpress/Search/TariffPriceInfo.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assert_json_with_class(tariff_price_info)

    def test_aeroexpress_reservation_create(self):

        customers = OrderFullCustomerRequest("4601123450", DocumentType.RUSSIAN_PASSPORT, 'Иван', 'Иванов',
                                             Sex.MALE, 1, 'Иванович', None, 'RU', None, self.datetime)

        reservation_items = AeroexpressReservationRequest('3', self.datetime, [1], 1, '105', ProviderPaymentForm.CARD)

        create = self.aeroexpress_api.aeroexpress_reservation.create([customers], [reservation_items], '+79123456789', ['test@test.ru'])

        input_data = json.loads(open('tests/data/Aeroexpress/Order/Reservation/Create.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assert_json_with_class(create)

    def test_aeroexpress_reservation_confirm(self):
        confirm = self.aeroexpress_api.aeroexpress_reservation.confirm(51978, provider_payment_form=ProviderPaymentForm.CARD)

        input_data = json.loads(open('tests/data/Aeroexpress/Order/Reservation/Confirm.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assert_json_with_class(confirm)

    @mock.patch('requests.Session', MockFileSession)
    def test_aeroexpress_reservation_blank(self):
        api = API(self.username, self.password, self.pos)
        blank = api.railway_reservation.blank(1, 2)

        input_data = json.loads(open('tests/data/Aeroexpress/Order/Reservation/Blank.in.json', 'r', encoding='utf8').read())
        pdf_file = open(PDF_PATH, 'rb').read()

        self.assertEquals(input_data, api.last_request)
        self.assertEquals(blank.content, pdf_file)

    def test_aeroexpress_reservation_cancel(self):
        cancel = self.aeroexpress_api.aeroexpress_reservation.cancel(51978)

        input_data = json.loads(open('tests/data/Aeroexpress/Order/Reservation/Cancel.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assertTrue(cancel)

    def test_aeroexpress_reservation_void(self):
        void = self.aeroexpress_api.aeroexpress_reservation.void(51978)

        input_data = json.loads(open('tests/data/Aeroexpress/Order/Reservation/Void.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assert_json_with_class(void)

    def test_aeroexpress_reservation_auto_return(self):
        auto_return = self.aeroexpress_api.aeroexpress_reservation.auto_return(52157)

        input_data = json.loads(open('tests/data/Aeroexpress/Order/Reservation/AutoReturn.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assert_json_with_class(auto_return)

    def test_aeroexpress_order_info(self):
        order_info = self.aeroexpress_api.aeroexpress_info.info(51978)

        input_data = json.loads(open('tests/data/Aeroexpress/Order/Info/OrderInfo.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assert_json_with_class(order_info)

    def test_aeroexpress_order_list(self):
        order_list = self.aeroexpress_api.aeroexpress_info.list(self.datetime, OperationType.PURCHASE)

        input_data = json.loads(open('tests/data/Aeroexpress/Order/Info/OrderList.in.json', 'r', encoding='utf8').read())
        self.assertEquals(input_data, self.aeroexpress_api.last_request)
        self.assert_json_with_class(order_list)

    def test_empty_message_params(self):
        error_data = {'Code': 1, 'Message': 'Message'}
        self.assertTrue(OnelyaAPIError('Test/Test', error_data, {}).message_params is None)

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

        if var_name == 'from':
            return 'from_'

        return var_name.replace('$', '')

    @staticmethod
    def get_value(var):
        value = var
        if type(value) == datetime:
            value = value.strftime('%Y-%m-%dT%X')
        return value
