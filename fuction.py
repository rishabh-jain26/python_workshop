# local variable
'''def myfunction():
    x=10
    y=20
    z=x+y
    print(z)
myfunction()
'''
# global variable
'''a=20 # global 
def myfunction():
    print(a)
myfunction()'''

# non-local variable
x=10
def myfunction():
    global x
    x=20 #non-local
myfunction()
print(x)
