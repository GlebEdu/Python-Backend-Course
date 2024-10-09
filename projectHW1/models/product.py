class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category):
        self.category = new_category

    def edit_price(self, new_price):
        self.price = new_price

    def set_sale(self, sale):
        self.sale = sale

    def cancel_sale(self):
        self.sale = 0

    def get_price(self):
        return self.price*(1-(self.sale/100))

    def __repr__(self):
        info = f"Product: {self.name} from category {self.category} costs {self.price}. "
        if self.sale == 0:
            info += "No discount.\n"
        else:
            info += f"{self.sale}% discount!\n"
        return info
