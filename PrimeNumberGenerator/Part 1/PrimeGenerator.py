
import datetime,math
while True:
    strategy=int(input("Choose strategy 1 or 2: "))
    if strategy==1 or strategy==2:
        break
    else:
        print("Selects a valid strategy!")
        continue
start=int(input("Enter start: "))
end=int(input("Enter end: "))
a=datetime.datetime.now()
##If User selects strategy 1,


#If User selects strategy 2, 
def GetPrime1(start,end):
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
    return str(result)

def GetPrime2(start,end):
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
    return str(result)
if strategy==1:  
    print(GetPrime1(start,end))
if strategy==2:
    print(GetPrime2(start,end))

print("Time taken for strategy",strategy,"is",datetime.datetime.now()-a)


