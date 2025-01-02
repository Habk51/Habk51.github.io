import os
import frontmatter
from datetime import datetime

def define_env(env):
    @env.macro
    def post_list(folder="docs/post"):
        posts = []

        # Duyệt qua tất cả các file trong thư mục
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".md"):  # Chỉ xử lý các file Markdown
                    filepath = os.path.join(root, file)
                    
                    # Đọc metadata của file
                    with open(filepath, "r", encoding="utf-8") as f:
                        meta = frontmatter.load(f)
                        
                        # Kiểm tra và xử lý metadata "date"
                        if "date" in meta:
                            date = meta["date"]
                            # Nếu date là string, chuyển đổi sang datetime
                            if isinstance(date, str):
                                date = datetime.strptime(date, "%Y-%m-%d")
                            
                            posts.append({
                                "title": meta.get("title", file.replace(".md", "")),
                                "date": date,
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
