def func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)


func(1, 2, 4, 5, 7, 8, 9, 14, name="ala", surname="ma_kota", age=10)