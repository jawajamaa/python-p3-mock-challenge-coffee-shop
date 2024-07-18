class Coffee:

    def __init__(self, name):
        self.name = name
        
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
    # I don't think one can return a unique list with comprehension...
        # return set(list([order for order in type(self).orders(self) if order.coffee == self]))
    
    def num_orders(self):
        return len(self.orders())
     
    #  my below solution takes the average of all drinks and not just the tested order, necessitating the creation and use of the truncate_float() function, and doesn't take a 0.0 order possibility (resulting in attempting to divide by 0)
    # def average_price(self):
    #     order_Prices = [order.price for order in Order.all]
    #     total_all_prices = sum(order_Prices)/len(order_Prices)
    #     def truncate_float(num, decimal_places):
    #         multiplier = 10 ** decimal_places
    #         return int(num * multiplier)/ multiplier
    #     avg_price = truncate_float(total_all_prices, 1)
    #     return avg_price
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        total_price = sum(order.price for order in orders)
        average = total_price / len(orders)
        return round(average, 1)

    
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
        return f"Customer: {self.name}"
    
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def most_aficionado(self):
        coffee_spending = dict()

        for order in Order.all:
            breakpoint()
        # customer_total_spending = sum[order.price for order in self.orders()] 
        # coffee_spending[]
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
    
    @price.setter
    def price(self, price):
        if isinstance(price, float) and not hasattr(self, "price") and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError ("The coffee price must be a float (number with one decimal place in the tenths column) between 1.0 and 10.0")

    def __repr__(self):
        return f"{self.customer} ordered {self.coffee} for £{self.price}"
