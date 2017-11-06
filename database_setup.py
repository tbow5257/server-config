from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture,
        }


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

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'type': self.type,
            'name': self.name,
            'price': self.price,
            'FOV': self.FOV,
            'additional_components': self.additional_components,
            'id': self.id,
            'user_id': self.user_id,
        }


class Experience(Base):
    __tablename__ = 'experience'

    type = Column(
        String(2), nullable=False
    )

    name = Column(
        String(80), nullable=False
    )

    id = Column(
        Integer, primary_key=True
    )

    description = Column(String(250))

    price = Column(String(8))

    user_id = Column(
        Integer, ForeignKey('user.id')
    )

    user = relationship(
        User
    )

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'type': self.type,
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'price': self.price,
            'user_id': self.user_id,
        }


engine = create_engine('sqlite:///immersivecatalog.db')

Base.metadata.create_all(engine)
