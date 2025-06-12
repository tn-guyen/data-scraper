import sqlite3

from Objects.course_code import *
from Objects.course import *
from Objects.coordinator import *
from Objects.degree import *
from Objects.degree_plan import *

class DBWriter:
    def writeCourseCode(self, array: dict[str, CourseCode]):
        try:
            connection = sqlite3.connect('your_database.db') # setup database connection
            cursor = connection.cursor() # object to execute sql queries
            
            # iterature thru keys (no values)
            for item in array:
                # array {key : value}
                array.get(item) # gets values based of key(item)

                cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (item, array.get(item))) 
                print(item) 

            cursor.execute("SELECT * FROM your_table") # execute sql
            results = cursor.fetchall() # get results
            connection.commit() # saves changes in database (if needed)
            
            connection.close() # close connection (important!)
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        finally:
            if (connection):
                connection.close()
                print("The SQLite connection is closed")