import math

class Car():
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def inflate(self):
        years = int(input("\nHow many years: "))
        rate = float(input("Rate: "))

        for x in range(0,years+1,1):
            new_price = self.price*((1+rate)**(-x))
        total_loss = math.trunc(self.price - new_price)
        cost_per_year = math.trunc(total_loss/years)

        print("\nRemaining equity: {}".format(math.trunc(new_price)))
        print("Total loss in value after {} years: {}".format(years, total_loss))
        print("Cost to own per year: {}".format(cost_per_year))
        print("Cost to own per month: {}".format(math.trunc(cost_per_year/12)))
        
        return None

    def showall(self):
        for i in a:
            print("Make: {}\nModel: {}\nYear: {}\nOriginal price: {}\n".format(
		i.make, i.model, i.year, i.price))
