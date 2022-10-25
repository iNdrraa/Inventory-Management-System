import pymysql #call library
class connection1:
    
    
    def getconnection(self):
        
        try:
            
            conn=pymysql.connect(host='localhost',user='root',
                                 password='',db='inventory')
            
        except Exception as e:
            print(e)
            
        else:
            print("Connection successfully created")
            return conn
