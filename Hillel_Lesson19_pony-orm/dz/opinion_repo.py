from pony.orm import db_session, select, left_join
from models import Opinion

class OpinionRepo:
    def __init__(self):
        self.__model = Opinion

    @db_session
    def get_all_by_sql(self):
        opinions = self.__model.select_by_sql("SELECT * FROM opinions")
        return opinions

    @db_session
    def get_all_by_cycle(self):
        opinions = select(opinion for opinion in self.__model).page(1, pagesize=3).to_list()
        return opinions

    @db_session
    def get_all_by_lambda(self):
        opinions = Opinion.select(lambda opinion: opinion)
        return opinions.page(1).to_list()

    @db_session
    def get_opinions_with_positive_rating(self, rating):
        opinions = Opinion.select(lambda opinion: opinion.rating > rating)
        return opinions.page(1).to_list()

    @db_session
    def left_join(self):
        result = left_join((opinion, user) for opinion in Opinion for user in opinion.user)
        for res in result:
            opinion = res[0]
            user = res[1]
            print(f"{opinion.comment} <----- {user.first_name}")




if __name__ == '__main__':
    opinion_repo = OpinionRepo()
    opinions_lambda = opinion_repo.get_all_by_lambda()
    print(opinions_lambda)
    print(opinion_repo.get_opinions_with_positive_rating(3))
    opinion_repo.left_join()

