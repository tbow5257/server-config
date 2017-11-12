from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import *

engine = create_engine('postgresql:///immersivecatalog.db')
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

User2 = User(name="Bob McClarksky", email="bob@mcclarksky.biz",
             picture='https://api.adorable.io/avatars/285/abott@adorable.png')
session.add(User2)
session.commit()

# Headset examples
headset1 = Headset(user_id=1, type="VR", name="Oculus Rift", price=30000, FOV=100,
                   additional_components="Base stations")

session.add(headset1)
session.commit()

headset2 = Headset(user_id=1, type="AR", name="Samsung Galaxy", price=700, FOV=90, additional_components=None)

session.add(headset2)
session.commit()

headset3 = Headset(user_id=2, type="VR", name="HTC Vive", price=600, FOV=110, additional_components="Base stations")

session.add(headset3)
session.commit()

headset4 = Headset(user_id=1, type="AR", name="Iphone 8", price=800, FOV=50, additional_components=None)

session.add(headset4)
session.commit()

headset5 = Headset(user_id=2, type="VR", name="FOVE", price=800, FOV=110, additional_components=None)

session.add(headset5)
session.commit()

headset6 = Headset(user_id=1, type="AR", name="Magic Leap", price=1000, FOV=50, additional_components=None)

session.add(headset6)
session.commit()

headset7 = Headset(user_id=2, type="VR", name="Windows Mixed Reality Headset", price=449.99, FOV=95,
                   additional_components=None)

session.add(headset7)
session.commit()

headset8 = Headset(user_id=2, type="AR", name="Meta 2", price=1495.00, FOV=90, additional_components=None)

session.add(headset8)

# Experience examples
experience1 = Experience(user_id=1, type="VR", name="Space Pirate Trainer", description="Sci-fi shooting gallery",
                         price=14.99)

session.add(experience1)
session.commit()

experience2 = Experience(user_id=1, type="AR", name="Augment", description="Visualize 3D models in AR", price=None)

session.add(experience2)
session.commit()

experience3 = Experience(user_id=2, type="VR", name="Facebook Spaces",
                         description="Hangout with friends in a virtual environment", price=None)

session.add(experience3)
session.commit()

experience4 = Experience(user_id=1, type="AR", name="Snapchat", description="Share video and pictures with friends",
                         price=None)

session.add(experience4)
session.commit()

experience5 = Experience(user_id=1, type="VR", name="Accounting", description="Justin Roiland silliness", price=None)

session.add(experience5)
session.commit()

experience6 = Experience(user_id=1, type="AR", name="IKEA Place",
                         description="Look at 3D models of furniture in your home", price=None)

session.add(experience6)
session.commit()

experience7 = Experience(user_id=1, type="VR", name="Tethered", description="Fantasy strategy game", price=19.99)

session.add(experience7)
session.commit()

experience8 = Experience(user_id=1, type="AR", name="Star Wars Tabletop",
                         description="Visualize Star Wars on your coffee table", price=None)

session.add(experience8)
session.commit()
