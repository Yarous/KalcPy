import os#импорт библиотеки

os.system('pip install colorama')#устанавлеваем пакет
import colorama#импорт ранее установлиного пакета
from colorama import init
init()
from colorama import Fore, Back, Style

w = input("Чо делаем?: ")#тут понятно)
A = float(input("первое число: "))
b = float(input("второе число: "))

if w == "+":#если складываем
	k = A + b#тут создаём ответ
	print( Back.GREEN )#красим задний фон
	print(k)#выводим ранне созданнаю переменную
if w == "*":#если умножаем
	d = A * b#тут создаём ответ
	print( Back.RED )#красим задний фон
	print(d)#выводим ранне созданнаю переменную

if w == "-":#если убовляем
	l = A - b#тут создаём ответ
	print( Back.GREEN )#красим задний фон
	print(l)#выводим ранне созданнаю переменную
if w == "/":#если делим
	i = A / b#тут создаём ответ
	print( Back.BLUE )#красим задний фон
	print(i)#выводим ранне созданнаю переменную
	