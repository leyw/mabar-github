import Cappucino

class CoffeeShop:

    _recipes = {};

    def register( self, coffeeName : str, make ):
        self._recipes[coffeeName] = make

    def serve( self, coffeeName):
        if coffeeName not in self._recipes:
            return "Sorry, your coffee is currently unavailable"
        
        coffee =  self._recipes[coffeeName]
        return coffee

coffeeshop = CoffeeShop()
cappucino_coffee = Cappucino.Cappucino()

coffeeshop.register("cappucino", cappucino_coffee.serve())