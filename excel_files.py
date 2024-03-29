import csv

with open("week23.csv", 'w') as f: # 'w','r', 'a'
    pen = csv.writer(f)
    header = ["Name", "Cell Phone", "city"]
    pen.writerow(header)
    pen.writerow(["Nicholas","444 3859 0306","Savannah"])
f.close

