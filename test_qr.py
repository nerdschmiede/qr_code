import glob
import os

import pytest
import qr


@pytest.fixture(autouse=True)
def delete_qr_codes_after_test():
    # Setup: fill with any logic you want
    yield   # this is where the test is happening
    # Teardown : fill with any logic you want
    endings = ['jpg', 'png', 'docx', 'pdf']
    for ending in endings:
        files = glob.glob(f'*.{ending}')
        for file in files:
            os.remove(file)


def test_write_and_read_jpg():
    data = "test data"

    qr_code = qr.Code(data)
    qr_code.save_jpg('test')

    assert qr.get_data("test.jpg") == data


def test_write_and_read_png():
    data = "test data"

    qr_code = qr.Code(data)
    qr_code.save_png('test')

    assert qr.get_data("test.png") == data


def test_write_docx_list():
    data = ['Alan', 'Ada', 'Grace']

    qr_code = qr.Code(data)
    qr_code.save_docx('test')

    assert os.path.isfile('test.docx')


def test_write_docx_single_data():
    data = 'Alan'

    qr_code = qr.Code(data)
    qr_code.save_docx('test')

    assert os.path.isfile('test.docx')


def test_write_pdf_list_data():
    data = ['Alan', 'Ada', 'Grace']

    qr_code = qr.Code(data)
    qr_code.save_pdf('test')

    assert os.path.isfile('test.pdf')
