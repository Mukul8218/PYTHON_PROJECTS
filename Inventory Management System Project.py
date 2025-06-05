                                                       ##### INVENTORY MANAGEMENT SYSTEM PROJECT #####

# REQUIRED LIBRARIES
import mysql.connector

# A Mysql Connection And Cursor
conn= mysql.connector.connect(
host= "127.0.0.1",
user= "root",
password= "mukulsql",
database= "store"
    )
cur= conn.cursor()

# A Method to add a product
def addProduct():
    pname=input("\n\t Enter Product Name: ")
    price=input("\tEnter Product Price: ")
    sql="insert into product(pname,price) value(%s,%s)"
    data=(pname,price)
    cur.execute(sql,data)
    conn.commit()
    if cur.rowcount > 0:
        print("\n\tProduct Added Successfully!")
    else:
        print("\n\tProduct Addition Failed!")
    input("\n\tPress Enter To Continue...")

# A Method to add a customer
def addCustomer():
    cname=input("\n\t Enter Customer Name: ")
    cadd=input("\tEnter Customer Address: ")
    sql="insert into customer(cname,cadd) value(%s,%s)"
    data=(cname,cadd)
    cur.execute(sql,data)
    conn.commit()
    if cur.rowcount > 0:
        print("\n\tCustomer Added Successfully!")
    else:
        print("\n\tCustomer Addition Failed!")
    input("\n\tPress Enter To Continue...")

# Check Existance of a customer by ID
def checkCustomer(cid):
    sql= "select * from customer where cid="+cid
    cur.execute(sql)
    return cur.fetchall()

# Check Existance of a Product by ID
def checkProduct(pid):
    sql= "select * from product where pid="+pid
    cur.execute(sql)
    return cur.fetchall()
    
# A Method to place order
def placeAnOrder():
    cid =input("\n\tEnter Customer ID: ")
    data = checkCustomer(cid)
    if len(data)!=0:
        print("\n\tCustomer Name: ",data[0][1])
        print("\tCustomer Address: ",data[0][2])
        pid = input("\n\tEnter Product ID: ")
        pdata = checkProduct(pid)
        if len(pdata)!=0:
            print("\n\tProduct Name: ",pdata[0][1])
            print("\tProduct Price: ",pdata[0][2])
            qyt= input("\n\tEnter Product You Want To Buy: ")
            sql = "insert into orders(cid,pid,qyt) value(%s,%s,%s)"
            data=(cid,pid,qyt)
            cur.execute(sql,data)
            conn.commit()
            if cur.rowcount > 0:
                print("\n\tOrder Placed Successfully!")
            else:
                print("\n\tFailed To Order Placed!")
        else:
            print("\n\tProduct is Not Available on this ID!")
    else:
        print("\n\tCustomer is not available on this ID")
    input("\n\tPress Enter To Continue...")
    
# A Method To View All Orders
def viewAllOrders():
    sql="""SELECT cname,cadd,pname,price,qyt from customer c
               join orders o
              on c.cid=o.cid
              join product p
             on o.pid=p.pid;"""
    cur.execute(sql)
    data= cur.fetchall()
    for order in data:
        print("\n\t"+order[0]+"\t"+order[1]+"\t"+order[2]+"\t"+str(order[3])+"\t"+str(order[4]))
    input("\n\tPress Enter To Continue...")
    
# A Method To View An Order
def viewOrder():
    cid= input("\n\tEnter Customer ID: ")
    data = checkCustomer(cid)
    if len(data)!=0:
        sql="""SELECT cname,cadd,pname,price,qyt,price*qyt from customer c
                   join orders o
                   on c.cid=o.cid
                   join product p
                   on o.pid=p.pid where c.cid="""+cid
        cur.execute(sql)
        order= cur.fetchall()
        for data in order:
            print("\n\tCustomer Name: ",data[0])
            print("\tCustomer Add: ",data[1])
            print("\tProduct Name: ",data[2])
            print("\tProduct Price: ",data[3])
            print("\tProduct Quantity: ",data[4])
            print("\t-------------------------------------------")
            print("\tTotal Amount: ",data[5])
            print("\t------------------------------------------")
    else:
        print("\n\tCustomer ID is invalid!")
    input("\n\tPress Enter To Continue...")
# A Method to delete a product
def deleteProduct():
    pid= input("\n\tEnter Product ID: ")
    sql="delete from product where pid="+pid
    cur.execute(sql)
    conn.commit()
    if cur.rowcount>0:
        print("\n\tProduct Removed Successfully!")
    else:
        print("\n\tProduct is not available on this ID!")
    input("\n\tPress Enter To Continue...")    

# Dashboard
while True:
    print("\n\t*****INVENTORY MANAGEMENT SYSTEM PROJECT*****")
    print ("\n\t1. Add Product")
    print("\t2. Add Customer")
    print("\t3. Delete Product")
    print("\t4. Place An Order")
    print("\t5. View All Orders")
    print("\t6. View An Orders By Customer ID")
    print("\t7. Exit")
    ch=int(input("\n\tEnter Your Choice: "))
    if ch==7:
        print("\n\t Thank You! For Using Our Software!")
        break
    elif ch==1:
        addProduct()
    elif ch==2:
        addCustomer()
    elif ch==3:
        deleteProduct()
    elif ch==4:
        placeAnOrder()
    elif ch==5:
        viewAllOrders()
    elif ch==6:
        viewOrder()
    else:
        input("\n\tWrong Entered !\n\Try Again By Pressing Enter Button!")

















    

