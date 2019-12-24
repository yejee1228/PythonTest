from titanic.controller import Controller
from titanic.view import View
if __name__ == '__main__':
    def print_menu():
        print('0. 종료')
        print('1. 생존자 시각화')
        print('2. 정확도')
        print('3. 교차검증')
        print('4. 캐글제출')
        return input('메뉴 입력\n')


    while 1:
        menu = print_menu()
        if menu == '1':
            app = Controller()
            train = app.create_model('train.csv')
            # test = app.create_model('test.csv')
            vue = View(train)
            view = input('차트내용 선택\n'
                         '1. 생존자 vs 사망자\n'
                         '2. 생존자 성별 대비')
            if view == '1':
                vue.showPlot()
            elif view == '2':
                vue.plot_sex()
        if menu == '2':
            pass
        if menu == '3':
            pass
        if menu == '4':
            pass
        elif menu == '0':
            break