from pony.orm import db_session, select

from models import User

class UserRepo:
    def __init__(self):
        self.__model = User

    @db_session
    def get_user_by_id(self, id):
        user = self.__model.get(lambda user: user.id == id)
        return user

    @db_session
    def get_all_by_sql(self):
        users = self.__model.select_by_sql("SELECT * FROM users")
        return users

    @db_session
    def get_all_by_cycle(self):
        users = select(user for user in self.__model).page(1, pagesize=5).to_list()
        return users

    @db_session
    def get_all_by_lambda(self):
        users = User.select(lambda user: user)
        return users.page(1).to_list()

    @db_session
    def add_user(self, id, first_name, last_name, phone, email, status):
        self.__model(id=id, first_name=first_name, last_name=last_name, phone=phone, email=email, status=status)

    @db_session
    def delete_user_by_id(self, id):
        user_to_del = self.get_user_by_id(id)
        user_to_del.delete()

    @db_session
    def delete_user_by_id_range(self, id):
        users_to_del_r = self.__model.select(lambda user: user.id > id)
        for user in users_to_del_r:
            user.delete()

    @db_session
    def update_user_email_by_id(self, id, new_email):
        user = self.get_user_by_id(id)
        user.email = new_email


if __name__ == '__main__':
    user_repo = UserRepo()
    users_sql = user_repo.get_all_by_sql()
    for usr in users_sql:
        print(usr)
    users_cycle = user_repo.get_all_by_cycle()
    print(users_cycle)
    users_lambda = user_repo.get_all_by_lambda()
    print(users_lambda)
    user_repo.add_user(20, "Jolif", "Ftliop", "+380653332211", "sdsd6@as.ssas", 2)
    print(users_lambda)
    user_get_by_id = user_repo.get_user_by_id(20)
    user_del_by_id = user_repo.delete_user_by_id(20)
    user_repo.update_user_email_by_id(9, "sd@sd.newwwww")
    print(user_repo.get_user_by_id(9))



