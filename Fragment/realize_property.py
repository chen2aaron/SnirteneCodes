class CelsiusA:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


a = CelsiusA(37)
print(a.temperature)
print(a.to_fahrenheit())
print(a.__dict__)
print('-'*20)


class CelsiusB:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


b = CelsiusB(37)
print(b._temperature)
print(b.to_fahrenheit())
print(b.get_temperature())
print(b.set_temperature(-270))
print(b._temperature)
print('-'*20)


class CelsiusC:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)

c = CelsiusC(29)
print(c.temperature)
print(c.to_fahrenheit())
print(c.get_temperature())
print(c.set_temperature(123))
print('-'*20)


class CelsiusD:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    @temperature.deleter
    def temperature(self):
        print("Delete value")
        del self._temperature

d = CelsiusD(100)
del d.temperature
print(d.temperature)