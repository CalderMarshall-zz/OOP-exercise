#defines person as a class
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        #prints all info for a person
    def print_contact_info(self):
        print  "%s's email: %s" "%s's phone number: %s" %(self.name,self.email, self.name, self.phone)
Sonny = Person("Sonny","sonny@hotmail.com","483-485-4948'")
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
Sonny.greet(Jordan)
Jordan.greet(Sonny)
Sonny.print_contact_info()
#prints Sonny's information
print "%s's phone is : %s, %s's email is %s" % (Sonny.name, Sonny.phone, Sonny.name, Sonny.email)
#Prints Jordan's information
print "%s's phone is : %s, %s's email is %s" % (Jordan.name, Jordan.phone, Jordan.name, Jordan.email)

class Vehicle(object):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    # car = Vehicle("Porshe", "918", "2016")
    def print_info(self):
        print "Make: %s, Model: %s, Year: %s" % (self.make, self.model, self.year)
my_car = Vehicle("Porshe", "918", "2016")
my_car.print_info()
