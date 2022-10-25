import connection as c 
class product:
    def gets(self):
        self._productname=input("Enter Product Name:")
        self._rate=int(input("Enter Rate:"))
        self._vendername=input("Entere vender name:")
        self._category=input("Category:")
    def __show__(self):
        print("Product Name:",self._productname)
        print("Rate:",self_rate)
        print("Vender name:",self_vendername)
        print("Category:",self_category)
class item:
    def gets(self):
        self._itemcode=int(input("Enter Item Code:"))
        self._barcode=int(input("Enter Barcode:"))
        self._brandname=input("Enter Brand Name:")
        self._type=input("Type of item:")
    def __show__(self):
        print("Item Code:",self_itemcode)
        print("Barcode:",self_barcode)
        print("Brand Name:",self_brandname)
        print("Type:",self_type)
class bill:
    def gets(self):
        self._name=input("Enter coustomer name:")
        self._address=input("Enter Coustomer Address:")
        self._mobileno=input("Enter mobile No:")
        self._date=input("Enter today date:")
    def __show__(self):
        print("Enter coustomer name:",self._name)
        print("Enter Coustomer Address:",self._address)
        print("Enter Mobile No:",self._mobileno)
        print("Enter Today Date:",self._date)
class final(product,item,bill):
    def compute(self):
        product.gets(self)
        item.gets(self)
        bill.gets(self)
    def insertion(self):
        c1=c.connection1()
        conn=c1.getconnection()
        
        #catre cursor
        cur=conn.cursor()
        query="insert into product values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(self._productname,self._rate,self._vendername,self._category,self._itemcode,self._barcode,self._brandname,self._type,self._name,self._address,self._mobileno,self._date)
        try:
            cur.execute(query,val)
        except Exception as e1:
            print("query error")
        else:
            conn.commit()
            print("record save Successfully") 
            conn.close()
    def search(self):
        c1=c.connection1()
        conn=c1.getconnection()
        #catre cursor
        cur=conn.cursor()
        r=int(input("Enter item code:"))
        query="select * from product where itemcode=%s"
        cur.execute(query,r)
        ans=cur.fetchall()
        if ans:
            print(ans)
        else:
            print("Item code  not exist")
        conn.close()
    def delete(self):
        c1=c.connection1()
        conn=c1.getconnection()
        cur=conn.cursor()
        r=int(input("Enter item code:"))
        query="delete from product where itemcode=%s"
        cur.execute(query,r)
        conn.commit()
        conn.close()
        
        

#main program
f=final()

while True:
    print("1-Ins ert record:")
    print("2-Search record:")
    print("3-delete record:")
    ch=int(input("Enter Your choice:"))
    if ch==1:
        f.compute()
        f.insertion()
    if ch==2:
        f.search()
    if ch==3:
        f.delete()
    chh=input("Again Enter data-Yes or No?:").strip().lower()
    if  chh=="yes":
        print("continue")
    else:
        break
    
        
