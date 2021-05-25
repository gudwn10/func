def sum_nums(*args):
    data=0
    for i in args:
        data +=i
    data_mean = data / len(args)
    return data, data_mean
a , b = sum_nums(10, 20, 30)
print(f'합 : {a}, 평균 {b}')
a, b = sum_nums(10, 20 ,30 ,40 ,50)
print(f'합 : {a}, 평균 {b}')