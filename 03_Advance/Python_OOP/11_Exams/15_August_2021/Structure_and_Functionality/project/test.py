from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea
from project.drink.water import Water


bakery = Bakery("MyBakery")
# print(bakery.add_table("OutsideTable", 51, 10)) # ok
# print(bakery.add_table("OutsideTable", 1, 10)) # ok raise error
# print(bakery.add_table("InsideTable", 51, 10)) # ok raise error
bakery.add_table("InsideTable", 1, 10) # ok
# bakery.add_table("InsideTable", 2, 0 ) #ok raise error
bakery.add_food("Bread", "Bread", 1) # ok
# print(bakery.add_food("Bread", "Bread", 0)) #ok raise error
# print(bakery.add_food("Bread", "", 1)) # ok raise error

#print(bakery.add_food('Cake', 'Cake1', 2)) # ok
# print(bakery.add_food('Cake', 'Cake2', 0)) # ok raise error
# bakery.add_food('Cake', '', 2) # ok raise error
 # ok
bakery.order_food(1, "Bread")
print(bakery.leave_table(1))

