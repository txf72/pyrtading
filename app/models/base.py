from contextlib import contextmanager
import logging
import threading
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import settings
import app.models.candle


logger = logging.getLogger(__name__)
Base = declarative_base()
engine = create_engine(f"sqlite:///{settings.db_name}?check_seme_thread=False")
Session = scoped_session(sessionmaker(bind=engine))
lock = threading.Lock()


@contextmanager
def session_scope():
    session = Session()
    session.expire_on_commit = False
    try:
        lock.acquire()
        yield session
        session.commit()

    except Exception as e:
        logger.error(f"action=session_scope error={e}")
        session.rollback()
        raise

    finally:
        session.expire_on_commit = True
        lock.release()


def init_db():
    Base.metadata.create_all(bind=engine)
