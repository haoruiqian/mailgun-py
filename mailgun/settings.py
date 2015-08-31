
BASE_URL = 'https://api.mailgun.net/v3/'
DATETIME_FORMAT = '%a, %d %b %Y %H:%M:%S %Z'

import logging
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
LOGGER_HANDLERS = [stream_handler]
DEFAULT_LOGGER_LEVEL = 'INFO'

allowed_levels = ('INFO', 'WARNING', 'ERROR', 'DEBUG')

def set_default_logger_level(level):
    if level not in allowed_levels:
        raise Exception('%s not in allowed levels "%s"' % (level, ','.join(allowed_levels)))
    DEFAULT_LOGGER_LEVEL = level