import sqlite3

try:
    # create or open a file called animals.db with SQLite3 database engine
    conn = sqlite3.connect('animals.db')
    
    # get a cursor object
    cursor = conn.cursor()
    
    # obtain data in runtime
    # Note: user needs to enter 6 pieces of data separated with space, e.g.
    # horse brown 2018/07/05 200 male 1
    animal_type, colour, dob, weight_kg, gender, purchased = input('enter values for: type, colour, dob, weight_kg, gender, purchased:\n').split()
    runtime_data=(animal_type, colour, dob, weight_kg, gender, purchased)
    
    # note: when primary key of a table is of integer data type,
    # an attempt to insert a record with NULL value for the INTEGER
    # primary key column will result in the next available
    # sequential integer value assigned for that record
    sql = '''INSERT INTO animals
             (id, type, colour, dob, weight_kg, gender, purchased) 
             VALUES(NULL, ?, ?, ?, ?, ?, ?)'''

    # execute the sql statement with the data obtained in runtime
    cursor.execute(sql, runtime_data)
    print("Record successfully inserted into table 'animals'.")
    
    # commit the change
    conn.commit()

    rows = cursor.execute('SELECT * FROM animals')
    for row in rows:
        print(row)
        
# catch any exceptions
except Exception as e:
    # roll back any change if something goes wrong
    conn.rollback()
    print(e)
    
finally:
    # close the db connection
    conn.close()
