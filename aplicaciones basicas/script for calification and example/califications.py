import os


def run(folder):
    f = open("Results.txt", "w+")
    f.write("Results:"+"\n")
    calification=0
    last=None
    os.chdir(folder)
    name=None
    date=None
    for student in os.listdir():
        if student!="Results.txt" and student!="califications.py":
            name=student.split("-")[-2]
            date=student.split("-")[-1]
            os.chdir(student)
            last=os.listdir()[-1].replace(" ","")
            os.rename(last,last.replace(" ",""))
            print(100*'#')
            print(student+'|'+last)
            print('')
            if '.py' in last:
                os.system("type "+last)
                print('')
                print(100*'.')
                os.system("python3 "+last)
            elif '.ipynb' in last:
                os.system("nbterm "+last.replace(" ",""))
                print('')
                print(100*'.')
                os.system("ipython "+last.replace(" ",""))
            os.chdir('..')
            calification=input('Put the calification for '+name+'(Date of deliverey: '+date+') = ')
            f.write(name+"|"+"Result: "+calification+"\n")
            
def menu():
    folder=input('Put the folder: ')
    run(folder)
    
menu()
    

                
                
        