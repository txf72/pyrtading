import logging
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from app.models.base import Base
from app.models.base import session_scope

logger = logging.getLogger(__name__)


class BaseCandle():
    time = Column(DateTime, primary_key=True, nullable=False)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Integer)

    @classmethod
    def create(cls, time, open, close, high, low, volume):
        candle = cls(time=time,
                     open=open,
                     close=close,
                     high=high,
                     low=low,
                     volume=volume)
        try:
            with session_scope() as session:
                session.add(candle)
            return candle
        except IntegrityError:
            return False

    @classmethod
    def get(cls, time):
        with session_scope() as session:
            candle = session.query(cls).filter(
                cls.time == time).first()
        if candle is None:
            return None

        return candle

    def save(self):
        with session_scope() as session:
            session.add(self)

    @classmethod
    def get_all_candles(cls, limit=100):
        with session_scope() as session:
            candles = session.query(cls).order_by(
                desc(cls.time)
            ).limit(limit).all()

        if candles is None:
            return None

        candles.reverse()
        return candles

    @property
    def value(self):
        return {
            "time": self.time,
            "open": self.open,
            "close": self.close,
            "high": self.low,
            "volume": self.volume
        }


class BTC_JPY_BaseCandle1D(BaseCandle, Base):
    __tablename__ = "BTC_JPY_1D"


class BTC_JPY_BaseCandle1H(BaseCandle, Base):
    __tablename__ = "BTC_JPY_1H"


class BTC_JPY_BaseCandle1M(BaseCandle, Base):
    __tablename__ = "BTC_JPY_1M"
