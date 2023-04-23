

class Accounting(Order):
    if (os.path.exists("accounting.xlsx") == False):
      w=Workbook()
      file=w.active
      file.append(['order.no','quantity'])
      file.freeze_panes = 'A2'
      w.save('accounting.xlsx')
    else:
        pass

    def __init__(self):
        super().__init__()
    def hh(self):    
          wb=load_workbook('accounting.xlsx')
          ws = wb.active
          ws.append([self.order_no,self.cart_item.loc['total']['quantity']])
          wb.save('accounting.xlsx')
          return open("accounting.xlsx","r+").read() 
         
