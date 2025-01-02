import os
import frontmatter
from datetime import datetime

# Hàm macro để tạo danh sách các bài viết
def define_env(env):
    @env.macro
    def post_list(folder="docs/post"):
        posts = []  # Danh sách lưu trữ các bài viết

        # Duyệt qua tất cả các file trong thư mục
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".md"):  # Chỉ xử lý các file Markdown
                    filepath = os.path.join(root, file)
                    
                    # Đọc metadata của file
                    with open(filepath, "r", encoding="utf-8") as f:
                        meta = frontmatter.load(f)
                        if "date" in meta:  # Kiểm tra nếu có metadata "date"
                            posts.append({
                                "title": meta.get("title", file.replace(".md", "")),
                                "date": datetime.strptime(meta["date"], "%Y-%m-%d"),
                                "url": filepath.replace("docs/", "").replace(".md", "/"),
                            })

        # Sắp xếp danh sách bài viết theo ngày tăng dần
        posts.sort(key=lambda x: x["date"])

        # Tạo danh sách Markdown
        output = "\n".join([
            f"- [{post['title']}]({post['url']}) ({post['date'].strftime('%Y-%m-%d')})"
            for post in posts
        ])
        return output
