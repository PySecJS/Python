import mysql.connector  
      
    #Create the connection object   
connection = mysql.connector.connect(host = "localhost", user = "root",passwd = "", database = "python")  
      
    #printing the connection object   
print(connection)   