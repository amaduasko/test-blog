
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date,datetime
from modules.models import Role
from modules.models import User
from modules.models import Base




def random_date(numb=1): 
    start_dt = date.today().replace(day=numb, month=numb).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day


class Db():


  def __init__(self):
    print('initialize db')

  def create(self):
      print("creating db")

      # create the database
      engine = create_engine('sqlite:///data/data.sqlite')
      Base.metadata.create_all(engine)
      Session = sessionmaker()
      Session.configure(bind=engine)
      
      self.engine = engine
      self.session = Session()

      print("db created")

  def get_roles(self):
    return self.session.query(Role).all()
  
  def add_new_role(self, role_name, role_id):

    # Check if the role exists
    role = (
        self.session.query(Role)
        .filter(Role.name == role_name)
        .one_or_none()
    )

    # Does the role already exist?
    if role is not None:
        return

    # Create the new role
    if role is None:
      role = Role(id=role_id,name=role_name)
      # Add the role 
      self.session.add(role)

      # Commit to the database
      self.session.commit()
    
  def get_users(self):
    return self.session.query(User).all()
  

  def add_new_user(self,user_fio):
    users = self.get_users()

    # Check if the role exists
    user = (
        self.session.query(User)
        .filter(User.fio == user_fio)
        .one_or_none()
    )

    # Does the role already exist?
    if user is not None:
        return

    # Create the new role
    if user is None:
      user = User(
        id=len(users) + 1,
        fio = user_fio, 
        id_role= random.randint(1,2), 
        datar=random_date(random.randint(1,12)), 
        created_on=datetime.now())
      # Add the role 
      self.session.add(user)

      # Commit to the database
      self.session.commit()

  def get_users_selections(self):
    data = []
    roles = self.get_roles()

    users = self.session.query(User).order_by("created_on").slice(0,3)
    for user in users:
      role = [r for r in roles if r.id == user.id_role]
      user.role = role[0].name if role else ''
      data.append(user)
    return data




db = Db()