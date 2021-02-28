from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from dolphin.config.ConfigHelper import ConfigHelper

Base = declarative_base(class_registry={

})

url = ConfigHelper.getValue('global', 'conn')
engine = create_engine(url, echo=False, encoding="utf-8")
Session = sessionmaker(bind=engine)
session = Session()
