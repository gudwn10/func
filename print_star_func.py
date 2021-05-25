def print_star():
    print('*********')
def print_hash():
    print('#########')
def print_plus():
    print('+++++++++')
    
for i in range(6):
    print_hash()
    print_star()
    print_plus()
    print_plus()
    print_star()
    print_hash()
    break

def plus(a):
    for i in range(a):
        print('*********')
        #return a

plus(4)