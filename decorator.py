# Функция декоратор
def time_this(nr):
    """
    Функция-декоратор для оценки времени выполнения функции, которая обернута декоратором
    nr - параметр, показывающий сколько раз запускать оборачиваемую функцию, для расчета среднего времени выполнения
    """
    import time
    # Функция-обертка, в которой происходит
    def wrapper(func):
        avg_time = 0
        for i in range(nr):
            t0 = time.time()
            func()
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time = avg_time/nr
        print("Выполнение заняло %.5f секунд" % avg_time)
        return func
    return wrapper


# Декорирование функции empty_func
@time_this(10)
def empty_func():
    for j in range(10000000):
        pass