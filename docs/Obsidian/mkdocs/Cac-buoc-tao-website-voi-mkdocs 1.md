---
title: Các Bước tạo Website với MKDocs
aliases:
  - Các Bước tạo Website với MKDocs
tags:
  - obsidian
date: 2024-09-06
share: true
category: Obsidian
---
## Nguồn tham khảo:
- [link của mkdocs](https://squidfunk.github.io/mkdocs-material/getting-started/)
- [blog của Thiện qc](https://thienqc.github.io/blog/tags/)
## Chuẩn bị những gì

- Tải VS Code
- Tải Github destop
-  Đăng ký tài khoản github
- Cài đặt Python
- Tải template blog của một ai đó làm mẫu- mình sử dụng blog của thienqc.github.io
![](https://i.imgur.com/HHVnbz8.png)

## Lưu ý
-  Ở bước cài python nhớ chọn đường dẫn, nếu quên thì xóa->cài lại 
## Thực Hành

### B1-Trên github page
- Tạo một repository -> copy link HTTPS ->sang bước 2
![](https://i.imgur.com/9uaeMmK.png)

### B2 - Trên github destop 

Github destop đăng nhập bằng tài khoản github của bạn.
Vào mục File-> clone repository -> Paste đường link ở bước 1 để clone thư mục về máy tính. 

### B3  Vào VS code
 - Chọn file -Open folder vừa tạo ở bước 2
 - Mở Terminal trên VS code
 -  Nhập dòng lệnh bên dưới để cài mkdocs :[Tham khảo thêm ở đây](https://squidfunk.github.io/mkdocs-material/getting-started/)
 
```
 pip install mkdocs-material
```
### Bước 4 vẫn đang ở VS code

- Gõ tiếp dòng lệnh ở trong cái folder blog  vừa clone và đang mở VS code gõ mkdocs new . (dấu chấm) 
  - Nhớ là mkdocs new . (dấu . để nó ko tạo thêm folder con)
  
```
  mkdocs new . 
```
![](https://i.imgur.com/fX0eRRn.png)

Sau bước này sẽ thấy trong folder có thêm file mkdocs.yml và folder docs chứa tệp index

![](https://i.imgur.com/EYg61hK.png)

Xong rồi, giờ ta gõ tiếp ,lệnh này là để ==preview== web thôi. 



```
mkdocs server
```

Giờ ta đã có một website được hiện thị ở đường link hiện ra trên cửa sổ Terminal của VS code kiểu 

 ==link http://127.0.0.1:8000/ là truy cập được rồi==

### B5 Đến bước cấu hình theo cá nhân rồi đây

Website bên trên là một web cơ bản nhất ( tempalte ) Giờ ta cần làm một chút để nó được cá nhân hóa và làm đẹp và đẩy lên mạng là xong rồi. cùng làm tiếp các bước sau nhé.

#### B5.1 
 Trong folder ==blog==  ( trong ví dụ của mình là folder blog)
Mở Folder template của thiện qc tải ở bước B1 Copy các tệp sau vào folder của mình

![](https://i.imgur.com/7iZxVU7.png)


> [!NOTE] Một số lưu ý khi copy
> tệp mkdocs thì đè lên tệp cũ của mình ( để đỡ phải setup nhiều)


mở tiếp thư mục docs của thienqc copy tiếp sang thư mục của mình
![](https://i.imgur.com/DvjeTAQ.png)
#### B5.2 Giờ chỉnh lại một chút file mkdocs.yml để thành web của mình

![](https://i.imgur.com/MDp8rEm.png)
![](https://i.imgur.com/qlNAB2Q.png)
Xong rồi thì lưu lại nhé
![](https://i.imgur.com/Y5icZXE.png)
### B6 cài đặt web trên github page nữa là xong rồi.

![](https://i.imgur.com/LmEl2s8.png)
Chờ và truy nhập web thôi
