import psycopg2
from datetime import datetime
from src.config.queries import INSERT_USER, SELECT_PASSWORD, LIST_USER, UPDATE_USER, DELETE_USER
from src.config.credentials import db_config

try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
except Exception as error:
    print(f"Error connecting to PostgreSQL: {error}")
    exit()


class User_Manager:

    def login(self, email, password):
        try:
            query = f"SELECT password FROM users WHERE email='{email}'"
            cursor.execute(query)
            row = cursor.fetchone()
            if row is None:
                return 3
            else:
                saved_password = row[0]
                if saved_password == password:
                    return 1
                else:
                    return 2
                
        except Exception as error:
            return f"Error : {error}"
    
        

    def add_user(self, email, password, first_name, last_name, phone_number, role):
        try:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            values = (email, password, first_name, last_name, phone_number, role, now, now)
            cursor.execute(INSERT_USER, values)
            conn.commit()
            return 1
        except Exception as error:
            return  f"Error : {error}"
             

    def list_user(self):
        try:
            cursor.execute(LIST_USER)
            row= cursor.fetchall()
            return 1, row 
        except Exception as e:
            return 2 , str(e)

    def edit_user(self, email, password, new_role, new_first_name, new_last_name):
        try:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            values = (password, new_role, new_first_name, new_last_name, now, email)
            cursor.execute(UPDATE_USER, values)
            conn.commit()
            return 1 
        except Exception as e:
            return 2 
        

    def delete_user(self, email):
        try:
            cursor.execute(DELETE_USER,(email,))
            conn.commit()
            return 1
        except Exception as error:
            return f"Error: {error}"


    
   
        
    
