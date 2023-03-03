import random


def compare(A):
    if(A%2==0):
        print(A/2)
    else:
        print((A*3)+1)

compare(random.randint(1,10))                                  