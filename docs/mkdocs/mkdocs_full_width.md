---
title: Cách xóa khoảng trắng lề của mkdocs
aliases:
  - Cách xóa khoảng trắng lề của mkdocs
tags:
  - mkdocs
date: 
url: 
author: 
Releated:
---

## > [!NOTE]  Xóa khoảng trắng ở lề mkdocs


![](https://i.imgur.com/qKzHywJ.png)
# [Nguồn tham khảo](https://github.com/squidfunk/mkdocs-material/discussions/3692)


## Cách Hà thực hiện

### Bước 1: trong thư mục docs/assets/stylesheets 
tạo file custom.css
![](https://i.imgur.com/zWgnxqM.png)

#### Đây là nội dung file css

```
@media only screen and (min-width: 76.25em) {
  .md-main__inner {
    max-width: none;
  }
  .md-sidebar--primary {
    left: 0;
  }
  .md-sidebar--secondary {
    right: 0;
    margin-left: 0;
    -webkit-transform: none;
    transform: none;   
  }
}
```
### Bước 2: Trong file mkdocs.yml

![](https://i.imgur.com/zewjJcg.png)
