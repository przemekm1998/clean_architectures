import pytest

from tdd_calc.calc import Calc


@pytest.fixture(scope='module')
def calc():
    yield Calc()


def test_add_two_numbers(calc):
    res = calc.add(4, 5)

    assert res == 9


def test_add_three_numbers(calc):
    res = calc.add(4, 5, 6)

    assert res == 15


def test_add_many_numbers(calc):
    s = range(100)

    assert calc.add(*s) == 4950


def test_subtract_two_numbers(calc):
    res = calc.sub(10, 3)

    assert res == 7


def test_mul_two_numbers(calc):
    res = calc.mul(7, 3)

    assert res == 21


def test_div_two_numbers(calc):
    res = calc.div(13, 2)

    assert res == 6.5
    assert type(res) is float


def test_div_by_zero_returns_inf(calc):
    res = calc.div(5, 0)

    assert type(res) is str
    assert res == 'inf'


def test_avg_correct_average(calc):
    res = calc.avg([2, 5, 12, 98])

    assert res == 29.25


def test_avg_removes_upper_outliers(calc):
    res = calc.avg([2, 5, 12, 98], ut=90)

    assert res == pytest.approx(6.33333)


def test_avg_removes_lower_outliers(calc):
    res = calc.avg([2, 5, 12, 98], lt=10)

    assert res == pytest.approx(55)


def test_avg_upper_threshold_is_included(calc):
    res = calc.avg([2, 5, 12, 98], ut=98)

    assert res == 29.25


def test_avg_lower_threshold_is_included(calc):
    res = calc.avg([2, 5, 12, 98], lt=2)

    assert res == 29.25


def test_avg_empty_list(calc):
    res = calc.avg([])

    assert res == 0


def test_avg_manages_empty_list_after_outlier_removal(calc):
    res = calc.avg([12, 98], lt=15, ut=90)

    assert res == 0


def test_avg_manages_empty_list_before_outlier_removal(calc):
    res = calc.avg([], lt=15, ut=90)

    assert res == 0


def test_avg_manages_zero_value_lower_outlier(calc):
    res = calc.avg([-1, 0, 1], lt=0)

    assert res == 0.5


def test_avg_manages_zero_value_upper_outlier(calc):
    res = calc.avg([-1, 0, 1], ut=0)

    assert res == -0.5
