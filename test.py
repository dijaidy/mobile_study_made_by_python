def var_scope():
    global s # global variable
    print(s)
    s = "Python is easy" # local variable
    print(s)



s = "Python is not easy"


var_scope()

print(s)