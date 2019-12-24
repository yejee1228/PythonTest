from titanic.model import Titanic
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#구글에서 제공하는 인공지능.
#sklearn : 가르치는 라이브러리. 사이킷런.
#model: 머신. 머신을 러닝(learning)하는 것.
from sklearn.tree import DecisionTreeClassifier
#디시전트리. 결정트리. 스무고개. 선형회귀.
from sklearn.ensemble import RandomForestClassifier
#앙상블에 있는 랜덤포레스트. 분류시에는 Classifier, 예측할 때에는 Regressor
from sklearn.naive_bayes import GaussianNB
#나이브베이즈 분류기
from sklearn.svm import SVC
#서포트 백터 머신
from sklearn import metrics
#사이킷런: cook book. 필요할 때 하나씩 찾아보는 것.
from sklearn.model_selection import KFold
#구글에서 만든 비교군을 두어 교차검증을 한다.
from sklearn.model_selection import cross_val_score
#교차검증할 때 점수 뽑아내는 것

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
        self._model = Titanic()

    def new_model(self, fname):
        model = self._model
        model.context('./data')
        model.fname('/'+fname +'.csv')
        return pd.read_csv(model.fname())

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
        sex_mapping = {"male": 0, "female": 1}
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

    @staticmethod
    def create_model_dummy(train):
        model = train.drop('Survived',axis = 1)# 정답을 없애버린다. 문제를 내기 위함.
        dummy = train['Survived'] #답을 모르는 상태로 답을 리턴하는 것.
        return[model, dummy] #모델과 답

    def hook(self):
        list = self.load_data()
        list = self.drop_feature(list, 'Cabin')
        list = self.drop_feature(list, 'Ticket')
        list = self.embarked_nominal(list)
        list = self.sex_nominal(list)
        return list[0]

    def create_random_variable(self) -> str:  #변수: 여기서는 피쳐(feature)
        train = self.hook()
        tr, te = train_test_split(train, test_size= 0.3, random_state= 0)
        #test_size : 30%.
        #random, 1: 이전에 냈던 문제를 안냄. 0: 이전에 냈던 문제를 다시 냄.
        target_col = ['Pclass', 'Sex', 'Embarked']
        train_X = tr[target_col]
        train_Y = tr['Survived'] #정답 Y = f(X)
        test_X = te[target_col]
        test_Y = te['Survived']

        features_one = train_X.values
        #그중에 하나만 뽑는다. 하나씩만 넣어서 체크하는 것이 아니라 한번에 대량 데이터를 넣는다.
        target = train_Y.values

        tree_model = DecisionTreeClassifier()
        #tree_model = DecisionTreeRegressor
        #생성자처리. new가 생략됨. 이 알고리즘을 모델이라고 한다.
        #우리가 지금 알고리즘을 만들고 잇음. => 타이타닉 모델이 되는 것.
        #얼마만큼의 정확도를 가지고 있는지가 돈이 되는 것.
        #Classfier = 분류
        #Regressor = 하나의 값으로 바꿈
        tree_model.fit(features_one, target) #최적화
        dt_prediction = tree_model.predict(test_X) #예측
        accuracy = metrics.accuracy_score(dt_prediction, test_Y)#정확도. 정답률.
        print('트리모델의 정확도: {}'.format(accuracy))
        return accuracy

    @staticmethod
    def create_kfold() -> object:
        return KFold(n_splits=10, #10조각으로 사용한다.
                     shuffle=True, #셔플
                     random_state=0) #한번 사용한건 사용하지 않는다.

    def accuracy_by_dtree(self)->str: #accuracy 나오면 결과값은 스트링!
        train = self.hook()
        print('결정트리 방식으로 검증')
        print(train)
        arr = self.create_model_dummy(train)
        model = arr[0]
        dummy = arr[1]
        clf = DecisionTreeClassifier()#얘를 검증해본다.
        kfold = self.create_kfold()
        score = cross_val_score(clf, model, dummy, cv=kfold, n_jobs=1, scoring='accuracy')\
        #cv: 프로퍼티 값. 내가 만든 KFold는 10조각으로 자른 것.
        #n_jobs=1 ->몇번 검증하나? 10조각을 1번 검증.
        #어큐러시의 정확도를 검증하는 것.
        return round(np.mean(score) *100, 2)#평균값 숫자이지만 리턴하면서 스트링값으로 출력.

    def accuracy_by_rforest(self):
        print('랜덤포레스트 방식으로 검증')
        train = self.hook()
        arr = self.create_model_dummy(train)
        model = arr[0]
        dummy = arr[1]
        clf = RandomForestClassifier(n_estimators=13)
        # 숫자-측정기 갯수 estimators가 디시전트리 하나짜리. dtree 13개짜리 숲.
        kfold = self.create_kfold()
        scoring = 'accuracy'
        #점수
        score = cross_val_score(clf, model, dummy, cv=kfold, n_jobs=1, scoring=scoring)
        accuracy = round(np.mean(score)*100, 2) #퍼센트 측정, 소수점 2자리까지.
        return accuracy

    def accuracy_by_nb(self):
        print('나이브베이즈 방식으로 검증')
        train = self.hook()
        arr = self.create_model_dummy(train)
        model = arr[0]
        dummy = arr[1]
        clf = GaussianNB()
        # 숫자-측정기 갯수 estimators가 디시전트리 하나짜리. dtree 13개짜리 숲.
        kfold = self.create_kfold()
        scoring = 'accuracy'
        # 점수
        score = cross_val_score(clf, model, dummy, cv=kfold, n_jobs=1, scoring=scoring)
        accuracy = round(np.mean(score) * 100, 2)  # 퍼센트 측정, 소수점 2자리까지.
        return accuracy

    def accuracy_by_svm(self):
        print('서포트벡터 방식으로 검증')
        train = self.hook()
        arr = self.create_model_dummy(train)
        model = arr[0]
        dummy = arr[1]
        clf = SVC()
        # 숫자-측정기 갯수 estimators가 디시전트리 하나짜리. dtree 13개짜리 숲.
        kfold = self.create_kfold()
        scoring = 'accuracy'
        # 점수
        score = cross_val_score(clf, model, dummy, cv=kfold, n_jobs=1, scoring=scoring)
        accuracy = round(np.mean(score) * 100, 2)  # 퍼센트 측정, 소수점 2자리까지.
        return accuracy