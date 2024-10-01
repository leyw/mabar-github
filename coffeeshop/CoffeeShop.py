import Cappucino

class CoffeeShop:

    _recipes = []

    def register( self, coffeeName, make ):
        self._recipes[coffeeName] = make     

coffeeshop = CoffeeShop()

coffeeshop.register('cappucino', Cappucino())