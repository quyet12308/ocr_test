# dự án test ocr 

## mục đích 
- Test công nghệ ocr vào thực tế 
- Hiện đang làm về 3 lĩnh vực : bussiness card , cccd , hóa đơn 
- Mục đích chính là trích xuất thông tin có ích từ ảnh 

## công nghệ sử dụng 
- easyocr có thể sẽ dùng thêm ppocr hoặc 1 cái thư viện nào đó khác .
- Hiện tại mới chỉ dùng model sẵn có . Nhưng tương lai rất có thể sẽ cần train lại model hoặc sẽ cần áp dụng thêm 1 số công nghệ mới
- Hiện tại chưa có các bộ giải mã (kiểu như CTC ) hoặc ctc đã ẩn ở trong các thư viện kia rồi .

## Cấu trúc dụ án 
- main là file chính 
- Thư mục check_data_text là thư mục chứa code khai thác data nhận được sau khi chạy inference chủ yếu là sử lý theo cách regex 

## Các chạy thử nghiệm 
- B1: tải và cài đặt python 
- B2: tải và cài đặt các thư viện cần thiết 
```cmd
pip install -r requirements.txt
```

- B3: Chạy dự án 
```cmd
python main.py
```