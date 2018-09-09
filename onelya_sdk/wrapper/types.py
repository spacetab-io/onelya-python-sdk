class ReturnTarget:
    RETURN = 'Return'
    EXCHANGE = 'Exchange'


class SpecialPlacesDemand:
    NO_VALUE = 'NoValue'
    INVALID = 'PlacesForDisabledPersons'
    VIP = 'PlacesForVipPersons'


class TariffType:
    STANDART = 'Standard'
    ROUND_TRIP = 'RoundTrip'
    BUSINESS = 'Business'
    CHILD = 'Child'


class RailwayTransitPermissionApprovalStatus:
    NO_VALUE = 'NoValue'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'


class MealTime:
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'


class ProlongReservationType:
    RAILWAY_THREE_HOURS_RESERVATION = 'RailwayThreeHoursReservation'


class PendingElectronicRegistration:
    NO_VALUE = 'NoValue'
    TO_CANCEL = 'ToCancel'


class CarGrouping:
    GROUP = 'Group'
    DONT_GROUP = 'DontGroup'


class PricingTariffType:
    FULL = 'Full'
    CHILD = 'Child'


class RzhdCardTypes:
    RZHD_BONUS = 'RzhdBonus'
    UNIVERSAL_RZHD_CARD = 'UniversalRzhdCard'


class RailwayServiceType:
    TICKETS = 'Tickets'
    TALONS = 'Talons'
    CRIMEA_TALONS = 'CrimeaTalons'


class SimpleOperationStatus:
    ERROR = 'Error'
    IN_PROCESS = 'InProcess'
    SUCCEEDED = 'Succeeded'


class OperationType:
    PURCHASE = 'Purchase'
    RETURN = 'Return'
    EXCHANGE = 'Exchange'


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


class Sex:
    NOVALUE = 'NoValue'
    MALE = 'Male'
    FEMALE = 'Female'


class ProviderPaymentForm:
    CASH = 'Cash'
    INVOICE = 'Invoice'
    CARD = 'Card'


class CarStorey:
    NO_VALUE = 'NoValue'
    FIRST = 'First'
    SECOND = 'Second'


class RailwayPassengerCategory:
    ADULT = 'Adult'
    CHILD = 'Child'
    BABY_WITHOUT_PLACE = 'BabyWithoutPlace'


class RailwayTravelEvent:
    INJURY = 'Injury'
    DEATH = 'Death'
    DISABILITY = 'Disability'


class TransportNodeType:
    AIRPORT = 'Airport'
    RAILWAY_STATION = 'RailwayStation'
    BUS_STOP = 'BusStop'
    AEROEXPRESS_STATION = 'AeroexpressStation'


class StationTimeDescription:
    NO_VALUE = 'NoValue'
    MOSCOW = 'Moscow'
    LOCAL = 'Local'
    GREENWICH = 'Greenwich'


class RouteStopType:
    NO_VALUE = 'NoValue'
    DEPARTURE = 'Departure'
    ARRIVAL = 'Arrival'
    INTERMEDIATE = 'Intermediate'


class CabinPlaceDemands:
    NO_VALUE = 'NoValue'
    IN_ONE_CABIN = 'InOneCabin'
    NO_SIDE_PLACES = 'NoSidePlaces'
    IN_ONE_COMPARTMENT = 'InOneCompartment'


class CabinGenderKind:
    NO_VALUE = 'NoValue'
    MIXED = 'Mixed'
    MALE = 'Male'
    FEMALE = 'Female'


class InsuranceSupplier:
    IGS = 'Igs'
    SOGAZ = 'Sogaz'
    RENESSANS = 'Renessans'
    ROSGOSSTRAH = 'Rosgosstrah'
    BLAGOSOSTOYANIE = 'Blagosostoyanie'


class PassengerSpecifyingRule:
    Standard = 'Standard'
    HELSINKI_WARSAW_CLASS11 = 'HelsinkiWarsawWithClass11'
    HELSINKI_WARSAW_CLASS12 = 'HelsinkiWarsawWithClass12'
    BERLIN_CLASS11 = 'BerlinWithClass11'
    BERLIN_CLASS12 = 'BerlinWithClass12'
    PARIS_PRAGUE_NIVE_CLASS11 = 'ParisPragueNiceWithClass11'
    PARIS_PRAGUE_NIVE_CLASS12 = 'ParisPragueNiceWithClass12'
    TWO_PLACE_AT_ONCE = 'TwoPlacesAtOnce'
    TWO_PLACE_AT_ONCE__ADDITIONAL_CHILD = 'TwoPlacesAtOnceWithAdditionalChild'
    FOUR_PLACE_AT_ONCE = 'FourPlacesAtOnce'
    KUPEK_TARIFF = 'KupekTariff'


