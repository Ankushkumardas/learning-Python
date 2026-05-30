# an event that interrupt sthe basic flow of the program

# try -->  # block of code to be executed
# except --> # if the above block gives an error the except block will be executed
# finally -->  # block that will always execute irrespective of the error

a=3
b=2

try :
    res=a/b
    print(res)
except Exception as e :
    print("error",e)
finally :
    print("end")
