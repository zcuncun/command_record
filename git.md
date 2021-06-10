# 常用
## 本地

$ git init // 将当前目录变成一个Git可以管理的仓库

$ git status // 查看当前仓库状态（仓库下的工作区文件是否被修改过）

$ git add file2.txt file3.txt // 添加file2.txt和file3.txt两个文件

$ git rm test.txt // 情况1：确认删除

$ git commit -m "wrote a readme.txt." // 将文件提交到仓库（把暂存区的所有内容提交到当前分支）

$ git reset --hard HEAD^ // 回到上一个版本（HEAD: 当前版本，HEAD^: 上一个版本，HEAD~100: 往上100个版本）

$ git reset --hard 1234567 // 回到指定版本号commit id
　
$ git checkout -- readme.txt // 将readme.txt撤回到最近一次git add或git commit状态（注：--表示在当前分支，如果没有，则切换到另一个分支）

$ git checkout -b <name> // 创建+切换分支
  
$ git merge <name> // 合并分支到当前分支上

$ git branch -d <name> // 删除该分支

## 远程

git push origin master // 以后每次本地修改更新后，推送最新修改

git push origin --delete Chapater6 //  可以删除远程分支Chapater6 
  
git branch <name> // 创建分支（如：git branch dev）

git checkout <name> // 切换分支

// 4.2 解决冲突

git log --graph // 查看分支合并图

git log --graph --pretty=oneline --abbrev-commit // 查看分支合并缩略图

// 4.3 分支管理策略

git merge --no-ff -m "注释" dev // 合并后的分支有历史记录，而Fast-Forward合并之后，分支没有历史记录

// 4.4 Bug分支

git stash // 隐藏分支工作现场，为修复bug准备

git stash list // 查看有哪些分支隐藏的工作现场，为恢复工作现场做准备

git stash apply // 恢复工作现场，


git stash drop // 删除存储的stash内容，恢复到隐藏前的工作现场

git stash pop // 恢复到隐藏前的工作现场，相当于git stash apply和git stash drop

git stash apply stash@{0} // 可以多次stash，通过git stash list查看所有的stash，然后可以恢复到指定的隐藏的工作现场

// 4.5 Feature分支

注：当添加一个feature时，最好新建一个分支：git checkout -b <name>

git branch -D <name> // 强行删除一个没有被合并到主分支的分支

// 4.6 多人协作（最好结合工作场景理解）

git remote -v // 查看远程库详细信息

git push origin dev // push本地dev分支到远程dev

git push origin master // push本地master分支到远程master（时刻保持同步）

git pull // 将最新的pull/dev(master)爬下来

git checkout -b branch-name origin/branch-name // 在本地创建和远程分支对应的分支

git branch --set-upstream-to=origin/<branch> dev // 建立本地分支和远程分支的关联

git tag <tagname> // 创建标签

git tag // 查看所有标签

git tag <tagname> commitId // 为某次提交创建指定标签

git show <tagname> // 查看指定标签具体内容

git tag -a <tagname> -m "v0.1 released" commitId // 为某次指定的提交创建标签，同时添加标签注释
  
  
 
## 查看

$ git diff readme.txt // 查看工作区的readme.txt与缓存区的readme.txt的区别

$ git diff --cached // 比较暂存区（stage/index）和分支（master）的区别

$ git log // 查看最近到最远的提交记录（详情: commit id + Author + Date + comment）

$ git log --pretty=oneline // 查看最近到最远的提交记录（简写：commit id + comment）

$ git reflog // 查看每一次命令记录历史，确保能回到任意版本　

git tag -d <tagname> // 删除某个标签

git push origin <tagname> // 推送某个标签到远程库

git push origin --tags // 一次性推送所有标签到远程库

git tag -d v0.9 // 删除远程库标签（第一步：删除本地库标签）

git push origin :refs/tags/v0.9 // 删除远程库标签（第二步：从远程库删除标签）
