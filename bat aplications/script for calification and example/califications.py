import os


def run(folder,percentage):
    name_file=("Results " + folder +" "+percentage+".txt").replace(" ","_")
    f = open(name_file, "w+")
    calification = 0
    last = None
    os.chdir(folder)
    name = None
    date = None
    verification = {}
    count = 0
    confirm = None
    list = []
    for student in os.listdir():
        if student != "Results " + "folder" + ".txt" and student != "califications.py":
            name = student.split("-")[-2]
            date = student.split("-")[-1]
            os.chdir(student)
            last = os.listdir()[-1].replace(" ", "")
            os.rename(last, last.replace(" ", ""))
            print(100 * "#")
            print(student + "|" + last)
            print("")
            if ".py" in last:
                os.system("type " + last)
                print("")
                print(100 * ".")
                os.system("python3 " + last)
            elif ".ipynb" in last:
                os.system("nbterm " + last.replace(" ", ""))
                print("")
                print(100 * ".")
                os.system("ipython " + last.replace(" ", ""))
            os.chdir("..")
            if name not in verification.keys():
                calification = input(
                    "Put the calification for "
                    + name
                    + "(Date of deliverey: "
                    + date
                    + ") = "
                )
                count += 1
                verification[name] = count
                list.append(name + "," + calification)
            else:
                confirm = input(
                    "Do you want rewrite the calification for "
                    + student
                    + "?"
                    + "(put x for No or put any symbol for yes): "
                )
                if confirm != "x":
                    calification = input(
                        "Put the calification for "
                        + name
                        + "(Date of deliverey: "
                        + date
                        + ") = "
                    )
                    list[count - 1] = name + "," + calification
            print(100 * "%")
            print("you qualified to " + str(count) + " students.")
            print(100 * "%")
    for calification in list:
        f.write(calification + "\n")
    print("NOW YOU CAN OPEN "+name_file+" FILE")
    exit = input(
        "Do you want calificate other folder? (put x for No or put any symbol for yes): "
    )
    folder = None
    if exit == "x":
        print("Gracias")
    else:
        folder = input("Put the folder: ")
        run(folder)


def menu():
    folder = input("Put the folder: ")
    percentage=input("Put the porcentaje of the activity(0 to 1, please put 2 numbers after .): ")
    run(folder,percentage)


menu()
