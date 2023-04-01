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
                cls.all.append(item)

    @staticmethod
    def string_to_number(string: str) -> int:
        try:
            return int(string)
        except ValueError:
            return int(string[0: string.find('.')])
