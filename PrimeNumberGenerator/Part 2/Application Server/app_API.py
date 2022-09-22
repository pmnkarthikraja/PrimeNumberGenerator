import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import math
import datetime
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root', password='root!@#123', database='primedetails',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()

app=Flask(__name__)
api=Api(app)

def GetPrime1(start,end):
    a=datetime.datetime.now()
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
    b=datetime.datetime.now()-a  
    return y,size,str(b)

def GetPrime2(start,end):
    a=datetime.datetime.now()
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
    #print("Number of prime numbers present: ",size)
    out1=list(map(str,out))
    result=','.join(out1) 
    b=datetime.datetime.now()-a   
    return out,size,str(b)

class Home(Resource):
    def get(self,strategy,start,end):
        userrange=str(start)+"-"+str(end)
        now=datetime.datetime.now()
        stringtime = now.strftime("%d/%m/%Y %H:%M:%S:%f")
        if strategy==1:
            out=GetPrime1(start,end)
            result={"Primes are":out}
            # out1=jsonify(out[0])
            total={"Total number of primes present":out[1]}
            strategychosen={"Strategy chosen":strategy}
            timeelapsed={"Time Elapsed":out[2]}
            timeelapse_db=str(out[2])
            strategy_db=str(strategy)
            totalprime_db=str(out[1])
            mycursor.execute("insert into user_primedetails (CurrentTimestamp, UserRange,TimeElapsed, Algorithm_Chosen, No_of_primes_returned) values ('%s','%s','%s','%s','%s');"%(stringtime,userrange,timeelapse_db,strategy_db,totalprime_db))
            mydb.commit()
            res=jsonify(result,total,strategychosen,timeelapsed)
            return res
        if strategy==2:
            out=GetPrime2(start,end)
            result={"Primes are":out}
            total={"Total number of primes present: ":out[1]}
            strategychosen={"Strategy chosen":strategy}
            timeelapsed={}
            timeelapsed['Time Elapsed']=out[2]
            timeelapse_db=str(out[2])
            strategy_db=str(strategy)
            totalprime_db=str(out[1])
            mycursor.execute("insert into user_primedetails (CurrentTimestamp, UserRange,TimeElapsed, Algorithm_Chosen, No_of_primes_returned) values ('%s','%s','%s','%s','%s');"%(stringtime,userrange,timeelapse_db,strategy_db,totalprime_db))
            mydb.commit()
            res=jsonify(result,total,strategychosen,timeelapsed)
            return res

api.add_resource(Home,'/home/Strategy=<int:strategy>/<int:start>/<int:end>')
if __name__=="__main__":
    app.run(debug=True)