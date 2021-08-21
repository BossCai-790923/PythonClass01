class buildings():
    def __init__(self,name_building,location):
        self.name_building= name_building
        self.location=location
    def say_location_name_building(self):
        print(f"Hello students! This is {self.name_building}! It is located at {self.location}!")

building1= buildings('Eiffel Tower','Paris')
building2=buildings('Big Ben','London')


class dogs():
    def __init__(self, type, age):
        self.type=type
        self.age=age
    def state_type_age_dog(self):
        print(f"This is a {self.type}. It is {self.age} years old.")

dog1=dogs("golden retriever", 1)
dog2=dogs("corgi",2)


class computers():
    def __init__(self, whose_compu, brand):
        self.whose_compu=whose_compu
        self.brand=brand
    def say_whose_brand_compu(self):
        print(f"This is {self.whose_compu}'s computer. It is {self.brand} computer")

compu1=computers("Alice","Apple")
compu2=computers("Ben","Windows")


if __name__=="__main__":

    building1.say_location_name_building()
    building2.say_location_name_building()

    dog1.state_type_age_dog()
    dog2.state_type_age_dog()

    compu1.say_whose_brand_compu()
    compu2.say_whose_brand_compu()