class CarType:
    UNKNOWN = 'Unknown'
    SHARED = 'Shared'
    SOFT = 'Soft'
    LUXURY = 'Luxury'
    COMPARTMENT = 'Compartment'
    RESERVED_SEAT = 'ReservedSeat'
    SEDENTARY = 'Sedentary'


class BlankStatus:
    ELECTRONIC_REGISTRATION_ABSENT = 'ElectronicRegistrationAbsent'
    ELECTRONIC_REGISTRATION_PRESENT = 'ElectronicRegistrationPresent'
    NOT_CONFIRMED = 'NotConfirmed'
    VOIDED = 'Voided'
    RETURNED = 'Returned'
    PLACES_RETURNED = 'PlacesReturned'
    VOUCHER_ISSUED = 'VoucherIssued'


class DetailedOperationStatus:
    ERROR = 'Error'
    CREATED = 'Created'
    RESERVED = 'Reserved'
    IN_PROCESS_OF_CANCELLING = 'InProcessOfCancelling'
    IN_PROCESS_OF_FINALIZING = 'InProcessOfFinalizing'
    IN_PROCESS_OF_VOIDING = 'InProcessOfVoiding'
    IN_PROCESS = 'InProcess'
    SUCCEEDED = 'Succeeded'


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


class AdditionalPlaceRequirements:
    NO_VALUE = 'NoValue'
    MOTHER_AND_BABY_PLACES = 'MotherAndBabyPlaces'
    WITH_BABY_PLACES = 'WithBabyPlaces'
    WITH_PETS_PLACES = 'WithPetsPlaces'
    USUAL = 'Usual'
    USUAL_NEAR_THE_TABLE = 'UsualNearTheTable'
    ANY_NEAR_THE_TABLE = 'AnyNearTheTable'
    ANY_NOT_NEAR_THE_TABLE = 'AnyNotNearTheTable'
    NEAR_THE_PLAYGROUND = 'NearThePlayground'
    NEAR_THE_PLAYGROUND_AND_NOT_THE_TABLE = 'NearThePlaygroundAndNotTheTable'
    NEAR_THE_PLAYGROUND_AND_THE_TABLE = 'NearThePlaygroundAndTheTable'
    NEAR_THE_PLACES_WITH_PETS = 'NearThePlacesWithPets'
    FOLDABLE_PLACE = 'FoldablePlace'


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


class PreferredAdultTariffType:
    FULL = 'Full'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    PUPIL = 'Pupil'
    HOLIDAY = 'Holiday'
    WEDDING = 'Wedding'
    FAMILY = 'Family'
    KUPEK = 'Kupek'
    SINGLE = 'Single'
    TKS_P = 'TksP'
    TKS_M = 'TksM'
    TKS_I = 'TksI'


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


class TicketTariffType:
    FULL = 'Full'
    CHILD = 'Child'
    CHILD17 = 'Child17'
    FREE_CHILD = 'FreeChild'
    JUNIOR = 'Junior'
    SENIOR = 'Senior'
    BACKWARD_WAY_IN_ROUND_TRIP_WITH_DISCOUNT = 'BackwardWayInRoundTripWithDiscount'
    BACKWARD_WAY_IN_ROUND_TRIP_WITH_DISCOUNT_IN_INTERSTATE_DIRECTION = 'BackwardWayInRoundTripWithDiscountInInterstateDirection'
    UNIVERSAL_CARD = 'UniversalCard'
    PUPIL = 'Pupil'
    HOLIDAY = 'Holiday'
    WEDDING = 'Wedding'
    FAMILY = 'Family'
    KUPEK = 'Kupek'
    SINGLE = 'Single'
    TKS = 'Tks'
    CHILD_BACKWARD_WAY_IN_ROUND_TRIP_WITH_DISCOUNT = 'ChildBackwardWayInRoundTripWithDiscount'
    CHILD_BACKWARD_WAY_IN_ROUND_TRIP_WITH_DISCOUNT_IN_INTERSTATE_DIRECTION = 'ChildBackwardWayInRoundTripWithDiscountInInterstateDirection'
    BIRTHDAY = 'Birthday'
    UNKNOWN = 'Unknown'


class ReservationPlaceType:
    NO_VALUE = 'NoValue'
    NEAR_PLAYGROUND = 'NearPlayground'
    UPPER = 'Upper'
    NOT_NEAR_TABLE = 'NotNearTable'
    LOWER = 'Lower'
    MIDDLE = 'Middle'
    FOLDABLE = 'Foldable'
    WITH_PETS = 'WithPets'
    WITH_CHILD = 'WithChild'
    MOTHER_AND_BABY = 'MotherAndBaby'
    NEAR_PASSENGERS_WITH_PETS = 'NearPassengersWithPets'
    NEAR_TABLE = 'NearTable'
    NEAR_TABLE_PLAYGROUND = 'NearTablePlayground'
    SEPARATE_COMPARTMENT = 'SeparateCompartment'
    INVALIDS = 'Invalids'
    NEGOTIATIONS = 'Negotiations'


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
