# 初始化 git 仓库
git init

# 绑定远程仓库
git remote add origin https://github.com/zl1732/LeetCode.git

# 拉取远程已有内容（并合并）
git pull origin main --allow-unrelated-histories

# 添加所有文件
git add .

# 提交一次
git commit -m "first commit"

# 把分支名字改成 main（和 GitHub 默认一致）
git branch -M main

# 推送到 GitHub
git push -u origin main

