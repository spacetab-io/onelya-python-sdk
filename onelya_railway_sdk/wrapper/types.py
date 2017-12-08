
class TransportType:
    TRAIN = 'Train'
    BUS = 'Bus'
    FERRY = 'Ferry'


class StationTimeDescription:
    NO_VALUE = 'NoValue'
    MOSCOW = 'Moscow'
    LOCAL = 'Local'
    GREENWICH = 'Greenwich'


class BookingSystem:
    EXPRESS_3 = 'Express3'
    EXPRESS_2 = 'Express2'
    TEEMA = 'Teem'


class RoutePolicy:
    INTERNAL = 'Internal'
    FINLAND = 'Finland'
    INTERNATIONAL = 'International'


class CarGrouping:
    GROUP = 'Group'
    DONT_GROUP = 'DontGroup'


class CarServices:
    BEDCLOTHES = 'Bedclothes'
    MEAL = 'Meal'
    WIFI = 'Wifi'
    TV = 'Tv'
    HYGIENIC_KIT = 'HygienicKit'
    PRESS = 'Press'
    AIR_CONDITIONING = 'AirConditioning'
    BIO_TOILET = 'BioToilet'
    PLAID = 'Plaid'
    WASHBASIN_IN_COMPARTMENT = 'WashbasinInCompartment'
    SHOWE_RROOM_IN_COMPARTMENT = 'ShowerRoomInCompartment'
    HYGIENIC_SHOWER = 'HygienicShower'
    SOCKET_220V = 'Socket220V'
    SLIPPERS = 'Slippers'
    PETS_CARRIAGE = 'PetsCarriage'
    PLACES_FOR_PASSENGER_WITH_BABY = 'PlacesForPassengerWithBaby'
    TRANSFER = 'Transfer'


class CarType:
    UNKNOWN = 'Unknown'
    SHARED = 'Shared'
    SOFT = 'Soft'
    LUXURY = 'Luxury'
    COMPARTMENT = 'Compartment'
    RESERVED_SEAT = 'ReservedSeat'
    SEDENTARY = 'Sedentary'


class DiscountType:
    NO_VALUE = 'NoValue'
    SENIOR = 'Senior'
    JUNIOR = 'Junior'
    ROUND_TRIP = 'RoundTrip'
    ROUND_TRIP_IN_INTERSTATE_DIRECTION = 'RoundTripInInterstateDirection'
    PUPIL = 'Pupil'
    UNIVERSAL_CARD = 'UniversalCard'
    HOLIDAY = 'Holiday'
    WEDDING = 'Wedding'
    FAMILY = 'Family'
    KUPEK = 'Kupek'
    SINGLE = 'Single'


class PlaceReservationType:
    USUAL = 'Usual'
    TWO_PLACE_AT_ONCE = 'TwoPlacesAtOnce'
    FOUR_PLACE_AT_ONCE = 'FourPlacesAtOnce'