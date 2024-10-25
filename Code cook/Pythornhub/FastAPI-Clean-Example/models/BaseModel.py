from sqlalchemy.ext.declarative import declarative_base

from configs.Database import Engine

EntityMeta = declarative_base()


def init():
    EntityMeta.metadata.create_all(bind=Engine)
