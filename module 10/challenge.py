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

#defining methods

    def show_school_info(self):
        return {
            "name":self.__name,
            "city":self.__city,
            "state":self.__state,
            "courses":self.__courses
        }



    def organize_hackathon(self):
        print("Organizing a generic hackathon.")

#define a subclass called Ds Prishtina where it has a private attr called student number and 2 methods
class DS_Prishtina(DigitalSchool):
    def __init__(self,name,city,state,courses,student_number):
        super().__init__(name,city,state,courses)
        self.__student_number=student_number

    def SCF(self):
        print("First edition")

    def organize_hackathon(self):
        print("Were doing a data analysis hackathon")

#Implementing

prishtina_obj=DS_Prishtina("Ds-Prishtina","Prishtina","Kosova",["python",'html','css','java'],300)
prishtina_obj.organize_hackathon()

#define the subclass dsferizaj inhereting from digitalschool

class DS_Ferizaj(DigitalSchool):
    def __init__(self,name,city,state,courses,student_number):
        super().__init__(name,city,state,courses)
        self.__student_number=student_number

    def organize_hackathon(self):
        print("Organizing the first dsFerizaj hackathon")

    def internship(self):
        print("We are looking for applicants for a DigitalSchool Internship")

ferizaj=DS_Ferizaj("ds-ferizaj",'ferizaj','Kosova',['html','css','javascrip'],244)
print(ferizaj.internship())
print(ferizaj.organize_hackathon())
print(ferizaj.show_school_info())