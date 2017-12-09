

class CarGrouping:
    GROUP = 'Group'
    DONT_GROUP = 'DontGroup'


class PricingTariffType:
    FULL = 'Full'
    CHILD = 'Child'


class RzhdCardTypes:
    RZHD_BONUS = 'RzhdBonus'
    UNIVERSAL_RZHD_CARD = 'UniversalRzhdCard'


class TransportType:
    TRAIN = 'Train'
    BUS = 'Bus'
    FERRY = 'Ferry'


class PlaceReservationType:
    USUAL = 'Usual'
    TWO_PLACE_AT_ONCE = 'TwoPlacesAtOnce'
    FOUR_PLACE_AT_ONCE = 'FourPlacesAtOnce'


class BookingSystem:
    EXPRESS_3 = 'Express3'
    EXPRESS_2 = 'Express2'
    TEEM = 'Teem'


class RoutePolicy:
    INTERNAL = 'Internal'
    FINLAND = 'Finland'
    INTERNATIONAL = 'International'


class StationTimeDescription:
    NO_VALUE = 'NoValue'
    MOSCOW = 'Moscow'
    LOCAL = 'Local'
    GREENWICH = 'Greenwich'


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


class DocumentType:
    RUSSIAN_PASSPORT = 'RussianPassport'
    RUSSIAN_FOREIGN_PASSPORT = 'RussianForeignPassport'
    FOREIGN_PASSPORT = 'ForeignPassport'
    BIRTH_CERTIFICATE = 'BirthCertificate'
    MILITARY_CARD = 'MilitaryCard'
    MILITARY_OFFICER_CARD = 'MilitaryOfficerCard'
    RETURN_TO_CIS_CERTIFICATE = 'ReturnToCisCertificate'
    DIPLOMATIC_PASSPORT = 'DiplomaticPassport'
    SERVICE_PASSPORT = 'ServicePassport'
    SAILOR_PASSPORT = 'SailorPassport'
    STATELESS_PERSON_IDENTITY_CARD = 'StatelessPersonIdentityCard'
    RESIDENCE_PERMIT = 'ResidencePermit'
    RUSSIAN_TEMPORARY_IDENTITY_CARD = 'RussianTemporaryIdentityCard'


class CarService:
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


class CarPlaceType:
    NOVALUE = 'NoValue'
    SEPARATE_COMPARTMENT = 'SeparateCompartment'
    SIDE_LOWER_NEAR_RESTROOM = 'SideLowerNearRestroom'
    SIDE_UPPER_NEAR_RESTROOM = 'SideUpperNearRestroom'
    THIRD_SHELF = 'ThirdShelf'
    FOLDABLE = 'Foldable'
    UPPER = 'Upper'
    LOWER = 'Lower'
    USUAL = 'Usual'
    LAST_KUPE_LOWER = 'LastKupeLower'
    LAST_KUPE_UPPER = 'LastKupeUpper'
    MIDDLE = 'Middle'
    WITH_BICYCLE = 'WithBicycle'
    SIDE_LOWER = 'SideLower'
    SIDE_UPPER = 'SideUpper'
    NEAR_PLAYGROUND = 'NearPlayground'
    NEAR_TABLE_PLAYGROUND = 'NearTablePlayground'
    NEAR_TABLE = 'NearTable'
    WITH_PETS = 'WithPets'
    MOTHER_AND_BABY = 'MotherAndBaby'
    WITH_CHILD = 'WithChild'
    NEAR_PASSENGER_SWITH_PETS = 'NearPassengersWithPets'
    INVALIDS_LOWER = 'InvalidsLower'
    INVALIDS_UPPER = 'InvalidsUpper'
    NEGOTIATIONS = 'Negotiations'