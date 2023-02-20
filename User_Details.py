from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, or_
from sqlalchemy.orm import declarative_base, sessionmaker
from databaseLogin import DBLogin
import pandas as pd

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    mobile_number = Column(String(255), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, nullable=False, default=datetime.now)
    last_updated_date = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, fname='', lname='', email_id='', user_pass='', mob_num=''):
        self.first_name = fname
        self.last_name = lname
        self.email = email_id
        self.password = user_pass
        self.mobile_number = mob_num

    @classmethod
    def user_creation(cls, fname, lname, email_id, user_pass, mob_num):
        try:
            engine = DBLogin().db_connection()
        except Exception as e:
            print(e)
            return "!Error: Fail to connect with DB"

        Session = sessionmaker(bind=engine)
        session = Session()

        # Check if user with same email or mobile number already exists
        existing_user = session.query(User).filter(or_(User.email == email_id, User.mobile_number == mob_num)).first()

        if existing_user:
            return "Error! User Already Exists."

        # Create new user object
        user = User(fname, lname, email_id, user_pass, mob_num)
        session.add(user)
        session.commit()
        session.close()
        return None

    @classmethod
    def user_update_pass(cls, email_id, user_pass):
        engine = DBLogin().db_connection()
        if not engine:
            return "!Error: Fail to connect with DB"

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            existing_user = session.query(cls).filter_by(email=email_id).first()
            if not existing_user:
                return 'Error! User not found'

            existing_user.password = user_pass
            session.commit()

            return None

        except Exception as ex:
            print("Error while updating the Password : \n", ex)
            return "Error! while updating the Password"

    @classmethod
    def user_update_mobile(cls, email_id, mob_num):
        engine = DBLogin().db_connection()
        if not engine:
            return "!Error: Fail to connect with DB"

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            existing_user = session.query(cls).filter_by(email=email_id).first()
            if not existing_user:
                return 'Error! User not found'

            existing_user.mobile_number = mob_num
            session.commit()

            return None

        except Exception as ex:
            print("Error while updating the Mobile Number : \n", ex)
            return "Error! while updating the Mobile Number"

    @classmethod
    def user_update_fname(cls, email_id, fname):
        engine = DBLogin().db_connection()
        if not engine:
            return "!Error: Fail to connect with DB"

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            existing_user = session.query(cls).filter_by(email=email_id).first()
            if not existing_user:
                return 'Error! User not found'

            existing_user.first_name = fname
            session.commit()

            return None

        except Exception as ex:
            print("Error while updating the First Name : \n", ex)
            return "Error! while updating the First Name"

    @classmethod
    def user_update_lname(cls, email_id, lname):
        engine = DBLogin().db_connection()
        if not engine:
            return "!Error: Fail to connect with DB"

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            existing_user = session.query(cls).filter_by(email=email_id).first()
            if not existing_user:
                return 'Error! User not found'

            existing_user.last_name = lname
            session.commit()

            return None

        except Exception as ex:
            print("Error while updating the Last Name : \n", ex)
            return "Error! while updating the Last Name"

    @classmethod
    def all_user_list(cls):
        engine = DBLogin().db_connection()
        if not engine:
            return "!Error: Fail to connect with DB"

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            all_users = session.query(cls)

            user_dict = {'User_id': [], 'first_name': [], 'last_name': [], 'email': [], 'mobile_number': [],
                         'is_active': [], 'created_date': [], 'last_updated_date': []}

            for my_user in all_users:

                user_dict['User_id'].append(my_user.user_id)
                user_dict['first_name'].append(my_user.first_name)
                user_dict['last_name'].append(my_user.last_name)
                user_dict['email'].append(my_user.email)
                user_dict['mobile_number'].append(my_user.mobile_number)
                user_dict['is_active'].append(my_user.is_active)
                user_dict['created_date'].append(my_user.created_date)
                user_dict['last_updated_date'].append(my_user.last_updated_date)
                # user_dict['role_id'].append(my_user.role_id)

            print('return Dict...')
            return user_dict

        except Exception as ex:
            print("Error while Extracting the User Details : \n", ex)
            return "Error! while Extracting the User Details"
