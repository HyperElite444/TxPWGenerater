import numbers
import random, string

def banner():
    print("\033[1;31m |''||''| '||' '|'  '||''|.  '|| '||'  '|'  ..|'''.| ")
    print("\033[1;31m    ||      || |     ||   ||  '|. '|.  .'  .|'     ' ")
    print("\033[1;35m    ||       ||      ||...|'   ||  ||  |   ||    ... ")
    print("\033[1;35m    ||      | ||     ||         ||| |||    '|.    || ")
    print("\033[1;35m   .||.   .|   ||.  .||.         |   |      ''|...'|ʙʏ ᴍʀ.ᴛʜᴇɴᴜx")
    print("")
    print("")

banner()

password_length = int(input("\033[1;32m Password Length    :\033[1;33m  "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""   
for index in range(password_length):
    password = password + random.choice(characters)
print("\033[1;32m Password Generated :\033[1;33m  {}".format(password))
print("")
print("")
