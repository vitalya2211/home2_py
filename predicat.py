from math import modf
import time 
import colorama
from colorama import Fore, Back 
colorama.init(autoreset=True)

def check_num(x):
    y=0
    while x:
        dig=x%10
        y=y*10+dig
        x//=10
    return y
def sum_digit(x):
    x=int(x)
    minus=False
    if x<0:
        x*=-1
        minus=True
    y=0
    while x:
        if x//10==0 and minus:
            y-=x%10
            return y
        y+= x%10
        x//=10
    return y
def mult_print(N:int,val:[])->list:
    x=1
    result=[1]
    for i in range(2,N+1):
        x*=i
        result.append(x)
    return result

def rand_dig(n:int)->int: 
    random_dig = float(time.time())
    random_dig-=int(random_dig)
    random_dig*=n
    random_dig=int(random_dig)
    return random_dig

#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Учтите, что числа могут быть отрицательными
#Пример: 67.82 -> 23 # 0.56 -> 11

digit_input=input('введите число для суммирования его чисел ->')
try:
    digit_input=digit_input.replace(',','')
    digit_input=digit_input.replace('.','')
    print(f'{sum_digit(digit_input)} сумма цифр числа')
except ValueError:
    print('ошибка ввода, хотелось цифр :-)')
#Напишите программу, которая принимает на вход число N и выдает набор произведений 
#(набор - это список) чисел от 1 до N.
#Не используйте функцию math.factorial.
#Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.
#Пример:- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
N=1
while N:
    try:
        N=int(input('введите число, для получения списка произведений от 1 до N \
для окончания работы, введите 0 -> '))
        val=[]
        for i in range(1,N+1):
            val.append(i)

        if N:
            print(mult_print(N,val))
        
    except ValueError:
        print(Fore.RED+ Back.YELLOW+ '\b\b\b\tAchtung!!!\n\tKritischer Fehler!!!\n\tGeben Sie die Nummer erneut ein (bitte)')


#Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, 
# но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа

try:
    num=int(input('введите число для проверки на полиндром ->'))
    num2=check_num(num)
    if num==num2:
        print(f'число {num} полиндром')
    else:
        while num !=num2:
            num+=num2
            num2=check_num(num)
        else: print(f'исходное число не полинром, полинромом является {num}')
        
except ValueError:
    print('ошибка ввода')
#    4 - Реализуйте выдачу случайного числа
#не использовать random.randint и вообще библиотеку random
#Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
#Учтите, что есть диапазон: от(минимальное) и до (максимальное)

from time import time

def time_random():
 return time() - float(str(time()).split('.')[0])

def gen_random_range(min, max):
 return int(time_random() * (max - min) + min)


print(gen_random_range(20,60))
