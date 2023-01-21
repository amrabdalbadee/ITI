def main_menu():
    print("0-import \n")
    print("1-new \n")
    print("2-search \n")
    print("3- delete \n")
    print("4- show all \n")
    print("5- export \n")
    print("6- export department \n")
    print("7- quit \n")
def print_function(i,n,s,d):
    print(f"Employee id is {i} \n")
    print("Employee name is {} \n".format(n))
    print("Employee salary is {} \n".format(s))
    print("Employee department is {} \n".format(d))
def to_str(i,n,s,d):
    #s = f"{i},{n},{s},{d}\n"
    s = f"ID : {i}    Name : {n}  Salary : {s}  Department : {d} \n"
    return s


def insert_function(clean_list,id_list,name_list,sal_list,dep_list):
    id_list.append(clean_list[0])
    name_list.append(clean_list[1])
    sal_list.append(clean_list[2])
    dep_list.append(clean_list[3])

def as_list(x):
    if type(x) is list:
        return x
    else:
        return [x]

#id_list = [1, 2, 3, 4]
#name_list = ["ahmed ali", "Ali ahmed", 'amr ahmed', 'ali mahmoud']
#sal_list = [2000, 3000, 4000, 5000]
#dep_list = ['finance', 'HR','Eng','HR']
id_list = []
name_list = []
sal_list = []
dep_list = []
flag = 1

while (flag == 1):
    main_menu()
    y = int(input("choose process: "))
    match y:
        case 0:
            try:
                with open("/home/mora/Downloads/ITI/python/emps.txt","r") as file:
                   lines = file.readlines()
                   [insert_function(as_list(index) + list(line.strip().split(',')),id_list,name_list,sal_list,dep_list) for index,line in enumerate(lines)]
            except:
                print("read file failed \n")
            finally:
                file.close()
        case 1:

            new_employee = input("please enter name,salary,dep: ")
            clean_ne = new_employee.split(",")
            clean_ne = [i.strip() for i in clean_ne]
            clean_ne.insert(0,len(id_list)+1)
            #if clean_ne[2] == '':
                #clean_ne[2] = 0
            clean_ne[2] = float(clean_ne[2] or 0)
            insert_function(clean_ne,id_list,name_list,sal_list,dep_list)

        case 2:
            name = input("please enter the initials of name: ")
            [print_function(i, n, s, d) for i, n, s, d in zip(id_list, name_list, sal_list, dep_list) if n.lower().startswith(name.strip().lower())]
        case 3:
            name = input("please enter the initials of name: ")
            tobedeleted = [(i,n,s,d) for i, n, s, d in zip(id_list, name_list, sal_list, dep_list) if
             n.lower().startswith(name.strip().lower())]
            for index,(i,n,s,d) in enumerate(tobedeleted):
                #print(tup)
                id_list.remove(i)
                name_list.remove(n)
                sal_list.remove(s)
                dep_list.remove(d)
        case 4:
            [print_function(i,n,s,d)for i,n,s,d in zip(id_list,name_list,sal_list,dep_list)]
        case 5:
            try:
                with open("/home/mora/Downloads/ITI/python/output_emps.txt", "w") as file:
                    tobewrited = [file.write(to_str(i, n, s, d)) for i, n, s, d in zip(id_list, name_list, sal_list, dep_list)]
            except:
                print("write file failed \n")
            finally:
                file.close()
        case 6:
            try:
                with open("/home/mora/Downloads/ITI/python/output_emps_2.txt", "w") as file:
                    writed_dep = []
                    for department in dep_list:
                        if department in writed_dep:
                            continue
                        else:
                            writed_dep.append(department)
                            file.write(department)
                            file.write("\n")
                            [file.write(to_str(i, n, s, d)) for i, n, s, d in zip(id_list, name_list, sal_list, dep_list) if department == d]

            except:
                print("write file failed \n")
            finally:
                file.close()
        case 7:
            print("BYE BYE")
            flag = 0
        case _:
            print("please enter a valid option \n")
