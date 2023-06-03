from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationships

Base = declarative_base()


class OpinionsModel(Base):
    __tablename__ = "opinions"
    id = Column(INTEGER, primary_key=True)
    from_user_id = Column(ForeignKey("users.id"))
    company_id = Column(INTEGER)
    comment = Column(VARCHAR(200))
    rating = Column(INTEGER)
    status = Column(INTEGER)
    users = relationships("UsersModel", back_populates="users")

    def __str__(self):
        return f"id = {self.id}', from_user_id = '{self.from_user_id}', company_id = '{self.company_id}'," \
               f" comment = '{self.comment}', rating = '{self.rating}', status = '{self.status}"
