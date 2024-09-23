from item import Item

class Phone(Item):
    # all = []
    def __init__(self, name: str, price: float, quantity = 0, broken_phones=0):
        # print(f"An instance of {name} is created")

        # Call to super function
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received argumnets
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

        # Actions to execute
        # Phone.all.append(self)
