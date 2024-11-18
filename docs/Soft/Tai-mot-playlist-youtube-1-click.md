---
title: Tải audio của một playlist youtube với 1 click
aliases:
  - Tải audio của một playlist youtube với 1 click
tags:
  - soft
date: 2024-09-30
share: 
category:
---

## Đây là đoạn code python tải 1 playlist trên youtube về máy tính.

### Chạy lệnh gõ cmd
#### python  youtube.py

Lưu đoạn code bên dưới là youtube.py

- Nhớ thay URL của playlist youtube trong đoạn  lệnh nha.


```
import os
import yt_dlp as youtube_dl

# Đường dẫn lưu file tải về
download_path = os.path.expanduser("~/Downloads")

# URL của playlist
playlist_url = "https://www.youtube.com/watch?v=49BiJEqOsvQ&list=PLlpAWCqcstzoaQQMEU2d5YnZ1FZ60mtoJ"

# Cấu hình tải xuống
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ignoreerrors': True,  # Bỏ qua lỗi khi gặp video private hoặc không truy cập được
}

# Tải playlist
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(playlist_url, download=False)

    for entry in info_dict['entries']:
        if entry is None:
            # Bỏ qua video không truy cập được hoặc private
            print("Bỏ qua video private hoặc không khả dụng.")
            continue
        
        print(f"Tải video: {entry['title']}")
        ydl.download([entry['webpage_url']])

```


## file tải về đang ở dạng .webm

nên tôi viết thêm đoạn code này để chuyển sang mp3.

Sau khi chuyển xong thì xóa file cũ đi. - > chạy thành công.

Biết tý python mà thấy dễ chịu quá


```
import os
import subprocess

# Đường dẫn tới ffmpeg.exe
ffmpeg_path = r'H:\ffmpeg\bin\ffmpeg.exe'

# Thư mục chứa các file .webm đã tải về
download_path = r'C:\Users\nguyhh.LLC\Downloads\youtube'

# Duyệt qua các file trong thư mục
for filename in os.listdir(download_path):
    if filename.endswith(".webm"):
        # Đường dẫn đầy đủ tới file .webm
        webm_file = os.path.join(download_path, filename)

        # Tạo đường dẫn cho file .mp3 mới
        mp3_file = os.path.splitext(webm_file)[0] + ".mp3"

        # Sử dụng ffmpeg để chuyển đổi file .webm sang .mp3
        command = [
            ffmpeg_path,
            '-i', webm_file,
            '-vn',  # Chỉ trích xuất âm thanh
            '-ab', '192k',  # Bitrate của file âm thanh
            mp3_file
        ]

        # Thực hiện lệnh ffmpeg
        subprocess.run(command, check=True)

        # In thông báo hoàn thành chuyển đổi
        print(f"Chuyển đổi thành công: {webm_file} -> {mp3_file}")

```
