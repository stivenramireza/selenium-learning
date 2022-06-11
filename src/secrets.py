from dotenv import load_dotenv

from src.logger import logger

import os

ENV = os.environ.get('ENV')
if ENV == 'production':
    dotenv_path = '.env'
    logger.info('Using production environment variables')
else:
    dotenv_path = '.env.dev'
    logger.info('Using development environment variables')

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception('env files do not exist')

load_dotenv(dotenv_path)

DRIVER_PATH = os.environ.get('DRIVER_PATH')
