import pytest
from src.cart import Cart, EmptyCartError

def test_total_sums_items(cart):  # 함수의 매개변수 이름과 fixture 이름(cart)을 일치시킴
    cart.add("book", 12000, 2)
    assert cart.total() == 24000
