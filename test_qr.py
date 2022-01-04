import glob
import os

import pytest
import qr


@pytest.fixture(autouse=True)
def delete_qr_codes_after_test():
    # Setup: fill with any logic you want
    yield   # this is where the test is happening
    # Teardown : fill with any logic you want
    jpgs = glob.glob('*.jpg')
    for file in jpgs:
        os.remove(file)


def test_write_and_read():
    data = "test data"

    qr_code = qr.Code("test.jpg")
    qr_code.write_data(data)

    assert qr_code.read_data() == data


def test_write_high_error_correction():
    data = "test data"

    qr_code = qr.Code("test_h.jpg")
    qr_code.set_error_correction_high()
    qr_code.write_data(data)
