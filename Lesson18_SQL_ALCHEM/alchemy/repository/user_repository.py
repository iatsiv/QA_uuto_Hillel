from alchemy.models.users_model import UsersModel
from alchemy.session import session

class UsersRepository:
    def __init__(self):
        self.__session = session
        self.__model = UsersModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_user_by_id(self, user_id):
        user = self.__session.get(self.__model, {'id': user_id})
        return user

    def add_user(self, user: UsersModel):
        self.__session.add(user)

    def remove_user_by_id(self, user_id):
        user = self.__session.get(self.__model, {'id': user_id})
        self.__session.delete(user)

    def update_user(self, user_id, new_data):
        user = self.__session.get(self.__model, {'id': user_id})
        for key, value in new_data.items():
            setattr(user, key, value)

if __name__ == "__main__":
    opinions_repo = UsersRepository()
    result = opinions_repo.get_all()
    for user in result:
        print(user)
