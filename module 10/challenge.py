class DigitalSchool:
    def __init__(self,name,city,state,courses):
        self.__name=name
        self.__city=city
        self.__state=state
        self.__courses=courses

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def state(self):
        return self.__state

    @property
    def courses(self):
        return self.__courses

    @name.setter
    def name(self,name):
        self.__name=name

    @city.setter
    def city(self,city):
        self.__city=city

    @state.setter
    def state(self,state):
        self.__state=state

    @courses.setter
    def courses(self,courses):
        self.__courses=courses

show_school_info=DigitalSchool("DigitalSchool","Prishtina","Kosova","Python")
print(show_school_info)


class DS_Prishtina(DigitalSchool):
    def __init__(self,student_number):
        self.__student_number=student_number

