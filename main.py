import logging
import sys
import settings

import datetime
from api.gmo import APIClient
from api.gmo import Balance
from api.gmo import Order
from app.models.candle import BTC_JPY_BaseCandle1M
from app.models.candle import BTC_JPY_BaseCandle1H
from app.models.candle import BTC_JPY_BaseCandle1D

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    import app.models



