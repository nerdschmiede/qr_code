# qr_code
QR Code module um QR Codes schnell zu erstellen.
Importiere das Modul
```
import qr
```

Eingabe kann ein String sein:
```
data = "test data"
qr_code = qr.Code(data)
qr_code.save_jpg('test')
```
Man kann auch eine Liste von Daten eingeben und ein Word Dokument speichern:
```
data = ['Alan', 'Ada', 'Grace']
qr_code = qr.Code(data)
qr_code.save_docx('test')
```
oder ein PDF erstellen.
```
data = ['Alan', 'Ada', 'Grace']
qr_code = qr.Code(data)
qr_code.save_pdf('test')
```
