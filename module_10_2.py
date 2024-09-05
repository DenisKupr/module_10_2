import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f"{self.name}, на нас напали!")
        total_enemies = 100
        days = 0

        while total_enemies > 0:
            days += 1
            time.sleep(1)
            total_enemies -= self.power
            if total_enemies > 0:
                print(f"{self.name} сражается {days}  день(дня) ..., осталось {total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

# Создание экземпляров класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения всех потоков
first_knight.join()
second_knight.join()

print("Все битвы окончены!")
