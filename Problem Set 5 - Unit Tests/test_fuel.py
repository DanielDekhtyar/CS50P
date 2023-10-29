# Learning Python with CS50
# Code for 'Refueling'
# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

import pytest
import fuel


def test_fraction():
  assert fuel.convert("1/2") == 50
  assert fuel.convert("1/4") == 25
  assert fuel.convert("3/4") == 75
  assert fuel.convert("1/3") == 33
  assert fuel.convert("1/3") != 30
  with pytest.raises(ValueError):
    fuel.convert("5/3")
    fuel.convert("cat/dog")
    fuel.convert("5/zebra")
  with pytest.raises(ZeroDivisionError):
    fuel.convert("5/0")
    fuel.convert("15/0")
  
def test_gauge():
  assert fuel.gauge(0) == "E"
  assert fuel.gauge(1) == "E"
  assert fuel.gauge(99) == "F"
  assert fuel.gauge(100) == "F"
  assert fuel.gauge(50) == "50%"
  assert fuel.gauge(75) == "75%"
  assert fuel.gauge(5) != "2%"