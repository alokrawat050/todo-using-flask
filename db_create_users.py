from app import db
from models import User

# insert data
db.session.add(User("alok", "alok@gmail.com", "mypassword"))
db.session.add(User("admin", "ad@min.com", "admin"))

# commit the changes
db.session.commit()