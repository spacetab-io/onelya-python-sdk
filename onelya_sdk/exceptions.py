

class OnelyaAPIError(Exception):
    __slots__ = ['code', 'message', 'message_params', 'request_data']

    def __init__(self, method, error_data, request_data):
        super(OnelyaAPIError, self).__init__()
        self.method = method.replace("/", "-")
        self.error_data = error_data
        self.request_data = request_data

        self.code = error_data.get('Code')
        self.message = error_data.get('Message').replace('request.', '')
        try:
            self.message_params = self.__prettify_message_params(error_data, request_data)
        except:
            self.message_params = 'Can\'t prettify message'

    @staticmethod
    def __prettify_message_params(error_data, request_data):
        message_params = error_data.get('MessageParams', None)
        if message_params is not None:
            json_message_params = {}
            for message in message_params:
                for item in message.split(', '):
                    param_key = item.split('.')[1].split(' =')[0]
                    json_message_params[param_key] = request_data[param_key]
            return json_message_params
        return message_params

    def __str__(self):
        error_message = '''Code: {self.code}
        Message: {self.message}
        MessageParams: {self.message_params}
        Docs: https://test.onelya.ru/ApiDocs/Api?apiId={self.method}'''.format(self=self)
        return error_message
