from establish_connection import establish_connection

cursor = establish_connection()

sql = """
CREATE TABLE INFO(
    USER_ID SERIAL PRIMARY KEY,
    FIRST_NAME CHAR(20),
    LAST_NAME CHAR(20),
    TITLE CHAR(10),
    AGE INT,
    NATIONALITY CHAR(20),
    NUM_COURSES INT,
    NUM_SEMESTER INT, 
    REGISTRATION_STATUS CHAR(20)
)
"""
cursor.execute(sql)
print("Table created successfully!")