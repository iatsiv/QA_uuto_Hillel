from alchemy.models.opinions_model import OpinionsModel
from alchemy.session import session

class OpinionsRepository:
    def __init__(self):
        self.__session = session
        self.__model = OpinionsModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def get_by_id(self, opinion_id):
        opinion = self.__session.get(self.__model, {'id': opinion_id})
        return opinion

    def add_item(self, opinion: OpinionsModel):
        self.__session.add(opinion)

    def remove_item_by_id(self, opinion_id):
        opinion = self.__session.get(self.__model, {'id': opinion_id})
        self.__session.delete(opinion)

    def update_item(self, opinion_id, new_data):
        opinion = self.__session.get(self.__model, {'id': opinion_id})
        for key, value in new_data.items():
            setattr(opinion, key, value)


if __name__ == "__main__":
    opinions_repo = OpinionsRepository()
    result_all = opinions_repo.get_all()
    for opinion in result_all:
        print(opinion)

    result_by_id = opinions_repo.get_by_id(1)
    print(result_by_id)
