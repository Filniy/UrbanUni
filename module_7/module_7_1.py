from pprint import pprint
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"
    
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        str_products = file.read()
        file.close()
        return  str_products

    def add(self, *products: Product):
        file = open(self.__file_name, 'a')
        products_file = self.get_products()
        for product in products:
            product = str(product)
            if product not in products_file:
                file.write(product+ '\n')
            else:
                print(f'Продукт {product} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())