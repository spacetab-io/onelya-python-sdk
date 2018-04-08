from datetime import datetime
from onelya_sdk.wrapper.types import MealTime


class AdditionalMeal(object):
    def __init__(self, meal_time: MealTime, meal_option_code: str):
        self.meal_time = meal_time
        self.meal_option_code = meal_option_code
