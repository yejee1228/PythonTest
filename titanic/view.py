import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

rc('font', family =
   font_manager
   .FontProperties(fname='C:/Users/User/AppData/Local/Microsoft/Windows/Fonts/D2Coding-Ver1.3.2-20180524.ttf')
   .get_name())

class View:
    def __init__(self):
        pass

    @staticmethod
    def showPlot(list):
        tr = list[0]
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        tr['Survived'] \
            .value_counts() \
            .plot.pie(explode=[0, 0.1],
                      autopct='%1.1f%%',
                      ax=ax[0],
                      shadow=True)
        ax[0].set_title('0.사망자 VS 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0.사망자 VS 1.생존자')
        sns.countplot('Survived', data=tr, ax=ax[1])
        plt.show()

    @staticmethod
    def plot_sex(list):
        tr = list[0]
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        tr['Survived'][tr['Sex'] == 'male'] \
            .value_counts() \
            .plot.pie(explode=[0, 0.1],
                      autopct='%1.1f%%',
                      ax=ax[0],
                      shadow=True)
        tr['Survived'][tr['Sex'] == 'female'] \
            .value_counts() \
            .plot.pie(explode=[0, 0.1],
                      autopct='%1.1f%%',
                      ax=ax[1],
                      shadow=True)
        ax[0].set_title('남성 생존비율(0:사망자, 1:생존자)')
        ax[1].set_title('여성 생존비율(0:사망자, 1:생존자)')
        plt.show()