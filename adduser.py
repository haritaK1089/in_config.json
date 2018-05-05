#####################################################
##Modulename: adduser.py
##Descrition: Adds an user by taking inputs from useradd_input.json file
##Version: 1.0
##Prerequisites: python version 3.6 and useradd_input.json file in the same folder as the execution script
##Author: Harita Kolluru 
####################################################
import json
import subprocess
import sys
import re
def addnewuser(user,command,options,op_val,arguments):
    result=subprocess.Popen([user, command, options, op_val, arguments], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = result.communicate()
    retc = result.returncode
    print(retc,out,err)
    return retc

jsonfile =  sys.argv[1]
print(jsonfile)
pattern = re.compile("[a-z][a-z0-9]*.json")
if(pattern.search(jsonfile)):
    json_data=json.loads(open(jsonfile).read())
    print(type(json_data["user1"]["op_val"]))
    user = json_data["user1"]["user"]
    print(user)
    command = json_data["user1"]["command"]
    options = json_data["user1"]["options"]
    op_val = str(json_data["user1"]["op_val"])
    arguments = json_data["user1"]["arguments"]
    addnewuser(user,command,options,op_val,arguments)
else:
    print("Please provide a valid json file having a filename and  extension .json")

