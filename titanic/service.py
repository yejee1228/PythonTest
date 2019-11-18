from titanic.model import Titanic
import pandas as pd

class Service:
    def __init__(self):
        self.m = Titanic()
        self.m.context = './data/'
        print(self.m.context)


    def new_file(self, fname) -> object: return self.m.context + fname


    def new_dframe(self, new_file) -> object:
        return pd.read_csv(new_file)


    def load_data(self):
        tr = self.new_dframe(self.new_file('train.csv'))
        print('----- train 객체 -----')
        print(tr.columns)
        te = self.new_dframe(self.new_file('test.csv'))

        """
        ['PassengerId', 'Survived',  'pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Tictet', 'Fare',
        'Cabin', 'Embarked']

        ['PassengerId', 고객ID,
         'Survived', 생존여부,
         'pclass', 승선권 1= 1st, 2 = 2nd, 3=3rd
        'Name', 이름,
        'Sex',
        'Age',
        'SibSp',동반한 형제, 자매, 배우자
        'Parch', 동반한 부모, 자식
        'Tictet', 티켓번호
        'Fare', 요금
        'Cabin', 객실번호
        'Embarked' 승선한 항구명 c= 쉐부로, Q= 퀸즈타운, s = 사우스햄톤]
        """
