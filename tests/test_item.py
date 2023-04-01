import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item('Смартфон', 10000, 20)


def test_item_init(item):
    assert item.name == 'Смартфон'
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000


def test_correct_name(item):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_incorrect_name(item):
    with pytest.raises(ValueError):
        item.name = 'СуперСмартфон'


def test_string_to_number():
    assert Item.string_to_number('8.4') == 8
