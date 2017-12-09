from ..wrapper.requests import RequestWrapper
from .wrapper import CreateReservation, OrderFullCustomerRequest, RailwayReservationRequest

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