
class Accounting:
    if (os.path.exists("accounting.xlsx") == False):
      w=Workbook()
      file=w.active
      file.append(['order','quantity','total price','send cost','tax'])
      file.freeze_panes = 'A2'
      w.save('accounting.csv')
    else:
        pass

    def acountant(self,a,b,c):    
          wb=pd.read_csv('accounting.csv')
          wb.loc[len(wb.index)]=[b,a.loc['total','quantity'],a.loc['total','total price'],(25 if c=='post'else 50),
                                  
                    a.loc['total','total price']*0.09]
          ws.append(p)
          wb.save('accounting.csv')
    def out(self):
          df = pd.read_excel("accounting.csv")
          return df 
         
