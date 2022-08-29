f=open("new3", "r")
# a=f.read().rstrip("@")            #right strip --it willl print right side
# b=f.read().lstrip("@")            #left strip ---it will print left side
print(b)
# print(a)
f.close()
print(f.name)      #file attached name
print(f.mode)      #file mode read or write
print(f.closed)    #file closing f.close()