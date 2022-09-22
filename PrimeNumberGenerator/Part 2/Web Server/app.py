from contextlib import redirect_stderr
from urllib import request
from datetime import datetime
import math
from flask import Flask,render_template,jsonify,url_for,redirect,request
import urllib.request
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root', password='root!@#123', database='primedetails',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
#mycursor.execute("drop table karthik")
# mycursor.execute("select * from user_primedetails;")
# for i in mycursor.fetchall():
#     print(i[4])

#mycursor.execute("insert into user_primedetails (CurrentTimestamp, UserRange, TimeElapsed, Algorithm_Chosen, No_of_primes_returned) values (1.23,'1-100',0.002,1,25);")
######--------------------------Prime number generation code --------------------------########


# while True:
#     strategy=int(input("Choose strategy 1 or 2: "))
#     if strategy==1 or strategy==2:
#         break
#     else:
#         print("Selects a valid strategy!")
#         continue
# start=int(input("Enter start: "))
# end=int(input("Enter end: "))

##If User selects strategy 1,
def GetPrime2(start,end):
    a=datetime.now()
    res=''
    out=[]
    count=0
    if start==1:start=2
    for i in range(start,end+1):
        for j in range(1,i):
            if i%1==0 and i==j:
                if i%j==0:res=True  
            if i!=j and j!=1 and i%j==0:res=False
        if res!=False: 
            count+=1 
            out.append(i)     
        res='' 
    size=len(out)
    print("Number of prime numbers present: ",size)
    out1=list(map(str,out))
    result=','.join(out1)    
    time_elapsed=datetime.now()-a
    return str(result),len(out),time_elapsed

#If User selects strategy 2, 
def GetPrime1   (start,end):
    a=datetime.now()
    if start==1:start=2
    res=None
    y=[]
    for i in range(start,end+1):
        if i <= 1:
            res=False
        maxfactor = math.floor(math.sqrt(i))
        for j in range(2, maxfactor+1):
            if i % j == 0:
                res=False
        if res is None:
            y.append(i)
        res=None
    size=len(y)
    print("Number of prime numbers present: ",size)
    out1=list(map(str,y))
    result=','.join(out1) 
    time_elapsed=datetime.now()-a   
    return str(result),len(y),time_elapsed

# if strategy==1:  
#     print(GetPrime1(start,end))
# if strategy==2:
#     print(GetPrime2(start,end))

#print("Time taken for strategy",strategy,"is",datetime.datetime.now()-a)


########--------------------------CODE END ------------------------------------########################

app=Flask(__name__)



@app.route("/", methods=['POST','GET'])
def home():
    return render_template("home.html")


@app.route("/result", methods=['POST','GET'])
def result():
    now=datetime.now()
    stringtime = now.strftime("%d/%m/%Y %H:%M:%S:%f")
    if request.method=='POST':
        startnumb=request.form.get("startnum")
        endnumb=request.form.get("endnum")
        strategy=request.form.get("strategy")
        if int(strategy)==1:
            result=GetPrime1(int(startnumb),int(endnumb))
            lenprime,totalprime=result[1],result[1]
            time_elapsed=result[2]
            if int(lenprime)>170:
                lenprime=170
            userrange=str(startnumb)+"-"+str(endnumb)
            mycursor.execute("insert into user_primedetails (CurrentTimestamp, UserRange, TimeElapsed, Algorithm_Chosen, No_of_primes_returned) values ('%s','%s','%s','%s','%s');"%(stringtime,userrange,time_elapsed,strategy,totalprime))
            mydb.commit()
            return render_template("result.html",result=result[0],lenprime=lenprime,time_elapsed=time_elapsed,totalprime=totalprime,strategy=strategy,timestamp=stringtime)
            
        if int(strategy)==2:
            result=GetPrime2(int(startnumb),int(endnumb))
            lenprime,totalprime=result[1],result[1]
            time_elapsed=result[2]
            if int(lenprime)>170:
                lenprime=170
            userrange=str(startnumb)+"-"+str(endnumb)
            mycursor.execute("insert into user_primedetails (CurrentTimestamp, UserRange, TimeElapsed, Algorithm_Chosen, No_of_primes_returned) values ('%s','%s','%s','%s','%s');"%(stringtime,userrange,time_elapsed,strategy,totalprime))
            mydb.commit()
            return render_template("result.html",result=result[0],lenprime=lenprime,time_elapsed=time_elapsed,totalprime=totalprime,strategy=strategy,timestamp=stringtime)
        return render_template("result.html")

 

if __name__=="__main__":
    app.run(debug=True)
