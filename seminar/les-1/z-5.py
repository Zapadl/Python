
# 5.Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

number = int(input('type in your number -> '))
if (((number%5)==0 & (number%10)==0) | (number%15==0)) & (number%30!=0):
print('success')
else:
print('did not work out!')