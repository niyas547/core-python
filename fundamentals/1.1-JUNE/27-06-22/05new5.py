# it will write the sentance in the given file and also it can be replace the sentance in any file

# f=open("new5","w")
# f.write("where r you")

f=open("new4", "w")
f.write("who r you here")
print(f.tell())     #it will tell current position of the file point
print(f.seek(5))