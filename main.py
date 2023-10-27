class Robotiaga:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def change_name(self, new_name):
        self.name = new_name

    def change_position(self, new_position):
        self.position = new_position

    def change_salary(self, new_salary):
        self.salary = new_salary

    def display_info(self):
        print(self.name, self.age, self.country)

kitayos = Robotiaga(name="kitayos", age=8, country="Ukraine")
kitayos.change_name("kitayos")
kitayos.display_info()

kitayos.change_position("Engineer")
kitayos.display_info()

kitayos.change_salary(50000)
kitayos.display_info()