# VNPT_Project_TesseractOCR
1. Mục tiêu đề tài:
- Input 1 file PDF hình ảnh và sau đó xuất ra màn hình các nội dung và check xem ở ô chữ ký có bị bỏ trống hay không.
2. Công nghệ:
- Ngôn ngữ: Python.
- Gói thư viện: 
  + pytesseract ( Để nhận dạng chữ từ ảnh).
  + Gói ngôn ngữ tiếng Việt cho pytesseract.
  + pdf2image (xuất file pdf thành các hình ảnh).
  + opencv-python ( Để xử lý và xem ảnh).
3. Ý tưởng:
- Sau khi nhận được file PDF hình ảnh sẽ xuất tất cả sildes thành file hình ảnh với định dạng JPG hoặc PNG.
- Sau đó đọc tất cả các hình ảnh và xuất kết quả ra màn hình. 
4. Thực hiện:
#import các thư viện 
import cv2
import os
import pytesseract
from pdf2image import convert_from_path

#xuất file PDF hình ảnh thành hình ảnh

input_path = 'text.pdf'

images = convert_from_path(input_path, 500)
 
for i in range(len(images)):
    image = images[i]
    image.save('data/output_{}.jpg'.format(i), 'JPEG')
