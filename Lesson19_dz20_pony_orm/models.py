from pony.orm import Database, PrimaryKey, Optional, Required, Set

db = Database()
db.bind(provider='postgres', user='postgres', password='1234', host='127.0.0.1', database='hillel')

class User(db.Entity):
    _table_ = "users"
    id = PrimaryKey(int, auto=True)
    first_name = Required(str, 50)
    last_name = Required(str, 50)
    email = Required(str, 50)
    phone = Required(str, 13)
    status = Required(int)
    opinions = Set("Opinion")

    def __str__(self):
        return f"id={self.id}; first_name={self.first_name}; last_name={self.last_name}; " \
               f"email={self.email}; phone={self.phone}; status={self.status}"

    def __repr__(self):
        return f"id={self.id}; first_name={self.first_name}; last_name={self.last_name}; " \
               f"email={self.email}; phone={self.phone}; status={self.status}"


class Opinion(db.Entity):
    _table_ = "opinions"
    id = PrimaryKey(int, auto=True)
    company_id = Required(int)
    comment = Required(str, 200)
    rating = Required(int)
    status = Required(int)
    user = Required(User, column="from_user_id")

    def __str__(self):
        return f"id={self.id}; company_id={self.company_id}; comment={self.comment}; " \
               f"rating={self.rating}; status={self.status}"

    def __repr__(self):
        return f"id={self.id}; company_id={self.company_id}; comment={self.comment}; " \
               f"rating={self.rating}; status={self.status}"


db.generate_mapping(create_tables=False)
