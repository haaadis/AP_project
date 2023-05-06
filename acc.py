
import os
import pandas as pd
from openpyxl import Workbook
class Accounting:
    if (os.path.exists("accounting.csv") == False):    
      file=pd.DataFrame()
      file[['order','quantity','total price','send cost','tax']] = None
      file.to_csv('accounting.csv')
    else:
        pass

    def acountant(self,a,b,c):    
          wb=pd.read_csv("accounting.csv")
          wb.drop(['Unnamed: 0'], axis=1)
          wb._append([b,a.loc['total','quantity'],
                    a.loc['total','total price'],
                    (25 if c=='post' else 50)
                    ,a.loc['total','total price']*0.09])
          wb.to_csv('accounting.csv')
    def out(self):
          df = pd.read_csv("accounting.csv")
          return df 
