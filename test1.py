#Тестовое задание 1
import re

car_numbers = ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12"]
valid_letters = "АВЕКМНОРСТУХABEKMHOPCTYX"
#Произведем проверку регулярным выражением
for number in car_numbers:
    if re.match(r"^["+valid_letters+"]{1}[0-9]{3}["+valid_letters+"]{2}[0-9]{2,3}$", number):
        print(number)
