### 🎯 Hướng dẫn đầy đủ dùng AI **FREE** trong **Obsidian Copilot**

### ✅ Bước 1: Tạo API Key OpenRouter

---

1.  Truy cập: [https://openrouter.ai/keys](https://openrouter.ai/keys)
2.  Đăng nhập tài khoản OpenRouter.
3.  Click **Create Key** → đặt tên (ví dụ: `ObsidianCopilot`) → **Generate**.
4.  Sao chép API Key dạng như:`sk-or-abc123xyz...`

### ✅ Bước 2: Tìm model Free mạnh nhất

1.  Vào: [https://openrouter.ai/models](https://openrouter.ai/models)
2.  Tìm kiếm từ khoá:  
    *   `Free` (chỉ hiện model miễn phí)
3.  Sắp xếp theo:  
    *   **Sort → Top models this week** (lọc ra model mạnh nhất tuần)
4.  Chọn model có tag tốt như:_`fast` (nhanh)_
5. `reasoning` (suy luận tốt)

📌 Ví dụ:

- `deepseek/deepseek-chat-v3-0324:free`
- `openchat/openchat-3.5-1210:free`
- `meta-llama/llama-3-8b-instruct:free`

### ✅ Bước 3: Thêm Model vào Obsidian Copilot

Mở **Obsidian** → `Settings → Copilot → Add Custom Model`, và điền:

Trường
Nội dung nhập




Model Name
deepseek/deepseek-chat-v3-0324:free (hoặc model free bạn chọn)


Display Name
DeepSeek V3 Free (hoặc đặt tên tùy thích)


Provider
OpenRouter


Base URL
(Để TRỐNG – không cần điền)


API Key
Dán API Key OpenRouter vừa tạo


Enable CORS
✅ BẬT Enable CORS (bật dấu tick này!)

👉 Sau đó bấm **Add Model**.

### ✅ Bước 4: Sử dụng Model trong Obsidian Copilot

-   Mở Copilot Chat (sidebar phải).
-   Ở ô chọn model, chọn model bạn vừa thêm (ví dụ: DeepSeek V3 Free).
-   Chat, hỏi, tương tác hoàn toàn **miễn phí**!

### 📋 Tóm tắt quy trình nhanh:

1. Tạo OpenRouter API Key
2. Vào models page → Filter Free → Sort Top Week
3. Copy model name chính xác
4. Add vào Copilot ( nhớ bật Enable CORS ✅ )
5. Sử dụng free!

### ⚡ Ghi nhớ:

Lỗi gặp phải
Cách xử lý




Lỗi "model ID"
Copy model name đúng 100%


Lỗi CORS nếu KHÔNG bật
Nhớ bật Enable CORS ✅


Server lỗi 403, timeout
Thử lại sau vài phút