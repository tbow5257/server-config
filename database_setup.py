
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

#Table to provide many to many model for Headsets and Experiences
compatible = Table('compatible',
                   Base.metadata,
        Column('headset_id', Integer, ForeignKey('headset.id')),
        Column('experience_id', Integer, ForeignKey('experience.id'))
    )

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Headset(Base):
    __tablename__ = 'headset'
    type = Column(
        String(2), nullable=False
    )

    name = Column(
        String(80), nullable=False
    )

    price = Column(
        String(8), nullable=False
    )

    FOV = Column(
        String(3), nullable=False
    )

    additional_components = Column(
        String(80)
    )

    id = Column(
        Integer, primary_key=True
    )

    user_id = Column(
        Integer, ForeignKey('user.id')
    )

    user = relationship(
        User
    )


class Experience(Base):
    __tablename__ = 'experience'

    name = Column(
        String(80), nullable=False
    )

    id = Column(
        Integer, primary_key=True
    )

    description = Column(String(250))

    price = Column(String(8))

    Headset = relationship(
        Headset, secondary=compatible,
        backref = backref('runs_on', lazy = 'dynamic')
    )

    user_id = Column(
        Integer, ForeignKey('user.id')
    )

    user = relationship(
        User
    )

engine = create_engine('sqlite:///immersivecatalog.db')

Base.metadata.create_all(engine)
