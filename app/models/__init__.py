from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

from config import get_config

config = get_config()

# Engine の作成
Engine = create_engine(
    config.CONNECT_STR
)

# Sessionの作成
session = Session(
    autocommit=False,
    autoflush=True,
    bind=Engine
)

Base = declarative_base()
