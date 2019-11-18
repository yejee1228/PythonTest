from titanic.service import Service

class Controller:
    def __init__(self):
        self.service = Service()

    @staticmethod
    def print_menu():
        print('0.종료')
        print('1.데이터 로드')
        return input('메뉴선택')

    def run(self):
        while 1:
            menu = self.print_menu()
            if menu =='1':
                self.service.load_data()
            elif menu == '0':
                break;



