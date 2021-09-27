import mysql.connector
import time

mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="Rental_Site")
mycursor = mydb.cursor()
class Reg_user:
    def newuser(self):
        username = input("Enter your name :")
        password = input("Enter your password :")
        mail = input("Enter your mail :")
        phone = int(input("Enter your Phone number :"))
        Aadhar = int(input("Enter your Aadhar :"))
        
        mycursor.execute(
            "insert into user(userid,username,password,email,Mobile,Aadhar) values(NULL,%s,%s,%s,%s,%s)",
            (username, password, mail, phone,Aadhar))
        mydb.commit()
        print("Registration success !!")
class validuser:
    def __init__(self,username,password,destination):
        self.username=username
        self.password=password
        self.destination=destination
    
    def validate_login(self):
        if(self.destination=='user'):
            mycursor.execute("select * from user where username like %s", (self.username,))
            data = mycursor.fetchall()
        elif(self.destination=='approver'):
            mycursor.execute("select * from approver where approvername like %s", (self.username,))
            data = mycursor.fetchall()
        elif(self.destination=='admin'):
            mycursor.execute("select * from admin where adminname like %s", (self.username,))
            data = mycursor.fetchall()
        
        
        if data:
            name = data[0][1]
            passw = data[0][2]
            if name == self.username and passw == self.password:
                return (data[0][0])
        return 0
        
        
class userview:
    def __init__(self,username,idval):
        self.username=username
        self.idval=idval
    def user(self):
        print('Welcome !! '+self.username)
        mycursor.execute("select msg from reqstatus where tenantid==%s ",(idval))
        notifi = mycursor.fetchone()
        if notifi:
            print("new msgs from approver is")
            print(notifi)
        loopval=True
        while(loopval==True):
            print("1.make owner req ,'+\n+'2.Make tenant req")
            role=int(input("choose your option"))
            if(role==1):
                print('owner req page')
                loopval=False
            elif (role==2):
                print('tenant req page')
                loopval=False        
            else:
                loopval=True
        


class approver_view:
    def __init__(self,username,idval):
        self.username=username
        self.idval=idval
    def approver(self):
        print('APPROVER USER')
        print('Welcome '+self.username)
        loopval=True
        while(loopval==True):

            print("1.check how many req coming ,'+\n+'2.process the req")
            role=int(input("choose the options"))
            if(role==1):
                print('count of req coming here')
                loopval=False
            elif (role==2):
                print('process the req as accept/decline')
                loopval=False        
            else:
                loopval=True

class admin:
    def __init__(self,username,idval):
        self.username=username
        self.idval=idval
    def adminview(self):
        print('ADMIN USER')
        print('Welcome '+self.username)
        loopval=True
        while(loopval==True):

            print("1.show user details ,'+\n+'2.show owner requests'+\n+'3. show tenant requests'+\n+'4.create offers'+\n+'5.create advertisements ")
            role=int(input("choose the options"))
            if(role==1):
                print('user details')
                loopval=False
            elif (role==2):
                print('owner requests')
                loopval=False    
                
            elif (role==3):
                print('tenant req')
                loopval=False
            elif (role==4):
                print('offers related')
                loopval=False
            elif (role==5):
                print('advertisements posted')
                loopval=False    
            else:
                loopval=True

if __name__ == '__main__':
    whileval=True
    while(whileval==True):
        print("welcome to Rental housing portal !!")
        destination = input("Are you a user or newuser or approver or admin or ?" + '\n' + " Type your destination :")
        destination = destination.lower()

        if destination == "user":
            username = input("Enter your name :")
            password = input("Enter your password :")
            obj=validuser(username,password,destination)
            idval=obj.validate_login()
            if idval!=0 :
                
                obj1=userview(username,idval)
                obj1.user()
                whileval=False
            else:
                print("User does not exist")
                whileval=True
        elif destination == "newuser":
            obj=Reg_user()
            obj.newuser()
            whileval=False
        elif destination == "approver":
            
            username = input("Enter your approver name :")
            password = input("Enter your approver password :")
            obj=validuser(username,password,destination)
            idval=obj.validate_login()
            if idval!=0 :
                obj=approver_view(username,idval)
                obj.approver()
                whileval=False
            else:
                print("Approver does not exist")
                whileval=True
            
        elif destination == "admin":
            
            username = input("Enter your approver name :")
            password = input("Enter your approver password :")
            obj=validuser(username,password,destination)
            idval=obj.validate_login()
            if idval!=0 :
                obj=admin(username,idval)
                obj.adminview()
                whileval=False
            else:
                print("Admin does not exist")
                whileval=True

        else:
            print("choose the correct option")
            whileval=True