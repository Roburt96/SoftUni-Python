from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:

    def __init__(self, *args):
        self.__name = args[0]
        self.__budget = int(args[1])
        self.__animal_capacity = int(args[2])
        self.__workers_capacity = int(args[3])
        self.animals = []
        self.workers = []

    @property
    def name(self):
        return self.__name

    @property
    def budget(self):
        return self.__budget

    def add_animal(self, animal_obj: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal_obj)
            self.__budget -= price
            return f"{animal_obj.name} the {animal_obj.__class__.__name__} added to the zoo"

        if self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker_obj: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker_obj)
            return f"{worker_obj.name} the {worker_obj.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for name in self.workers:
            if name.name == worker_name:
                self.workers.remove(name)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.__budget >= sum(work_salary.salary for work_salary in self.workers):
            self.__budget -= sum(work_salary.salary for work_salary in self.workers)
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        if self.__budget >= sum(animal_care.money_for_care for animal_care in self.animals):
            self.__budget -= sum(animal_care.money_for_care for animal_care in self.animals)
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = {"Lions": [], "Tigers": [], 'Cheetahs': []}
        [result[x.__class__.__name__ + "s"].append(str(x)) for x in self.animals]
        print_result = f"You have {len(self.animals)} animals",\
                       f"----- {len(result['Lions'])} Lions:", *result['Lions'],\
                       f"----- {len(result['Tigers'])} Tigers:", *result['Tigers'],\
                       f"----- {len(result['Cheetahs'])} Cheetahs:", *result['Cheetahs']
        return "\n".join(print_result)

    def workers_status(self):
        result_workers = {"Keepers": [], "Caretakers": [], "Vets": []}
        [result_workers[x.__class__.__name__ + "s"].append(str(x)) for x in self.workers]
        print_result = f"You have {len(self.workers)} workers", \
                       f"----- {len(result_workers['Keepers'])} Keepers:", *result_workers['Keepers'], \
                       f"----- {len(result_workers['Caretakers'])} Caretakers:", *result_workers['Caretakers'], \
                       f"----- {len(result_workers['Vets'])} Vets:", *result_workers['Vets']
        return "\n".join(print_result)





zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())

