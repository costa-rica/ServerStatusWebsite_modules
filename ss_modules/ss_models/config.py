import os
from ss_config import ConfigDev, ConfigProd, ConfigLocal

match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- ss_models/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- ss_models/config: Production')
    case _:
        config = ConfigLocal()
        print('- ss_models/config: Local')
    