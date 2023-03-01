from project.customer import Customer
from project.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers = list()
        self.dvds = list()

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        cur_customer = [customer for customer in self.customers if customer_id == customer.id][0]
        cur_dvd = [x for x in self.dvds if x.id == dvd_id][0]

        if cur_dvd in cur_customer.rented_dvds:
            return f"{cur_customer.name} has already rented {cur_dvd.name}"

        if cur_dvd.is_rented:
            return "DVD is already rented"

        if cur_customer.age < cur_dvd.age_restriction:
            return f"{cur_customer.name} should be at least {cur_dvd.age_restriction} to rent this movie"

        cur_customer.rented_dvds.append(cur_dvd)
        cur_dvd.is_rented = True
        return f"{cur_customer.name} has successfully rented {cur_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        cur_customer = [customer for customer in self.customers if customer_id == customer.id][0]
        cur_dvd = [x for x in self.dvds if x.id == dvd_id][0]

        if cur_dvd in cur_customer.rented_dvds:
            cur_customer.rented_dvds.remove(cur_dvd)
            cur_dvd.is_rented = False
            return f"{cur_customer.name} has successfully returned {cur_dvd.name}"

        return f"{cur_customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for x in self.customers:
            result += f"{str(x)}\n"
        for x in self.dvds:
            result += f"{str(x)}\n"
        return result



c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)





