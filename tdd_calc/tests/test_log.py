from unittest.mock import patch
from tdd_calc.logger import Logger


@patch('tdd_calc.logger.datetime.datetime')
def test_log(mock_datetime):
    test_now = 123
    test_message = 'test message'
    mock_datetime.now.return_value = test_now

    test_logger = Logger()
    test_logger.log(test_message)
    assert test_logger.messages == [(test_now, test_message)]
