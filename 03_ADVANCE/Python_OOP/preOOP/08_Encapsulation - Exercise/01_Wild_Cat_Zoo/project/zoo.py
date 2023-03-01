from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget  # 3000
        self.__animal_capacity = animal_capacity # 5
        self.__workers_capacity = workers_capacity # 8
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"

        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for i in self.workers:
            if i.name == worker_name:
                self.workers.remove(i)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum(x.salary for x in self.workers)
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_care = sum(x.money_for_care for x in self.animals)
        if self.__budget >= money_care:
            self.__budget -= money_care
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

