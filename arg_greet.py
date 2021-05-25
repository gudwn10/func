def greet(*names):
    for name in names:
        print('안녕하세요', name, '씨')
greet('홍길동', '양만춘', '이순신') # 인자가 3개
greet('James', 'Thomas')

def foo(*args):
    print('인자의개수',len(args))
    print('인자들:',args)
foo(10,20,30)