from P4 import P4, P4Exception
p4 = P4()
import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime) #used for debugging to see how long it takes
p4.port = "serverAddress" #this is hwere you put your server address of the depot you are trying to scyc 
p4.user = "userName" #the user name of the logged in uuser for perforce
p4.client = "workspace" #this is the workspace of where you want every to sync too


p4.exception_level = 1 #it is 2 by default which means raise all.
p4.connect()
p4.run("sync", "@label") #replace "label" with whatever the label you are thing to sync, Keep the @
localtime = time.asctime( time.localtime(time.time()) )
