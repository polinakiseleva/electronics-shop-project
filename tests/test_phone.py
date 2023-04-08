import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("IPhone 11 Pro", 60000, 15, 1)


def test_phone_init(phone):
    assert phone.name == "IPhone 11 Pro"
    assert phone.price == 60000
    assert phone.quantity == 15
    assert phone.number_of_sim == 1


def test_phone_repr(phone):
    assert repr(phone) == "Phone('IPhone 11 Pro', 60000, 15, 1)"


def test_incorrect_sim(phone):
    phone.number_of_sim = 0
    assert ValueError


def test_number_of_sim_ok(phone):
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
