#zad1
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


a = Number(5)
b = Number(10)

result = a + b
print(result)  

#zad2
class Games:
    Year = 0  

    def __init__(self, year):
        Games.Year = year  
        self._name = None  

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class PCGames(Games):
    def __init__(self, year, system_requirements):
        super().__init__(year)
        self._system_requirements = system_requirements 

    def get_name(self):
        return f"PC Game: {self._name} (Requires: {self._system_requirements})"


class PS4Games(Games):
    def __init__(self, year, exclusive):
        super().__init__(year)
        self._exclusive = exclusive  

    def get_name(self):
        exclusive_status = "Exclusive" if self._exclusive else "Non-Exclusive"
        return f"PS4 Game: {self._name} ({exclusive_status})"


class XboxGames(Games):
    def __init__(self, year, supports_game_pass):
        super().__init__(year)
        self._supports_game_pass = supports_game_pass  

    def get_name(self):
        game_pass_status = "Supports Game Pass" if self._supports_game_pass else "Does not support Game Pass"
        return f"Xbox Game: {self._name} ({game_pass_status})"


class MobGames(Games):
    def __init__(self, year, platform):
        super().__init__(year)
        self._platform = platform  

    def get_name(self):
        return f"Mobile Game: {self._name} (Platform: {self._platform})"


pc_game = PCGames(2024, "Windows 10, 16GB RAM")
pc_game.set_name("Warhammer 40,000: Space Marine 2")
print(pc_game.get_name())

ps4_game = PS4Games(2024, False)
ps4_game.set_name("FC 25")
print(ps4_game.get_name())

xbox_game = XboxGames(2024, True)
xbox_game.set_name("S.T.A.L.K.E.R 2")
print(xbox_game.get_name())

mobile_game = MobGames(2012, "iOS, Android")
mobile_game.set_name("Mobile legends")
print(mobile_game.get_name())


      
#ExtraTask
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("The vehicle is moving.")

class Rocket(Vehicle):
    def move(self):
        print(f"The rocket {self.make} {self.model} is blasting into space.")


class Submarine(Vehicle):
    def move(self):
        print(f"The submarine {self.make} {self.model} is diving under the water.")


class Hoverboard(Vehicle):
    def move(self):
        print(f"The hoverboard {self.make} {self.model} is gliding above the ground.")


def transport_all(vehicles):
    for vehicle in vehicles:
        vehicle.move()


if __name__ == "__main__":
    rocket = Rocket("SpaceX", "Starship")
    submarine = Submarine("Borei-class submarine", "955")
    hoverboard = Hoverboard("FutureTech", "X500")

    vehicles = [rocket, submarine, hoverboard]

    transport_all(vehicles)
