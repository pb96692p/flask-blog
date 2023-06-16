#from app import app, db

#if __name__ == '__main__':
 #   with app.app_context():
  #      db.create_all()

from app import db, app, User

# Create an application context
with app.app_context():
    # Create a new User instance
    user_1 = User(username='admin', email='admin@gmail.com', password='password')

    # Add the user to the database session
    db.session.add(user_1)

    # Commit the changes to the database
    db.session.commit()
