from datetime import datetime
from onelya_sdk.utils import get_array, get_item
from onelya_sdk.wrapper import FeeCalculation, RaceInfo, TariffPriceInfoResponse

TARIFF_PRICING_METHOD = 'Aeroexpress/V1/Search/TariffPricing'
TARIFF_PRICE_INFO_METHOD = 'Aeroexpress/V1/Search/TariffPriceInfo'


class Search(object):
    def __init__(self, request_wrapper):
        self.__request_wrapper = request_wrapper

    def tariff_pricing(self, departure_date: datetime):
        response = self.__request_wrapper.make_request(TARIFF_PRICING_METHOD, departure_date=departure_date)
        return TariffPricing(response)

    def tariff_price_info(self, departure_date: datetime, tariff_id: str):
        response = self.__request_wrapper.make_request(TARIFF_PRICE_INFO_METHOD, departure_date=departure_date,
                                                       tariff_id=tariff_id)
        return TariffPriceInfo(response)


class TariffPricing(object):
    def __init__(self, json_data):
        self.tariffs = get_array(json_data.get('Tariffs'), TariffPriceInfoResponse)

        self.json_data = json_data


class TariffPriceInfo(object):
    def __init__(self, json_data):
        self.document_types = json_data.get('DocumentTypes')
        self.client_fee_calculation = get_item(json_data.get('ClientFeeCalculation'), FeeCalculation)
        self.agent_fee_calculation = get_item(json_data.get('AgentFeeCalculation'), FeeCalculation)
        self.tariff_id = json_data.get('TariffId')
        self.tariff_name = json_data.get('TariffName')
        self.tariff_type = json_data.get('TariffType')
        self.route_name = json_data.get('RouteName')
        self.description = json_data.get('Description')
        self.price = json_data.get('Price')
        self.max_tickets_quantity_allowed_for_booking = json_data.get('MaxTicketsQuantityAllowedForBooking')
        self.is_for_guaranteed_seats = json_data.get('IsForGuaranteedSeats')
        self.races = get_array(json_data.get('Races'), RaceInfo)

        self.json_data = json_data
