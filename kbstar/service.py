import pandas as pd
import xlwings as xw
from kbstar.model import Model

class Service:
    def __init__(self):
        self._model = Model()

    def new_model(self, param):
        model = self._model
        model.context = './data'
        model.fname = param
        print(model.fname)
        wb = xw.Book(model.context + '/' + model.fname)
        sheet = wb.sheets['매매종합']
        row_num = sheet.range(1, 1).end('down').end('down').row
        data_range = 'A2:GE' + str(row_num)
        raw_data = sheet[data_range] \
            .options(pd.DataFrame, index=False, header=True).value
        return raw_data

"""
import pandas as pd
import xlwings as xw

class Model:
    def __init__(self):
        self.path='.\data\kbstar.xls'

    def load_data(self):
        # xlwings 모듈로 엑셀 읽기
        wb = xw.Book('.\data\kbstar.xls')
        # sheet 선택
        sheet = wb.sheets['매매종합']
        # 시트 행의 개수 계산
        row_num = sheet.range(1, 1).end('down').end('down').end('down').row
        # 읽어올 데이터 범위 설정(엑셀 열+행)
        data_range = 'A2:GE' + str(row_num)
        # options 함수로 pandas 데이터프레임에 쓰기
        raw_data = sheet[data_range]\
            .options(pd.DataFrame, index=False, header=True).value
        print(raw_data)

"""