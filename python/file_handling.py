# to read or write over a file we need to first open that 
from requests.sessions import default_headers
# a=open('sales_register.csv','r')
# print(a.read())
# print(a.readline())
# in list view in readlines 
# print(a.readlines())
# //best practose to close a file ater all teh oprations relaetd to itis finished 
# a.close()

# file-name=open("file_location","mode")
# modes can be ->
# 'r'--> read is by default_headers
# 'w'--> write -it will erase old one and create new file and if not file is there and will craete a new file and write there 
# 'a'--> append -it will add or append to the end of the file if file is not there it will create a new file and append there
a=open("sales_register.csv","a")
a.write("\n this i steh test write ")
# print(a.read())
a.close()