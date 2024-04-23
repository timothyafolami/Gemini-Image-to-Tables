import easyocr
reader = easyocr.Reader(['en'], detector='DB', recognizer = 'Transformer')
result = reader.readtext('new_2.jpg')
print(result)

# reader = easyocr.Reader(['en'], detection='DB', recognition = 'Transformer')