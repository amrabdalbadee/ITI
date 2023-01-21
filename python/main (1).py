
class Student:

    all = []

    # @classmethod
    # def create_from_year(cls,name,birthyear,grade):
    #     age = 2023 - birthyear
    #     obj =  cls(name,age,10)
    #     obj.grade = grade
    #     return obj


    @classmethod
    def import_Data(cls,path):
        with open(path) as handle:
            handle.readline()
            lines = handle.read().split('\n')

        for line in lines:
            cls(*line.split(','))

    @classmethod
    def filter_by_name(cls,name):
        return list(filter(lambda student: student.__name.lower().startswith(name.lower()), cls.all))

    @classmethod
    def delete_by_name(cls, name):
        cls.all = list(filter(lambda student: not student.__name.lower().startswith(name.lower()), cls.all))

    @classmethod
    def delete_by_age(cls, age):
        cls.all = list(filter(lambda student: not student.age == age, cls.all))

    @classmethod
    def filter_by_age(cls, age):
        return list(filter(lambda student: student.age == age, cls.all))


    def __init__(self, name, age, height):
        self.__name = name
        self._age = int(age)
        self.height = int(height)

        Student.all.append(self)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,val):
        if val < 0:
            print("age can't be negative")
            self._age = 0
        else:
            self._age = val

    def __get_attendence(self):
        print("attendance is taken")

    def attend(self):
        self.__get_attendence()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        print("inside setter")
        self.__name = value


    def __repr__(self):
        return f"Student(name = {self.__name}, age = {self.age}, height = {self.height})"    #developer friendly


    def __len__(self):
        return self.height

    def __mul__(self, other):
        self.age = self.age * other
        return self.age

    def __add__(self, other):
        self.height = self.height + other
        return self.height

    def __gt__(self, other):
        if type(other) == type(self):
            return self.age > other.age
        else:
            return False





class CollegeStudent(Student,):

    all = []
    def __init__(self,name,age,height,university):
        super().__init__(name,age,height)
        self.university = university
        CollegeStudent.all.append(self)

    def __repr__(self):
        return f"CollegeStudent(name = {self.name}, age = {self.age}, height = {self.height}, University = {self.university})"    #developer friendly


# Student.import_Data('stds_in.txt')

s = Student('A', 27,170)

cs = CollegeStudent("M",23,170,'Alex')

print(s)



