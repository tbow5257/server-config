import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


class VRHeadset(Base):
    __tablename__ = 'vr_headset'
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


class VRExperience(Base):
    __tablename__ = 'vr_experience'

    name = Column(
        String(80), nullable=False
    )

    id = Column(
        Integer, primary_key=True
    )

    description = Column(String(250))

    price = Column(String(8))

    VRHeadset_id = Column(
        Integer, ForeignKey('vr_headset.id')
    )

    restaurant = relationship(VRHeadset)

    @property
    def serialize(self):
        #returns object data in easliy serializeable format
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'price' : self.price,
        }

engine = create_engine('sqlite:///immersivecatalog.db')

Base.metadata.create_all(engine)
