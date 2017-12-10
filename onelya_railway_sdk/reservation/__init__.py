from ..utils import get_datetime, get_array
from ..wrapper.requests import RequestWrapper
from .requests import OrderFullCustomerRequest, RailwayReservationRequest
from ..wrapper import OrderCreateReservationCustomerResponse, RailwayReservationResponse

CREATE_METHOD = 'Railway/V1/Reservation/Create'


class RailwayReservation(object):

    def __init__(self, session):
        self.session = session
        self.request_wrapper = RequestWrapper(self.session)

    def create(self, customers: OrderFullCustomerRequest, reservation_items: RailwayReservationRequest,
               contact_phone=None, contact_emails=None):
        response = self.request_wrapper.make_request(CREATE_METHOD, customers=customers, contact_phone=contact_phone,
                                                     reservation_items=reservation_items, contact_emails=contact_emails)
        return CreateReservation(response)
class CreateReservation(object):
    def __init__(self, json_data):
        self.order_id = json_data.get('OrderId', None)
        self.amount = json_data.get('Amount', None)
        self.confirm_till = get_datetime(json_data.get('ConfirmTill', None))
        self.customers = get_array(json_data.get('Customers', None), OrderCreateReservationCustomerResponse)
        self.reservation_results = get_array(json_data.get('ReservationResults', None), RailwayReservationResponse)

        self.json_data = json_data
