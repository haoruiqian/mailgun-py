
from settings import *
import logging, requests
from exceptions import *

_logger = logging.getLogger('MailGun-PY')
for handler in LOGGER_HANDLERS:
    _logger.addHandler(handler)
_logger.setLevel(DEFAULT_LOGGER_LEVEL)

class MessageSender(object):
    resource_url = 'messages'
    def __init__(self, api_user, api_key, domain, timeout = 30):
        if not (api_user and api_key and domain):
            raise MissingRequiredFieldException()
        self.api_user = api_user
        self.api_key = api_key
        self.timeout = timeout
        self.url = '%s%s/%s' % (BASE_URL, domain, self.resource_url)

    def send(self, from_addr, to_addrs, subject, text = None, html = None, cc = None, bcc = None,
                    attachments = None, inline_files = None,
                    schedule_time = None, **kwargs):
        if not (from_addr and to_addrs and subject and (text or html)):
            _logger("Missing required parameters when sending email")
            raise MissingRequiredFieldException()
        args = kwargs
        args.update({'from': from_addr,
                'to': to_addrs,
                'subject': subject
                })
        if text:
            args['text'] = text
        if html:
            args['html'] = html
        files = []
        if attachments:
            if type(attachments) != list:
                attachments = [attachments]
            for attach in attachments:
                if type(attach) == file:
                    files.append(('attachment', attach))
                elif type(attach) in [str, unicode]:
                    files.append(('attachment', open(attach)))
        if inline_files:
            if type(inline_files) != list:
                inline_files = [inline_files]
            for inline_file in inline_files:
                if type(inline_file) == file:
                    files.append(('inline', inline_file))
                elif type(inline_file) in [str, unicode]:
                    files.append(('inline', open(inline_file)))
        if cc:
            args['cc'] = cc
        if bcc:
            args['bcc'] = bcc
        if schedule_time:
            args['o:deliverytime'] = schedule_time.strftime(DATETIME_FORMAT)
        response = requests.post(self.url, files = files, data = args,
            auth = (self.api_user, self.api_key), timeout = self.timeout)
        status = response.status_code
        if status != 200:
            raise APIException(status, response.text)