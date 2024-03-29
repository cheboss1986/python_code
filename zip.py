zip = input("enter your zip code")
z_1 = len(zip.strip())
z_2 = zip.isdigit()

if z_1 == 5 and z_2 == True:
    print("your entry is valid")
else:
    print("please enter a valid zip")
