# coding:utf8

import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy.exc import SQLAlchemyError

from dolphin.common.db.DatabaseService import Base, session
from dolphin.common.utils import crontab_run_next_time

logger = CommonLogger().getlogger()


class Poem(Base):
    __tablename__ = 'rss_sub_source'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    sub_url = Column(String, primary_key=False, nullable=False)
    sub_status = Column(Integer, primary_key=False, nullable=False)
    trigger_count = Column(Integer, primary_key=False, nullable=False)
    failed_count = Column(Integer, primary_key=False, nullable=False)
    next_trigger_time = Column(String, primary_key=False, nullable=False)
    rss_type = Column(String, primary_key=False, nullable=False)
    cron = Column(String, primary_key=False, nullable=False)
    standard_type = Column(String, primary_key=False, nullable=False)
    standard_version = Column(String, primary_key=False, nullable=False)
    lang = Column(String, primary_key=False, nullable=False)
    intro = Column(String, primary_key=False, nullable=False)
    sub_name = Column(String, primary_key=False, nullable=False)
    reputation = Column(Integer, primary_key=False, nullable=False)

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def select():
        rss = None
        try:
            now = datetime.datetime.now()
            rss = session.query(RssSource)\
                .filter(RssSource.sub_status == 1, RssSource.next_trigger_time <= now)\
                .order_by(RssSource.failed_count.asc())\
                .all()
        except SQLAlchemyError as e:
            session.rollback()
            logger.error("query rss source error", e)
        finally:
            session.close()
        return rss

    @staticmethod
    def update(source, success):
        try:
            new = session.query(RssSource).filter(RssSource.id == source.id).first()
            new.trigger_count = source.trigger_count + 1
            next_date = crontab_run_next_time(source.cron)
            new.next_trigger_time = next_date[0]
            if success is not True:
                new.failed_count = new.failed_count + 1
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            logger.error("update rss source error", e)
        finally:
            session.close()

    def update_sub_name(self, source, sub_name):
        try:
            new = session.query(RssSource).filter(RssSource.id == source.id).first()
            new.sub_name = sub_name
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
        finally:
            session.close()

    def update_intro(self, source, intro):
        try:
            new = session.query(RssSource).filter(RssSource.id == source.id).first()
            new.intro = intro
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
        finally:
            session.close()

    def update_lang(self, source, lang):
        try:
            new = session.query(RssSource).filter(RssSource.id == source.id).first()
            new.lang = lang
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
        finally:
            session.close()
