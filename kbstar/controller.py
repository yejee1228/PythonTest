from kbstar.service import Service
class Controller:
    def __init__(self):
        self._service = Service()

    def create_model(self, fname):
        return self._service.new_model(fname)
    """
    class Controller :
    def __init__(self):
        self.model = Model()

    def print_menu(self):
        print('0.종료')
        print('1.액셀데이터보기')
        return input('메뉴입력')

    def run(self):
        while 1:
            menu = self.print_menu()
            if menu=='1':
                self.model.load_data()
            elif menu == '0':
                break
    """
