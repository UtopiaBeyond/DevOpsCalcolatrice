import pytest
from operazioni import moltiplicazione


def test_moltiplicazione_interi():
    assert moltiplicazione(-3, 2) == -6


def test_moltiplicazione_float_e_int():
    assert moltiplicazione(2.5, 2) == 5.0