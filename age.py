#!/usr/bin/python3

from sys import argv
import datetime

agefile = "./age.txt"

if len(argv) == 5 and argv[1] == "set":
    y = argv[2]
    m = argv[3]
    d = argv[4]
    with open(agefile,"w") as f:
        f.write(y)
        f.write(m)
        f.write(d)

elif len(argv) > 1:
    print("bad syntax fuck off")

else:
    try:
        with open(agefile,"r") as f:
            s = f.readline()
    except FileNotFoundError:
        print("not-ok")
    y = s[0:4]
    m = s[4:6]
    d = s[6:8]
    date = datetime.datetime.strptime(f"{y} {m} {d}", '%Y %m %d').date()
    date = date + datetime.timedelta(days=365*18)
    if datetime.datetime.today().date() < date:
        print("not-ok")
    else:
        print("ok")