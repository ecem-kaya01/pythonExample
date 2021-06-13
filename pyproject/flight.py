class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passenger = []

    def passenger_addition(self,name):
        self.name= name

        if len(self.passenger)<self.capacity :
            self.passenger.append(name)
            print(f"{name} added succsesfully ")
        else:
            print(f"{name} can't added. Plane is full.")


people = ["Ecem" , "Brian", "Engin", "Fadime"]
flight = Flight(3)

for person in people:
    flight.passenger_addition(person)
