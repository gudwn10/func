def print_sum():
    global a,b
    a = 100
    b = 200
    result = a + b
    print('print_sum() 내부 :', a, '과', b, '의 합은', result, '입니다.')
a = 10
b = 20 # 여기까지 a,b는 10,20
print_sum()# 여기서 a=100, b=200 할당
result=a+b
print('print_sum() 외부 :', a, '과', b, '의 합은', result, '입니다.')