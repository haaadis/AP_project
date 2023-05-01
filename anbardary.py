



class Inventory:
    #def update_admin_manual(self):
    # if mojodo --> manual 
    
    def stock_manual(self):
        while True:
            in1=input(" bags or shoes").capitalize()
            if in1=='Bags':
                anbardari = pd.read_csv('C:/Users/ASUS/Downloads/Bags.csv')
            else:
                anbardari = pd.read_csv('C:/Users/ASUS/Downloads/Shoes.csv')
            id = int(input('Enter stock ID: '))
            new_stock = int(input('Enter new stock count: '))
            anbardari.loc[anbardari['id'] == id, 'stock'] = new_stock        
            t=input('do you wanna continue')
            if t=='yes':
                continue
            else:
                anbardari.to_csv('my_file.csv',index=False)
                break
    def stock_csv(self):
       while True:
            in1=input(" bags or shoes").capitalize()
            if in1=='Bags':
                anbardari = pd.read_csv('C:/Users/ASUS/Downloads/Bags.csv')
            else:
                anbardari = pd.read_csv('C:/Users/ASUS/Downloads/Shoes.csv')
            file=input()
            file=pd.read_csv(file)
            anbardari.set_index('id', inplace=True)
            anbardari.update(file.set_index('id'))
            anbardari.reset_index()
            t=input('do you wanna continue')
            if t=='yes':
                continue
            else:
                anbardari.to_csv('my_file.csv',index=False)
                break
        
    def add_item(self):
        while True:
                in1=input(" bags or shoes").capitalize()
                if in1=='Bags':
                    anbardari = pd.read_csv('C:/Users/ASUS/Downloads/Bags.csv')
                else:
                    anbardari = pd.read_csv('C:/Users/ASUS/Downloads/Shoes.csv')
                kala_w=input('enter w')
                
                kala_id=input('enter the id you wanna add')
                kala_name=input('enter the name ')
                kala_price=input('enter the unit price')
                kala_color=input('enter color')
                kala_stock=input('enter ths stock')
                
                anbardari.loc[len(anbardari.index)]=[kala_id,kala_name,kala_price,kala_stock,kala_color,kala_w]
                t=input('do you wanna continue')
                if t=='yes':
                    continue
                
                else:
                    anbardari.to_csv('my_file.csv',index=False)
                    break
