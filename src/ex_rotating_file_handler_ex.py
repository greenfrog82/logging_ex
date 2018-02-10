import logging
import logging.config
import logging_ex.handlers

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandlerEx',
            'formatter': 'default',
            'filename': 'test.log',
            'owner': ['greenfrog', 'admin'],
            'chmod': 0660,
            'maxBytes': 60,
            'backupCount': 10,
            # 'delay': True
            'delay': False
        }
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

for idx in range(0, 10):
    logger.debug('%d > A debug message' % idx)
