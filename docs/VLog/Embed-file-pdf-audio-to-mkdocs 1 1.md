---
title: Thêm pdf  và audio vào web như nào đây
aliases:
  - Thêm pdf  và audio vào web như nào đây
tags:
  - pdf
date: 
share: 
category:
---
# Phần 1- Nhúng file pdf vào web

## Bước 1- Bạn  cần up file lên google drive nhé.

## Bước 2:  Cope lấy cái link share- copy paste sang cửa sổ mới thì ta thấy đuôi của link nhận được có chữ ==view==

## Bước 3:  Sửa lại chữ ==view== thành ==preview== và paste link này vào cấu trúc embeded thôi là xong rồi.

#### Dưới đây là cấu trúc embebed, bạn copy lại và thay link tương ứng.

```
<iframe src="https://drive.google.com/file/d/1osXjAxtuNgW-ePlylnPoMJAkR4f09y3h/preview" width="100%" height="800px" frameborder="0"></iframe>
```
![](https://i.imgur.com/fQeiMwv.png)



                          🍀🍀🍀🍀🍀🍀


## Tương tự với file mp3 trên google drive nhé
![](https://i.imgur.com/62eokTq.png)


 ## Cách khác dễ dàng hơn là dùng tài khoản soudcloud ( nền tảng nghe nhạc miễn phí).

- Chọn file muốn nhúng.
-  Chọn Nút Share ![](https://i.imgur.com/w3BpcGP.png)
- Chọn mục embed
- rồi copy mã code paste vào ![](https://i.imgur.com/LExwZ6O.png)
### Dưới đây là ví dụ

<iframe width="100%" height="150" scrolling="no" frameborder="no" allow="autoplay=false" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/198275799&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/alamgir-4" title="Alamgir" target="_blank" style="color: #cccccc; text-decoration: none;">Alamgir</a> · <a href="https://soundcloud.com/alamgir-4/track04" title="Track04" target="_blank" style="color: #cccccc; text-decoration: none;">Track04</a></div>


#### Để khi load page ==không tự động phát== thì bạn sửa như sau 
![](https://i.imgur.com/mTkcq71.png)
![](https://i.imgur.com/v58G7lW.png)
