num = input()
def prime():
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
b = 0
for i in range(len(num)):
    if not prime(int(num)):
        break
    else:
        b += 1
if b == 3:
    print(f'{num} is cycle prime number')
else:
    print(f'{num} is not cycle prime number')

