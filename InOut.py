#summ for 3 numbers
# n1 = int(input("Введите число: "))
# n2 = int(input("Введите число: "))
# n3 = int(input("Введите число: "))
#
# print(n1+n2+n3)

#Area for rightangle triangle
#
# t = int(input("Введите основание треугольника: "))
# h = int(input("Введите высоту треугольника: "))
# s = t*h/2
# print("Площадь равна ", s)

#Printing user's name with !
#
# name = input("Ведите ваше имя: ")
# s = "Привет, {}!".format(name)
# print(s)

#Printing next and before numbers
#
# num1 = int(input("Введите число: "))
# num2 = num1 - 1
# num3 = num1 + 1
# print("Следующее число", num3)
# print("Предыдущее число", num2)

#Printing apples from students
# students = int(input("Введите количество студентов "))
# apples = int(input("Введите количество яблок "))
#
# a_by_s = apples//students
# a_by_basket = apples%students
# print("Яблок у студентова ", a_by_s)
# print("Яблок в корзине ", a_by_basket)

#Printing of numbers hours and minutes after midnight
# sec = int(input("Введите количество секунд: "))
#
# hours = sec // 3600
# minutes = sec // 60
#
# print(hours, minutes)

#Printing of difference first label from second
h1 = int(input("Введите часы первой метки: "))
m1 = int(input("Введите минуты первой метки: "))
s1 = int(input("Введите секунды первой метки: "))

h2 = int(input("Введите часы второй метки: "))
m2 = int(input("Введите минуты второй метки: "))
s2 = int(input("Введите секунды второй метки: "))

time1 = h1*3600 + m1*60 + s1
time2 = h2*3600 + m2*60 + s2
diff = time2 - time1
print(diff)