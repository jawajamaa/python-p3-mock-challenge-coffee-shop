class Coffee:
    all = list()

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and len(name) >=3:
            self._name = name
        else:
            raise ValueError ("Coffee name must be a string 3 characters or longer")
        
    def __repr__(self):
        return f'{self.name}'
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        oneTypeCoffee = list()

        for order in type(self).orders(self):
            if order.coffee == self and order.customer not in oneTypeCoffee:
                oneTypeCoffee.append(order.customer)
        return oneTypeCoffee
    # don't think one can return a unique list with comprehension?
        # return set(list([order for order in type(self).orders(self) if order.coffee == self]))
    
    def num_orders(self):
        coffeeOrders = dict()

        for coffee in type(self).all:
            # breakpoint()
            coffeeOrders[f'{coffee}'] = coffeeOrders.get(f'{coffee}', 0) + 1
        return coffeeOrders

    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError ("Customer name must be a string between 1 and 15 characters")
        
    def __repr__(self):
        return f'Customer: {self.name}'
    
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:
    all = list()

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price
    
    def __repr__(self):
        return f'{self.customer} ordered {self.coffee} for £{self.price}'

    @price.setter
    def price(self, price):
        if isinstance(price, float) and not hasattr(self, "price") and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError ("The coffee price must be a float (number with one decimal place in the tenths column) between 1.0 and 10.0")
