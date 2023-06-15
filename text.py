import cv2
import os

import img as img
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# Đường dẫn đến thư mục chứa các hình ảnh
folder_path = "C:\\Users\\minh nguyen\\PycharmProjects\\text1\\data"
 # Kiểm tra nếu là tệp tin ảnh (có thể sử dụng các định dạng khác như .jpg, .png, ...)
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
# Đường dẫn đầy đủ tới tệp tin ảnh
for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(folder_path, image_file)

    # Read the image using cv2
    image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
recognized_text = pytesseract.image_to_string(image)
# Display the recognized text
print('Image:', image_file)
print('Text:', recognized_text)
print()
#boxes=pytesseract.image_to_data(img)
#text = pytesseract.image_to_string(img, lang='eng')
#print(text)
#for x,b in enumerate(boxes.splitlines()):
  #  if x!=0:
   #     b=b.split()
    #    print(b)



