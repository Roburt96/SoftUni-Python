cat_price= "4" #цена храна за котки
dog_price= "2.5" #цена храна за кучета

print("Pet shop!")
print("Price for 1 cat food " + cat_price +",")
print("Price for 1 dog food " +dog_price + ".")

num2 = float(input("How many dog food do u want: "))
num1 = float(input("How many cat food do u want: "))


print("Total price is:")

result=(float(cat_price)*num1)+(float(dog_price)*num2)
print(float(result))