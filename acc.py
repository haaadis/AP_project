
import os
import pandas as pd
from openpyxl import Workbook
class Accounting:
    if (os.path.exists("accounting.csv") == False):    
      file=pd.DataFrame(columns =['order','quantity','total price','send cost','tax'])
      file.to_csv('accounting.csv',index=False)
    else:
        pass

    def acountant(self,a,b,c):    
          wb=pd.read_csv("accounting.csv")
          wb=wb._append({'order' :b,'quantity' :a.loc['total','quantity'],

                    'total price' :a.loc['total','total price'],
                    'send cost':(25 if c=='post' else 50)
                    ,'tax':a*0.09},ignore_index=True)
          wb.to_csv('accounting.csv', index=False)

    def out(self):
          df = pd.read_csv("accounting.csv")
          return df 
