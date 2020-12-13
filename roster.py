import cs50
from sys import argv

if len(argv) != 2:
    print ("usage error")
    exit()

db = cs50.SQL("sqlite:///students.db")
rows = db.execute('SELECT * FROM students WHERE house = ? ORDER BY last, first' , argv[-1])

for row in rows: 
    
    if row["middle"] == None:
        
        print( row["first"] + " " + row["last"] + ", born " + str(row["birth"]), sep =' ')
         
    else:
        print( row["first"] + " " + row["middle"] + " " + row["last"] + ", born " + str(row["birth"]), sep =' ')