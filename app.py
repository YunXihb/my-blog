import streamlit as st
import os
from datetime import datetime

# 页面配置
st.set_page_config(page_title="我的博客", page_icon="📝")

# 博客文章目录
POSTS_DIR = "posts"

# 获取所有文章
def get_posts():
    if not os.path.exists(POSTS_DIR):
        return []
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    posts = []
    for f in files:
        with open(os.path.join(POSTS_DIR, f), 'r', encoding='utf-8') as file:
            title = file.readline().strip().replace('# ', '')
            posts.append({'file': f, 'title': title})
    return sorted(posts, key=lambda x: x['title'])

# 读取文章内容
def get_post_content(filename):
    with open(os.path.join(POSTS_DIR, filename), 'r', encoding='utf-8') as file:
        return file.read()

# 侧边栏 - 文章列表
st.sidebar.title("📚 文章列表")
posts = get_posts()
if posts:
    selected = st.sidebar.radio("选择文章", [p['title'] for p in posts])
    post = next(p for p in posts if p['title'] == selected)
    content = get_post_content(post['file'])

    # 移除标题行（因为 Markdown 会渲染）
    lines = content.split('\n')
    content = '\n'.join(lines[1:])

    st.title(post['title'])
    st.markdown(content)
else:
    st.title("欢迎来到我的博客！")
    st.write("暂无文章，请在 posts 文件夹中添加 .md 文件。")
    st.info("格式：第一行是标题（# 标题），后面是正文")

# 页脚
st.sidebar.markdown("---")
st.sidebar.write("© 2024 我的博客")
