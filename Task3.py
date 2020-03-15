'''
Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
самом начале проверьте, хватит ли вам бензина из расчета того, что машина
расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
то пусть этот метод добавляет эти километры к значению одометра, но не
напрямую, а с помощью приватного метода __add_distance. Помимо этого
пусть метод drive также отнимет потраченное количество бензина с помощью
приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
more!”
'''
import time

class Car:
    def __init__(self, make, model, year, odometer, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
        self.fuel = fuel
        print(
        f'''
        Марка: {self.make}
        Модель: {self.model}
        Год выпуска: {self.year}
        Пробег: {self.odometer}
        Скорость: 100 км/час
        ''')
    def rasxod_car(self):
        self.dlina = int(input("Расстояние: "))
        self.benzin = int(input("Бензин: "))
        self.speed = int(input("скорость: "))
    
    def _add_distance(self):
        self.res = self.dlina // 10
        self.time_lite = (self.dlina / self.speed) * 60
        
        if self.res <= self.benzin:
            """
            Чтобы не ждать отключите time.sleep(local_time)
            """
            print(f"Мы уже в пути до место назначения {self.time_lite} минут")
            print(f"Подождите {int(self.time_lite)} минут ")
            local_time = float(self.time_lite)
            local_time = local_time * 60
            # time.sleep(local_time)
            print(f"Вы приехали в место назначения. Одометор машины {int(self.odometer) + int(self.dlina)} ")
            print(f"Осталось {self.benzin - self.res} литр бензина")
        else:
            print("Недостаточно топлива")


Auto = Car('Make', 'Model', 'Year', 0,'Fuel')
Auto.rasxod_car()
Auto._add_distance()
