import os
import subprocess
while True:
    directory="."
    dirs=[]
    c=1
    for i in os.listdir(directory):
        print(f"{c}.{i}")
        dirs.append(i)
        c=c+1
    print(f"{c}.Go-Back")
    choice=int(input("Which directory you want to go in:"))
    if choice==0:
        print("Exiting Program Bye")
        break
    elif choice==c:
        os.chdir('..')
    elif 1<=choice<=c:
        if os.path.isdir(dirs[choice-1]):
            os.chdir(dirs[choice-1])
        elif os.path.isfile(dirs[choice-1]):
            if os.name=='nt':
                os.startfile(dirs[choice-1])
            elif os.name=='posix':
                subprocess.run(['xdg-open',f"{dirs[choice-1]}"])




