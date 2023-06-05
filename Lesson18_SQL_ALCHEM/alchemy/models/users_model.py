from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.orm import declarative_base, relationships

Base = declarative_base()


class UsersModel(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True)
    first_name = Column(VARCHAR(50))
    last_name = Column(VARCHAR(50))
    email = Column(VARCHAR(50))
    phone = Column(VARCHAR(13))
    status = Column(INTEGER)
    opinions = relationships("UsersModel", back_populates="opinions")

    def __str__(self):
        return f"id = {self.id}', first_name = '{self.first_name}', last_name = '{self.last_name}'," \
               f" email = '{self.email}', phone = '{self.phone}', status = '{self.status}"
