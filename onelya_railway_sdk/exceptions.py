

class OnelyaAPIError(Exception):
    __slots__ = ['code', 'message', 'message_params']

    def __init__(self, error_data):
        super(OnelyaAPIError, self).__init__()
        self.error_data = error_data

        self.code = error_data.get('Code')
        self.message = error_data.get('Message')
        self.message_params = error_data.get('MessageParams', None)

    def __str__(self):
        error_message = 'Code: {self.code}\nMessage: {self.message}\nMessageParams: {self.message_params}'.format(self=self)
        return error_message
