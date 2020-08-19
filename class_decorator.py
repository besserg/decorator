from time import time


class Timer:
    """
    Класс-декоратор, для расчета среднего времени выполнения декорируемой функции
    """
    def __init__(self, func):
        self.func = func
        self.cntr = 10  # Количество запусков декорируемой функции

    def __call__(self, *args, **kwargs):
        avg_time = 0
        for i in range(self.cntr):
            t0 = time()
            self.func(*args, **kwargs)
            t1 = time()
            avg_time += (t1 - t0)
        avg_time = avg_time / self.cntr
        print("Выполнение заняло %.5f секунд" % avg_time)
        return self.func(*args, **kwargs)


# "Запуск" декоратора, для обертки функции empty_func
@Timer
def empty_func():
    for j in range(1000000):
        pass

empty_func()