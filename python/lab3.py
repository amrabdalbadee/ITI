class Employee:

    all = []

    def __init__(self, id, name, salary, department):
        self.id = int(id)
        self.__name = name
        self.__salary = int(salary or 0)
        self.department = department

        Employee.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        print("inside setter")
        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,val):
        if val < 0:
            print("salary can't be negative")
            self.__salary = 0
        else:
            self.__salary = val

    def __repr__(self):
        return f"Employee(id = {self.id},name = {self.__name}, salary = {self.__salary}, department = {self.department})"    #developer friendly

    @classmethod
    def import_file(cls, path):
        with open(path) as handle:
            handle.readline()
            lines = handle.read().split('\n')
        count = 0
        for line in lines:
            cls(count,*line.split(','))
            count +=1

    @classmethod
    def add_employee(cls):
        new_employee = input("please enter name,salary,dep: ")
        clean_ne = new_employee.split(",")
        clean_ne = [i.strip() for i in clean_ne]
        cls(len(Employee.all),*clean_ne)

    @classmethod
    def filter_by_name(cls,name):
        return list(filter(lambda Employee: Employee.__name.lower().startswith(name.lower()), cls.all))

    @classmethod
    def delete_by_name(cls,name):
        cls.all = list(filter(lambda Employee: not Employee.__name.lower().startswith(name.lower()), cls.all))

    @classmethod
    def export(cls,path):
        with open(path,'w') as file:
            tobewrited = [file.write(f"{e}\n") for e in cls.all]

    @classmethod
    def filter_by_department(cls,department):
        return list(filter(lambda Employee: Employee.department == department, cls.all))

    @classmethod
    def export_department(cls,path):
        with open(path,'w') as file:
            dep = []
            for Employee in cls.all:
                department = Employee.department
                if department in dep:
                    continue
                else:
                    dep.append(department)
                    export_list = Employee.filter_by_department(department)
                    file.write(f"{department}\n")
                    tobewrited = [file.write(f"{e}\n") for e in export_list]





def print_screen():
    print()
    print("0-import")
    print("1-new")
    print("2-search")
    print("3-delete")
    print("4-show all")
    print("5-export")
    print("6-export department")
    print("7-quit")
    print()




while True:

    print_screen()

    choice = input("Enter your: ")

    match choice:
        case '0':
            Employee.import_file("/home/mora/Downloads/ITI/python/emps.txt")

        case '1':
            Employee.add_employee()
        case '2':
            name = input('Enter name: ')

            filtered = Employee.filter_by_name(name)

            for emp in filtered:
                print(emp)

        case '3':

            name = input('Enter name: ')

            Employee.delete_by_name(name)

        case '4':

            for emp in Employee.all:
                print(emp)

        case '5':
            Employee.export('emp_out.txt')

        case '6':
            Employee.export_department('dept_out.txt')

        case '7':
            break

        case _:
            print("Wrong Choice")
