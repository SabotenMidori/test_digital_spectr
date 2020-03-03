#Тестовое задание 1
import re

car_numbers = ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12",
               "M1A0CC123", "y421pХ59", "Ф123ыф124", "!a432-yc-21", "H231JK721",
               "О999РМ00", "О123АА1","","К123ЕЕ12а"]
valid_numbers = []
digits = "0123456789"
#Номер может быть записан как кириллицей, так и латиницей
valid_letters = "АВЕКМНОРСТУХABEKMHOPCTYX"
#Насчет регистра букв в википедии ничего не сказано, так что будем учитывать оба, на всякий случай
valid_letters = valid_letters+valid_letters.lower()
#Произведем проверку регулярным выражением
for number in car_numbers:
    if re.match(r"^["+valid_letters+"]{1}[0-9]{3}["+valid_letters+"]{2}[0-9]{2,3}$", number):
        valid_numbers.append(number)

#Выведем отсеянный массив
print("Результат отсеивания регулярным выражением:")
for number in valid_numbers:
    print(number)
valid_numbers = []

#Теперь будем проверять долгим и сложным условием
for number in car_numbers:
    try:
        if valid_letters.find(number[0]) >= 0 and digits.find(number[1]) >= 0 and digits.find(number[2]) >= 0 and digits.find(number[3]) >= 0 and valid_letters.find(number[4]) >= 0 and valid_letters.find(number[5]) >= 0:
            try:
                last_digits = number[6:len(number)]
                i = int(last_digits)
            #Если поймали ошибку преобразования в число, значит, с концовкой номера не все хорошо
            except:
                continue
            if 2 <= len(last_digits) <= 3:
                valid_numbers.append(number)
    #сюда упадет, если мы попробуем посмотреть в элемент строки, которого нет, т.е. строка слишком короткая
    except:
        continue

#Выведем отсеянный массив
print("Результат отсеивания условием:")
for number in valid_numbers:
    print(number)
