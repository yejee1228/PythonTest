from titanic.model import Titanic
import pandas as pd
import numpy as np

"""
['PassengerId' 고객ID,
'Survived', 생존여부
'Pclass', 승선권 1 = 1st 2 = 2nd 3 = 3rd
'Name',
'Sex',
'Age',
'SibSp',동반한 형제, 자매, 배우자
'Parch', 동반한 부모, 자식
'Ticket', 티켓번호
'Fare', 요금
'Cabin', 객실번호
'Embarked'] 승선한 항구명 C = 쉐부로, Q = 퀸즈타운, S = 사우스햄톤
"""

class Service:
    def __init__(self):
        self.m = Titanic()
        self.m.context = './data/'
        print(self.m.context)

    def new_file(self, fname) -> object: return self.m.context + fname

    def new_dframe(self, new_file) -> object:
        return pd.read_csv(new_file)

    def load_data(self) -> []:
        tr = self.new_dframe(self.new_file('train.csv'))
        te = self.new_dframe(self.new_file('test.csv'))
        print('[1]결과 : ' + tr.columns)
        return [tr, te]

    @staticmethod
    def drop_feature(list, feature)->[]:
        tr = list[0]
        te = list[1]
        tr = tr.drop([feature], axis = 1)
        te = te.drop([feature], axis = 1)
        print('[2]결과 : ' + tr.columns)
        return [tr, te]

    @staticmethod
    def embarked_nominal(list)->[]:
        tr = list[0]
        te = list[1]
        tr = tr.fillna({"Embarked": "S"})
        city_mapping = {"S": 1, "C": 2, "Q": 3}
        tr['Embarked'] = tr['Embarked'].map(city_mapping)
        te['Embarked'] = te['Embarked'].map(city_mapping)
        return [tr, te]

    @staticmethod
    def sex_nominal(list) -> []:
        #male = 0, female = 1
        tr = list[0]
        te = list[1]
        combine = [tr, te]
        sex_mapping = {"male":0, "female":1}
        for i in combine :
            i['Sex'] = i['Sex'].map(sex_mapping)
        #tr['Sex'] = tr['Sex'].map(sex_mapping)
        #te['Sex'] = te['Sex'].map(sex_mapping)
        print(tr['Sex'])
        print(te['Sex'])
        return[tr, te]

    @staticmethod  # 지도학습.
    def age_ordinal(list) -> []:
        tr = None
        te = None
        tr['Age'] = tr['Age'].fillna(-0.5)  # 가장 많이 탄 나이대로 하는 경향이 있음. fillna 결측값 대체하기
        te['Age'] = te['Age'].fillna(-0.5)  # 가장 많이 탄 나이대로 하는 경향이 있음. fillna 결측값 대체하기
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult',
                  'Senior']  # 왜 나이를 붙였는가 분석자료를 만드는 것
        # 인공지능에게 나의 정보를 넘겼을때 '죽음'이라는 단답을 리턴하는 것이 아니라, 차트, *데이터 시각화* 하여 그것에 대한 증명을 보여줘야 한다.
        tr['AgeGroup'] = pd.cut(tr['Age'], bins, labels=labels)  # 오디널
        te['AgeGroup'] = pd.cut(te['Age'], bins, labels=labels)  # 오디널
        age_title_mapping = {0: 'Unknown', 1: 'Baby', 2: 'Child', 3: 'Teenager', 4: 'Student', 5: 'Young Adult',
                             6: 'Adult', 7: 'Senior'}
        for x in range(len(tr['AgeGroup'])):  # 코드와 테스트 코드를 두가지 작성하는 것 지도학습의 특징.
            if tr['AgeGroup'][x] == 'Unkwon':
                tr['AgeGroup'][x] = age_title_mapping[tr['Title'][x]]
        for x in range(len(tr['AgeGroup'])):  # 코드와 테스트 코드를 두가지 작성하는 것 지도학습의 특징.
            if te['AgeGroup'][x] == 'Unkwon':
                te['AgeGroup'][x] = age_title_mapping[te['Title'][x]]
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6,
                       'Senior': 7}
        tr['AgeGroup'] = tr['AgeGroup'].map(age_mapping)
        te['AgeGroup'] = te['AgeGroup'].map(age_mapping)
        print(tr['AgeGroup'].head())
        return [tr, te]

    @staticmethod
    def fare_odianl(list) -> []:
        tr = list[0]
        te = list[1]
        return [tr, te]


