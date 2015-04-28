
class InvalidEmailException(Exception):
    pass

class MissingRequiredFieldException(Exception):
    pass

resp_status_code_messages = {
    400: 'Bad Request - Often missing a required parameter',
    401: 'Unauthorized - No valid API key provided',
    402: 'Request Failed - Parameters were valid but request failed',
    404: "Not Found - The requested item doesn't exist",
    500: "Server Errors - something is wrong on Mailgun's end"
}
resp_status_code_messages[502] = resp_status_code_messages[500]
resp_status_code_messages[503] = resp_status_code_messages[500]
resp_status_code_messages[504] = resp_status_code_messages[500]

class APIException(Exception):
    message = "API did not return 200"
    def __init__(self, status_code, response):
        self.status_code = status_code
        self.response = response
        self.message = resp_status_code_messages.get(self.status_code, 'mailgun failed to handle your request')

    def __str__(self):
        return "API response status code: %d, %s, the response data is: \n%s"\
            % (self.status_code, self.message, self.response)