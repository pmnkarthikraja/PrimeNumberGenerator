# PrimeNumberGenerator
PrimeNumberGenerator giving a range of prime numbers 
Welcome to our PrimeNumberGenerator !

There is two part in this project present in two directories

Part 1 directory contains two files PrimeGenerator.py and test_PrimeGenerator.py. PrimeGenerator.py contains two algorithm, giving all prime numbers between user given range.
The difference between two algorithm is time_complexity. Algorithm 1 created with floor division method and Algorithm 2 created without floor division.

Requirements and dependencies for part 1:
    ---> Python 3.10.4
    ---> Visual Studio Code - IDE
    ---> Command Prompt
    
    MODULES used in PrimeGenerator.py
    ---> Datetime and math
    MODULES used in test_PrimeGenerator.py
    ---> unittest
    
Instructions to run part 1:
    -> place two python files in the same directory
    -> open command prompt -> Navigate to the parent directory -> Enter "py test_PrimeGenerator.py"
    -> It will successfully run and giving primenumbers as string format. For example) If user choose strategy 1 and give 1 and 10 range. It will give, "2,3,5,7" , "Number of prime numbers present: 4" and "Time taken for strategy 1 is 0.00:0023.
    
    
Part 2 directory contains two folders, "Web Server" and "Application Server"

Part 2 -> WEB SERVER - To display all prime numbers based on user given range in a Web Page. User can give input as range over HTTP method include GET and POST requests.
  Requirements and dependencies for part 2: WEB SERVER
      ---> Python 3.10.4
      ---> Flask 2.1.1
      ---> mysql.connecotr
      ---> HTML5 and CSS3
      ---> Javascript
      ---> MySQL Database (RDBMS) -8.0 command line client
      
   MODULES used in WEB SERVER -> app.py (main python file)
   
      ---> urllib - request module
      ---> Flask - render_template, jsonify, request
      ---> mysql.connector
    
   MySQL configuration via python:
      ---> mysql.connector
           ----> host: "localhost"
           ----> user: "root"
           ----> password: "root!@#123"
           ----> database: "primedetails"
           ----> auth_plugin: "mysql_native_password"
   
   How to install dependencies?
   
   --> open command prompt -> Enter pip install (package name). If you have already pip for python3.
   
   PATH CONFIGURATION - WEB SERVER
   
   Master folder: Assignment --> part 2 --> Web server
                                                --------> _pycache Dir
                                                --------> static Dir
                                                --------> templates Dir
                                                          --------> home.html
                                                          --------> result.html
                                                --------> app.py (main python file)
   Instructions to run part 2 - WEB SERVER:
        -> open command prompt -> Navigate to web server folder
        -> Enter "py app.py"
        -> It will run on a localhost server http://127.0.0.1:5000/
        -> Open browser -> Enter above URL
        -> You are now live in server and user can send request and get response through web page
        -> For example, Select Strategy: 1, Start Number: 1, End number: 10 and Enter "submit buttton". It will give all prime numbers between user range of 1-10, Number of prime numbers present, Which statergy user chosen and Time for execution
        
     
  Part 2 -> APPLICATION SERVER - To display all prime numbers based on user given range through API calling. User can send request as values in resource and get response in JSON format.
  
    Requirements and dependencies for part 2: APPLICATION SERVER
        ---> Python 3.10.4
        ---> Flask 2.1.1
        ---> mysql.connector (RDBMS)
        ---> Flask_restful 0.3.9
       
    MODULES used in APPLICATION SERVER -> app.py (main python file)
    
        ---> Flask - request, jsonify
        ---> Flask_restful - Resource, Api
        ---> datetime and math module
        ---> mysql.connector
     
     MySQL configuration via python:
        ---> mysql.connector
             ----> host: "localhost"
             ----> user: "root"
             ----> password: "root!@#123"
             ----> database: "primedetails"
             ----> auth_plugin: "mysql_native_password"
   
   
    PATH CONFIGURATION - WEB SERVER
   
    Master folder: Assignment --> part 2 --> Application Server
                                                --------> app_API.py (main python file)
                                                
   
    Instructions to run part 2 - APPLICATION SERVER:
        -> open command prompt -> Navigate to Application Server folder
        -> Enter "py app.py"
        -> It will run on a localhost server http://127.0.0.1:5000/
        -> Open browser -> Enter above URL
        -> You are now live in server and user can send request as values in resource and get response as JSON format.
        -> In resource, Type "http://127.0.0.1:5000/home/Strategy="select_strategy"/"startnumber"/"endnumber"
        -> For example, http://127.0.0.1:5000/home/Strategy=1/1/100
        -> It will JSON format data like [{primes are: 2,3,5,7},{Time_Elapsed: 00.00.00.0023},{Total number of primes present: 4},{Strategy chosen: 1}]
        -> All data's include , CurrentTimestamp, UserRange, TimeElapsed, Algorithm_Chosen and No_of_primes_returned are saved in MySQL database.(primedetails database).
        
   
   
   
   
   
   
   
   
