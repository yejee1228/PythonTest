from titanic.service import Service
from titanic.view import View

class Controller:
    def __init__(self):
        self.service = Service()
        self._list = []

    @property
    def list(self) -> object: return self._list

    @list.setter
    def list(self, list): self._list = list


    def create_model(self, fname) -> object:
        service = self._service
        dframe = service.new_model(fname)
        dframe = self.drop_feature(dframe, 'Cabin')
        dframe = self.drop_feature(dframe,'Ticket')
        dframe = self.embark_norminal(dframe)
        dframe = self.title_norminal(dframe)
        dframe = self.drop_feature(dframe, 'Name')
        return dframe
