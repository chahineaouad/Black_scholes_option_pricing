import numpy as np
import scipy.stats as stats

class BlackScholes:
    def __init__(self, spot, strike, days, rate, volatility):
        self.spot = spot
        self.strike = strike
        self.days = days/365
        self.rate = rate
        self.volatility = volatility

        self.d1 = (np.log(spot/strike) + (rate + .5 * np.square(volatility)) * self.days) / volatility * np.sqrt(self.days)
        self.d2 = self.d1 - self.volatility * np.sqrt(self.days)

    def call_price(self):
        return self.spot * stats.norm.cdf(self.d1) - self.strike * np.exp(-self.rate * self.days) * stats.norm.cdf(self.d2)

    def put_price(self):
        return self.strike * np.exp(-self.rate * self.days) * stats.norm.cdf(-self.d2) - self.spot * stats.norm.cdf(-self.d1)

    def call_delta(self):
        return stats.norm.cdf(self.d1)

    def put_delta(self):
        return stats.norm.cdf(self.d1) - 1

    def call_gamma(self):
        return np.exp(-.5 * np.square(self.d1)) / np.sqrt(2*np.pi) / (self.spot * self.volatility * np.sqrt(self.days))

    def put_gamma(self):
        return self.call_gamma()

    def call_vega(self):
        return self.call_gamma() * np.square(self.spot) * self.volatility * self.days

    def put_vega(self):
        return self.call_vega()


if __name__ == '__main__':
    input = input("Enter spot,strike,days,rate,volatility respectively: ")
    list = input.split(",")

    bs = BlackScholes(float(list[0]), float(list[1]), float(list[2]), float(list[3]), float(list[4]))

    print(f"price call: {bs.call_price()}, price put: {bs.put_price()}")
    print(f"call delta:{bs.call_delta()}, put delta:{bs.put_delta()}")
    print(f"call gamma = put gamma: {bs.call_gamma()}")
    print(f"call_vega = put_vega: {bs.call_vega()}")
    print("Thanks to Alon Sela for formulas ! ")
