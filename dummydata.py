from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, VRHeadset, VRExperience, User

engine = create_engine('sqlite:///immersivecatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Developer Mcgeeface", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

#VR Headset example
vrheadset1 = VRHeadset(user_id=1, name="GeezerVR", price=30000, FOV=290, additional_components=None)

session.add(vrheadset1)
session.commit()

vrheadset2 = VRHeadset(user_id=1, name="Wtf", price=10, FOV=10, additional_components="maybe theres somethin")

session.add(vrheadset2)
session.commit()

vrexperience1 = VRExperience(user_id=1, name="lolwut", description="somethin somethin", price=333, VRHeadset=vrheadset1)

session.add(vrexperience1)
session.commit()

