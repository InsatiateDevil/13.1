import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def coll():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, но и "
                    "получение дополнительных функций для удобства жизни",
                    [Product("Samsung Galaxy C23 Ultra",
                             "256GB, Серый цвет, 200MP камера",
                             180000.0, 5),
                     Product(
                         "Iphone 15", "512GB, Gray space",
                         210000.0, 8),
                     Product("Xiaomi Redmi Note 11",
                             "1024GB, Синий",
                             31000.0, 14)])


def test_init(coll):
    coll_for_test = coll.products[0]
    assert coll_for_test.name == "Samsung Galaxy C23 Ultra"
    assert coll_for_test.description == "256GB, Серый цвет, 200MP камера"
    assert coll_for_test.price == 180000.0
    assert coll_for_test.quantity == 5
