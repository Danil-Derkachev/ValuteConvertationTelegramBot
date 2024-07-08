import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv('TOKEN')  # Токен(пароль) моего бота
keys = {'евро': 'EUR',          # Доступные для конвертации валюты
        'рубль': 'RUB',
        'доллар': 'USD'}
