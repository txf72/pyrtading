import configparser
from utils.utils import bool_from_str


conf = configparser.ConfigParser()
conf.read("settings.ini")

account_id = conf["gmo"]["account_id"]
access_token = conf["gmo"]["access_token"]
product_code = conf["gmo"]["product_code"]

db_name = conf["db"]["name"]
db_driver = conf["db"]["driver"]

web_port = int(conf["web"]["port"])

trade_duration = conf["pytrading"]["trade_duration"].lower()
back_test = bool_from_str(conf["pytrading"]["back_test"])
use_percent = float(conf["pytrading"]["use_percent"])
past_period = int(conf["pytrading"]["past_period"])
stop_limit_percent = float(conf["pytrading"]["stop_limit_percent"])
num_ranking = int(conf["pytrading"]["num_ranking"])

JPY = int(conf["coin"]["JPY"])
BTC = int(conf["coin"]["BTC"])
ETH = int(conf["coin"]["ETH"])
BCH = int(conf["coin"]["BCH"])
LTC = int(conf["coin"]["LTC"])
XRP = int(conf["coin"]["XRP"])
XEM = int(conf["coin"]["XEM"])
XLM = int(conf["coin"]["XLM"])
BAT = int(conf["coin"]["BAT"])
OMG = int(conf["coin"]["OMG"])
XTZ = int(conf["coin"]["XTZ"])
QTUM = int(conf["coin"]["QTUM"])