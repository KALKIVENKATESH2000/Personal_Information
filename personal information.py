class people: 
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def display(self):
        print("name:",self.name)
        print("address:",self.address)
        print("age:",self.age)
        print("phone:",self.phone)

obj = people("name","address","age","phone")
obj.display()




