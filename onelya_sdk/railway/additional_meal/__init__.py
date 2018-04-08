from datetime import datetime
from onelya_sdk.utils import get_array, get_item
from onelya_sdk.wrapper.types import ProviderPaymentForm
from onelya_sdk.wrapper import (AdditionalMealOption, RateValue, AdditionalMealOption)

PRICING_METHOD = 'Railway/V1/AdditionalMeal/Pricing'
PURCHASE_METHOD = 'Railway/V1/AdditionalMeal/Purchase'
RETURN_METHOD = 'Railway/V1/AdditionalMeal/Return'


class AdditionalMeal(object):
    def __init__(self, request_wrapper):
        self.__request_wrapper = request_wrapper

    def pricing(self, order_item_id: int):
        response = self.__request_wrapper.make_request(PRICING_METHOD, order_item_id=order_item_id)
        return Pricing(response)

    def purchase(self, order_item_id: int, order_item_blank_id: int, meal_times: 'list of MealTimes',
                 agent_payment_id: str, agent_reference_id: str, provider_payment_form: ProviderPaymentForm):
        response = self.__request_wrapper.make_request(PURCHASE_METHOD, order_item_id=order_item_id,
                                                       order_item_blank_id=order_item_blank_id,
                                                       meal_times=meal_times,
                                                       agent_payment_id=agent_payment_id,
                                                       agent_reference_id=agent_reference_id,
                                                       provider_payment_form=provider_payment_form)
        return Purchase(response)

    def return_(self, order_item_id: int, agent_reference_id: str):
        response = self.__request_wrapper.make_request(RETURN_METHOD, order_item_id=order_item_id,
                                                       agent_reference_id=agent_reference_id)
        return Return(response)


class Pricing(object):
    def __init__(self, json_data):
        self.meal_options = get_array(json_data.get('MealOptions'), AdditionalMealOption)

        self.json_data = json_data


class Purchase(object):
    def __init__(self, json_data):
        self.order_item_id = get_item(json_data.get('OrderItemId'), int)
        self.vat_rate_values = get_array(json_data.get('VatRateValues'), RateValue)
        self.meal_times = get_array(json_data.get('MealTimes'), AdditionalMealOption)
        self.agent_reference_id = json_data.get('AgentReferenceId')

        self.json_data = json_data


class Return(object):
    def __init__(self, json_data):
        self.order_item_id = get_item(json_data.get('OrderItemId'), int)
        self.amount = get_item(json_data.get('Amount'), float)
        self.agent_reference_id = json_data.get('AgentReferenceId')

        self.json_data = json_data
