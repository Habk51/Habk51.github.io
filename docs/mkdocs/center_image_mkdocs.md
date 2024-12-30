---
title: căn ảnh vào center của mkdocs
aliases:
  - căn ảnh vào center của mkdocs
tags:
  - mkdocs
date: 
url: 
author: 
Releated:
---

> [!NOTE] # Bực bội với cái ảnh nằm không đúng center?
>  
> 

đã có cách khắc phục

## 1. copy file extra.css

![](https://i.imgur.com/ltCp0Mz.png#center)
### Đây là code của css
```
img[src*="#center"] {
    display: block;
    margin: 0 auto;
}
```

## 2. thêm mục extra.css vào file mkdocs.yml
![](https://i.imgur.com/m2F6jjT.png#center)


## 3. Trên note thì  thêm  #center vào 
![](https://i.imgur.com/o1Lz68m.png#center)


### [Nguồn tham khảo](https://github.com/squidfunk/mkdocs-material/issues/748)