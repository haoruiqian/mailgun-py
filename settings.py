
BASE_URL = 'https://api.mailgun.net/v3/'
DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %Z'

import logging
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
LOGGER_HANDLERS = [stream_handler]
DEFAULT_LOGGER_LEVEL = 'INFO'