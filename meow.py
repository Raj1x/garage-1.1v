class Car:
    def __init__(self, model, oil, max_oil, v_max):
        self.model = model
        self.oil = oil
        self.max_oil = max_oil
        self.v_max = v_max
    def add_oil(self):
        self.oil = self.max_oil
        print(f" | Oil Refilled. Current oil: {self.oil}")
    def check_oil(self):
        print(f" | Oil: {self.oil}/{self.max_oil}")
    def empty_oil(self):
        self.oil = 0
    def check_v_max(self):
        print(f" | V-max: {self.v_max}")
# I sometimes think, that I should think more
cars = {
    "toyota": Car("Old ah toyota", 30, 100, 220),
    "nissan": Car("Nissan with 3 left wheels", 50, 120, 200),
    "tractor": Car("Moving clanker", 450, 1000, 10)
}

print(" | ===== GARAGE ===== | ")
select_car = input(f" | Choose car from your garage:\n | Avaliable cars:{cars.keys()}: ")
if select_car in cars:
    active_car = cars[select_car]
    print(f"\n | ===== Selected: {active_car.model} ===== | ")
else:
    print("\n | That car does not exist in your garage poor ass *Laughing anime girl*")
    exit

while True:
    what = input("\n | What action you want to commit on your car?: \n | 1.empty oil / 2. fill oil / 3. check oil / 4. check v-max / 5. exit: ")
    if what == "1":
        active_car.empty_oil()
        print(" | You poured out all oil...")
    elif what == "2":
        active_car.add_oil()
        print(f" | You added oil \n | Oil: {active_car.oil}/{active_car.max_oil}")
    elif what == "3":
        active_car.check_oil()
    elif what == "4":
        active_car.check_v_max()
    elif what == "5":
        print("===== You exit garage =====")
        break
        
