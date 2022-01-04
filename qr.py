import qrcode
import cv2 as cv  # pip install opencv-python


class Code:
    def __init__(self, filename: str):
        self._filename = filename
        self._error_correction = qrcode.constants.ERROR_CORRECT_M

    def write_data(self, data: str):
        qr = qrcode.QRCode(error_correction=self._error_correction)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(self._filename)

    def set_error_correction_high(self):
        self._error_correction = qrcode.constants.ERROR_CORRECT_H

    def set_error_correction_medium(self):
        self._error_correction = qrcode.constants.ERROR_CORRECT_M

    def set_error_correction_low(self):
        self._error_correction = qrcode.constants.ERROR_CORRECT_L

    def read_data(self) -> str:
        image = cv.imread(self._filename)
        detector = cv.QRCodeDetector()

        data, _, _ = detector.detectAndDecode(image)
        return data
