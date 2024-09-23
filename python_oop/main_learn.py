import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # print(f"An instance of {name} is created")

        # Run validations to the received argumnets
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price)
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))
# print(item2.name, item2.price, item2.quantity)

# print(Item.__dict__) # All attributes for Class level
# print(item1.__dict__) # All attributes for Instance level
# # print(item2.pay_rate)

# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name)

# Item.instantiate_from_csv()
# print(Item.all)
