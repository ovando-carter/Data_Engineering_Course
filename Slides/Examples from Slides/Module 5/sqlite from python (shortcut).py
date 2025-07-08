import sqlite3
conn = sqlite3.connect('animals.db')

try:
    # create or open a file called animals.db with SQLite3 database engine
    conn = sqlite3.connect('animals.db')
    
    # remove the table animals if it exists
    conn.execute('DROP TABLE IF EXISTS animals')

    # create the table animals
    conn.execute('''CREATE TABLE  
                    animals (id INTEGER PRIMARY KEY,
                             type TEXT NOT NULL,
                             colour TEXT NOT NULL,
                             dob TEXT,
                             weight_kg REAL NOT NULL, 
                             gender TEXT NOT NULL,
                             purchased INTEGER NOT NULL)''')
    print("Table 'animals' created.")
    
    # insert some records into the table
    conn.execute('''INSERT INTO animals
                    (id, type, colour, dob, weight_kg, gender, purchased) 
                    VALUES
                    (1, 'dog', 'grey', '2010/05/15', 3.5, 'male', 1),
                    (2, 'cat', 'black', NULL, 0.5, 'female', 1),
                    (3, 'cat', 'black & white', '2021/10/20', 0.5, 'female', 0),
                    (4, 'rabit', 'white', NULL, 0.75, 'male', 1), 
                    (5, 'rabit', 'grey', NULL, 1.1, 'female', 1),
                    (6, 'horse', 'brown', '2018/07/05', 200, 'male', 1)''')
    print("6 records successfully inserted into table 'animals'.")
    
    # modify a record from the table
    conn.execute('UPDATE animals SET weight_kg = 190 WHERE id = 6')
    print("1 record successfully updated in the table 'animals'.")
    
    # display all records from the table
    rows = conn.execute('SELECT * FROM animals')
    count = 0
    for row in rows:
        print(row)
        count += 1
    print('The number of returned records:', count)

    # remove a record from the table
    conn.execute("DELETE FROM animals WHERE id = 6")
    print("1 record successfully deleted from table 'animals'.")

    # conn all records from the table
    rows = conn.execute('SELECT * FROM animals')
    count = 0
    for row in rows:
        print(row)
        count += 1
    print('The number of returned records:', count)

    # remove all record from the table
    conn.execute('DELETE FROM animals')
    print("All records successfully deleted from 'animals' table.")
    rows = conn.execute('SELECT * FROM animals')
    count = 0
    for row in rows:
        print(row)
        count += 1
    print('The number of returned records:', count)
    # remove the table
    conn.execute('DROP TABLE animals')
    print("Table 'animals' removed.")

    # commit the change
    conn.commit()
    
except Exception as e:
    conn.rollback()
    print(e)
finally:
    conn.close()