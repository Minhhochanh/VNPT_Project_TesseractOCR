# VNPT_Project_TesseractOCR
1. Mục tiêu đề tài:
- Input 1 file PDF hình ảnh và sau đó xuất ra màn hình các nội dung và check xem ở ô chữ ký có bị bỏ trống hay không.
2. Công nghệ:
- Ngôn ngữ: Python.
- Gói thư viện: 
  + pytesseract (nhận diện chữ).
  + Gói ngôn ngữ tiếng Việt cho pytesseract.
  + pdf2image (xuất file pdf thành các hình ảnh).
  + opencv-python ( xử lý ảnh và thị giác máy tính).
3. Ý tưởng:
- Sau khi nhận được file PDF hình ảnh sẽ xuất tất cả sildes thành file hình ảnh với định dạng JPG hoặc PNG.
- Sau đó đọc tất cả các hình ảnh và xuất kết quả ra màn hình. 
4. Thực hiện:
