

class OnelyaAPIError(Exception):
    __slots__ = ['code', 'message', 'message_params']

    def __init__(self, error_data):
        super(OnelyaAPIError, self).__init__()
        self.error_data = error_data

        self.code = error_data.get('Code')
        self.message = error_data.get('Message')
        self.message_params = self.get_pretty_message_params(error_data)

    @staticmethod
    def get_pretty_message_params(error_data):
        message_params = error_data.get('MessageParams', None)
        message_params = None if message_params is None else {param['key']: param['value'] for param in message_params}
        return message_params

    def __str__(self):
        error_message = 'Code: {self.code}\nMessage: {self.message}\nMessageParams: {self.message_params}'.format(self=self)
        return error_message
