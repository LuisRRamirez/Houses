import csv
from cs50 import SQL
from sys import argv

if len(argv) != 2:
    print ("usage error")
    exit()

db = SQL("sqlite:///students.db")

# Open CSV file
with open(argv[-1], "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles)

    # Iterate over CSV file
    for row in reader:
        
        fullname = row['name'].split()
        house = row["house"]
        birth = row["birth"]
        
        if len(fullname) == 3:
            
            first, middle, last = fullname
            
        else: 
            first, last = fullname
            middle = None
                
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)


