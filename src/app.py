import mysql.connector
from requests import RequestException



#BMI Calculator 

#Update User Info
def update_user_info(data):
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="BMI_Calculator",
            user="root",
            password="password"
        )
        print("Connected to MySQL successfully!")

        cursor = connection.cursor()
        
        try:
            query="INSERT INTO users (nric, username, age,weight,height) VALUES (%(nric)s, %(username)s, %(age)s, %(weight)s,%(height)s)"
            executequery=cursor.execute(query,data)
            
            # Commit the changes to the database
            connection.commit()

            # Close the cursor and the connection
            cursor.close()
            connection.close()
            print("Database has been updated")
        
            return executequery
            
        except RequestException as e:
            print("Error sending request:", e)
            
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None
        

#Get user data   
def getUserDataBmi(data):
    try:
        # Replace the placeholders with your actual database connection details
        connection = mysql.connector.connect(
            host="localhost",
            database="BMI_Calculator",
            user="root",
            password="password"
        )
        print("Connected to MySQL successfully!")

        cursor = connection.cursor()

        # Example: SELECT query
        query = "SELECT * from users where nric= %(nric)s;"
        cursor.execute(query,data)

        # Fetch and process the query results
        user_dict = {}  # The dictionary to store the data

        for (nric, username, age,weight,height,created_at) in cursor.fetchall():
            # Append each employee data to the dictionary
            user_dict= {
                "nric":nric,
                'username': username,
                'age':age,
                'weight':weight,
                'height': height,
            }
        print((user_dict))

        # Close the cursor and the connection
        cursor.close()
        connection.close()
        print("Connection closed.")

        return user_dict
    

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None
    

#Calculate BMI form user data 
def calculateBMI(userdict):
    
    #get user data from dic 
    weight_kg=userdict["weight"]
    height_m=userdict["height"]
    nric=userdict["nric"]
    
    bmi = weight_kg / ((height_m/100) ** 2)  
    bmiCategory=""
    if bmi < 18.5:
        bmiCategory="underweight"
    elif 18.5<= bmi <24.9:
        bmiCategory='Normal'
    elif 25 <= bmi < 29.9:
        bmiCategory='Overweight'
    elif bmi > 29.9:
        bmiCategory='Obese'
        
    userBmi={
        "nric":nric,
        "height":height_m,
        "weight":weight_kg,
        "BMI":bmi,
        "BMI Category":bmiCategory
    }
    
    return userBmi

# user_info=getUserDataBmi()
# bmi=calculateBMI(user_info)
# print(bmi)

#insert data into DB
def inserBmiData(data):
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="BMI_Calculator",
            user="root",
            password="password"
        )
        print("Connected to MySQL successfully!")

        cursor = connection.cursor()
        
        try:
            query="INSERT INTO bmi (nric, bmiValue) VALUES (%(nric)s, %(BMI)s)"
            executequery=cursor.execute(query,data)
            
            # Commit the changes to the database
            connection.commit()

            # Close the cursor and the connection
            cursor.close()
            connection.close()
            print("Database has been updated")
        
            return executequery
            
        except RequestException as e:
            print("Error sending request:", e)
            
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None
    
# updatedb=inserBmiData(bmi)
# print(updatedb)

#get existing user data 

def getDataBmiTable(data):
    try:
        # Replace the placeholders with your actual database connection details
        connection = mysql.connector.connect(
            host="localhost",
            database="BMI_Calculator",
            user="root",
            password="password"
        )
        print("Connected to MySQL successfully!")

        cursor = connection.cursor()

        # Example: SELECT query
        query = "SELECT * from bmi where nric= %(nric)s;"
        cursor.execute(query,data)

        # Fetch and process the query results
        user_dict = {}  # The dictionary to store the data

        for (bmiValue, nric) in cursor.fetchall():
            # Append each employee data to the dictionary
            user_dict= {
                "nric":nric,
                "BMI":bmiValue
            }
        print((user_dict))

        # Close the cursor and the connection
        cursor.close()
        connection.close()
        print("Connection closed.")

        return user_dict
    

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None