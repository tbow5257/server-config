from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Headset, Experience, User

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

#Headset examples
headset1 = Headset(user_id=1, type="VR", name="Oculus Rift", price=30000, FOV=100, additional_components="Base stations")

session.add(headset1)
session.commit()

headset2 = Headset(user_id=1, type="AR", name="Samsung Galaxy", price=700, FOV=90, additional_components=None)

session.add(headset2)
session.commit()

#Experience examples
experience1 = Experience(user_id=1, name="Space Pirate Trainer", description="somethin somethin", price=29.99, Headset=headset1)

session.add(experience1)
session.commit()

experience2 = Experience(user_id=1, name="Augment", description="yo mamama weo fpawef kjawe fpaw efpajw efjoiapejfpew", price=333, Headset=headset2)

session.add(experience2)
session.commit()
