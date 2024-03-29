'''
f=open("test.txt" ,'w') # 'w','a', 'r'
f.write("#This is the first line\n")
f.write("*This is the second line")

f.close
'''

with open ("test.txt", 'a') as f:
    f.write("first line\n")
    f.write("second line\n")
f.close

print(dir(f))