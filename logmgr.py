import logging
import logging.config
import config
import sys 
import datetime

def getLogger(logfile_prefix):
    print("[Init]::Setup Logger")
    # Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
    logging.getLogger().setLevel(logging.NOTSET)

    # Add stdout handler, with level INFO
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    formater = logging.Formatter('%(name)-13s: %(levelname)-8s %(message)s')
    console.setFormatter(formater)
    logging.getLogger().addHandler(console)

    # Add file rotating handler, with level DEBUG

    _rotatingHandler = logging.handlers.RotatingFileHandler(
        filename=config.LOG_FOLDER + '/' + logfile_prefix + '-{:%Y-%m-%d}.log'.format(datetime.datetime.now()),
        maxBytes=(1048576 * config.LOG_MAX_SIZE), backupCount=config.LOG_BACKUP)
    _rotatingHandler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    _rotatingHandler.setFormatter(formatter)
    logging.getLogger().addHandler(_rotatingHandler)

    # Logger
    _logger = logging.getLogger("app." + __name__)

    return _logger