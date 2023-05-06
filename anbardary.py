import pandas as pd
class Inventory:
    #def update_admin_manual(self):
    # if mojodo --> manual 
    
    def stock_manual(self):
        while True:
            warehouse = input('bags or shoes: ').capitalize() #choose
            df = pd.read_csv(warehouse+'.csv')
            id = int(input('Enter stock ID: '))
            print(df.loc[df['id']==id,'color'].to_string(index=False))   #print colors to choose from     
            color = input('which color?: ')
            new_stock = int(input('Enter new stock count: '))
            df.loc[(df['id'] == id)&(df['color']==color), 'stock'] = new_stock
                   
            t=input('do you wanna continue: ')
            if t=='yes':
                continue
            else:
                df.to_csv(warehouse+'.csv',index=False)
                break
    def stock_csv(self):
       while True:
            warehouse = input('bags or shoes: ').capitalize() #choose
            df = pd.read_csv(warehouse+'.csv')
            file=input(('enter the csv file path: '))
            file=pd.read_csv(file)
            df.set_index(['id','color'], inplace=True)
            df.update(file.set_index(['id','color']))
            df.reset_index()
            t=input('do you wanna continue: ')
            if t=='yes':
                continue
            else:
                df.to_csv(warehouse+'.csv',index=False)
                break
    
        
    def add_item(self):
        while True:
                warehouse = input('bags or shoes: ').capitalize() #choose
                df = pd.read_csv(warehouse+'.csv')
                kala_w=input('enter w')
                kala_id=input('enter the id you wanna add')
                kala_name=input('enter the name ')
                kala_price=input('enter the unit price')
                kala_color=input('enter color')
                kala_stock=input('enter ths stock')
                
                df.loc[len(df.index)]=[kala_id,kala_name,kala_price,kala_stock,kala_color,kala_w]
                t=input('do you wanna continue: ')
                if t=='yes':
                    continue
                
                else:
                    df.to_csv(warehouse+'.csv',index=False)
                    break
    def update(self,warehouse,id,quantity,color):
        wh = pd.read_csv(warehouse+'.csv')
        res = wh.loc[(wh['id'] == id) & (wh['color'] == color), 'stock'].iloc[0]
        wh.loc[(wh['id'] == id) & (wh['color'] == color), 'stock'] = int(res)-quantity
        x=wh['stock'].replace(0, 'unavailable')
        wh.update(x)
        wh.to_csv(warehouse+'.csv',index = False)
        
    def check_inventory(self):
        warehouse = input('bags or shoes: ').capitalize() #choose
        return pd.read_csv(warehouse+'.csv')
        
