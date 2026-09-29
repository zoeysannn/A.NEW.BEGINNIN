z=int(input("Please enter a 4-digit number; "))

#1
# s=0
# for i in str(z):
#     s=s+int(i)
# print(s)

#2
# s=0
# while z>0:
#     k=z%10
#     s=s+k
#     z=z//10
# print(s)

#3
def recursive_digit_adder(number):
    if number > 10:
        return number%10 + recursive_digit_adder((number-number%10)//10)
    return number
print(recursive_digit_adder(z)) 

'''
        my teacher Frignate The Best did it! :)
'''