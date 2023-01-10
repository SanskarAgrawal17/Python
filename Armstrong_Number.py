#Program is to check whether the number is armstrong or not.
n = int(input("Enter The Number: "))
n1 = n
sum = 0
while n != 0:
    r = n % 10
    sum = sum + (r**len(str(n1)))
    n = int(n/10)
if n1 == sum:
    print("Number is armstrong number : ")
else:
    print("Number is not armstrong number :")
