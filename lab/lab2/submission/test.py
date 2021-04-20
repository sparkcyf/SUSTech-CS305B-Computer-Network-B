import cs205b_lab2

cs205b_lab2.HiPython()

alist = [5,-1,8,-99,7,100,56,-34]
amax,amin = cs205b_lab2.find_max_min(alist)
print("max=%d,min=%d" % (amax,amin))

mycat = cs205b_lab2.cat("Persian cat")
print(mycat.meow())