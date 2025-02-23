import csv

CVS_FILE = '../src/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', " \
               f"{self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError('Действие допустимо только для экземпляров класса Item или Phone')
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, product: str):
        if len(product) > 10:
            raise ValueError('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = product

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open(CVS_FILE, encoding='windows-1251') as file:
            file_reader = csv.DictReader(file, delimiter=',')
            for item in file_reader:
                name, price, quantity = item.get('name'), int(item.get('price')), int(item.get('quantity'))
                cls.all.append(name, price, quantity)

    @staticmethod
    def string_to_number(string: str) -> int:
        try:
            return int(string)
        except ValueError:
            return int(string[0: string.find('.')])
