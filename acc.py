
class Accounting(Order):
    def __init__(self):
        super().__init__()
    if (os.path.exists("accounting.xlsx") == False):
      w=Workbook()
      file=w.active
      file.append(['quantity','order.no','total price','send cost','tax'])
      file.freeze_panes = 'A2'
      w.save('accounting.xlsx')
    else:
        pass

    def hh(self):
        self.order_n0() 
        cart=pd.read_csv('cart_item.csv')
        wb=load_workbook('accounting.xlsx')
        ws = wb.active
        with open('conf.txt')as f:
            lines=f.readlines()
        ws.append(cart['quantity'].iloc[-1] , re.findall('\d+',lines[3]), cart['total price'].iloc[-1])
        wb.save('accounting.xlsx')
        return open("accounting.xlsx","r+").read() 
         
