import lesson.utils as utils
from lesson.utils import find_seat_for_passanger
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
train_id = config['my_config']['train_id']


res = find_seat_for_passanger('34')
