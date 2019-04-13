import configparser
import os

const_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(const_path, '..', 'config', 'posted.cfg')
config = configparser.ConfigParser()
config.read(config_path)


#### Database ######
HOSTNAME = config['database']['HOSTNAME']
PORT = config['database']['PORT']
USERNAME = config['database']['USERNAME']
PASSWORD = config['database']['PASSWORD']
DB = config['database']['DB']
