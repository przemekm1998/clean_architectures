from tdd_calc.fileinfo_patching import FileInfo
from unittest.mock import patch


def test_init():
    filename = 'somefile.txt'
    fi = FileInfo(filename)

    assert fi.filename == filename


def test_init_relative():
    filename = 'somefile.txt'
    relative_path = f'../{filename}'
    fi = FileInfo(relative_path)

    assert fi.filename == filename


@patch('os.path.getsize')
@patch('os.path.abspath')
def test_get_info(abspath_mock, getsize_mock):
    filename = 'somefile.txt'
    original_path = f'../{filename}'

    test_abspath = 'some/abs/path'
    abspath_mock.return_value = test_abspath

    test_size = 1234
    getsize_mock.return_value = test_size

    fi = FileInfo(original_path)
    info = fi.get_info()

    abspath_mock.assert_called_with(original_path)
    getsize_mock.assert_called_with(original_path)
    assert info == (filename, original_path, test_abspath, test_size)
