class ShoppingCard:
    def __init__(self, prices):
        self.prices = prices
        
    def total_price(self,prices):
        return sum(prices)

prices = [2, 4, 6, 8, 10]
card = ShoppingCard(prices)
total = card.total_price(prices)
print(total)
