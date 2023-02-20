from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, or_
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from databaseLogin import dbLogin

Base = declarative_base()
# generate_password_hash(password) for future use in password

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(8), nullable=False)
    mobile_number = Column(Integer, unique=True, index=True, nullable=False)
    role_id = Column(Integer, ForeignKey('user_role.user_role_id'))
    role = relationship("UserRole")
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, nullable=False)
    last_updated_date = Column(DateTime, nullable=False)

    @classmethod
    def create_user(cls, first_name, last_name, email, password, mobile_number, role_id):
        engine = dbLogin.dbConnection()
        if not engine:
            return "!Error: Fail to connect with DB"

        Session = sessionmaker(bind=engine)

        session = Session()
        # Check if user with same email or mobile number already exists
        existing_user = session.query(cls).filter(or_(cls.email == email, cls.mobile_number == mobile_number)).first()
        if existing_user:
            return None
        # Create new user object
        try:
            user = cls(first_name=first_name, last_name=last_name, email=email, password=password,
                       mobile_number=mobile_number, role_id=role_id, created_date=datetime.now(),
                       last_updated_date=datetime.now())
            session.add(user)
            session.commit()
        except Exception as e:
            print("!ERROR: User not created {}".format(e))
            return "Error"

        session.refresh(user)
        session.close()
        return user
