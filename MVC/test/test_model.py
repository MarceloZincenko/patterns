import sys
sys.path.append('./')
from src.Model import Prices
import pytest

def test_get_all_prices():
    assert len(Prices.get_all_prices())>0

def test_get_prices_given_ticker():
    test_case = Prices("AL30")
    assert len(test_case.get_prices_given_ticker())>0

