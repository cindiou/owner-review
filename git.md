- [Git 的设计理念](#git-的设计理念)
- [创建仓库 | 时光穿梭](#创建仓库--时光穿梭)
- [远程仓库](#远程仓库)
- [分支管理](#分支管理)
  - [分支创建 | 合并](#分支创建--合并)
  - [分制管理策略](#分制管理策略)
  - [Bug 分支](#bug-分支)
  - [feature分支](#feature分支)
  - [多人协作](#多人协作)
  - [rebase | 衍合过程](#rebase--衍合过程)
- [标签](#标签)
- [Gitee](#gitee)
- [自定义Git](#自定义git)
  - [.gitignore文件](#gitignore文件)
  - [配置别名](#配置别名)


# Git 的设计理念

```markdown
Git
分布式的核心设计是同步，而不是主从

集中式和分布式的区别是：你的本地是否有完整的版本库历史！
假设 SVN 服务器没了，那你丢掉了所有历史信息，因为你的本地只有当前版本以及部分历史信息。
假设 GitHub 服务器没了，你不会丢掉任何 git 历史信息，因为你的本地有完整的版本库信息。你可以把本地的 git 库重新上传到另外的 git 服务商。

Unix 的哲学是“没有消息就是好消息”，说明添加成功。

注意事项：

- 如果要真正使用版本控制系统，就要以纯文本方式编写文件。
- 千万不要使用 Windows 自带的记事本编辑任何文本文件
```

# 创建仓库 | 时光穿梭

```markdown
- 版本回退
- 工作区、暂存区、仓库
- 管理、撤销修改
- 删除文件
```

```markdown
## 常用命令

git init

- git add
  每次修改，如果不用 git add 到暂存区，那就不会加入到 commit 中。
- git commit -m

git status
git diff

- git log 命令显示从最近到最远的提交日志
  --pretty=oneline
  git log --graph --pretty=oneline --abbrev-commit

- git reset --hard HEAD^
  HEAD^^
  HEAD~100

- git reflog 查看命令历史

## 区域划分

工作区>>>>暂存区>>>>仓库

git add 把文件从工作区>>>>暂存区，git commit 把文件从暂存区>>>>仓库，

git diff 查看工作区和暂存区差异，
git diff --cached 查看暂存区和仓库差异，
git diff HEAD 查看工作区和仓库的差异，
git diff HEAD -- readme.txt

git diff 时是分为两种情况的：暂存区为空和暂存区不为空。
首先我们明确知道 git diff 是比较工作区和暂存区的文件的，如果此时暂存区为空，那么稍微有点不同，即：

- 1.暂存区为空使用 git diff：因为此时暂存区为空，此时使用 git diff 同样也是比较工作区和仓库，即和使用 git diff HEAD 结果相同
- 2.暂存区不为空使用 git diff:因为此时暂存区不为空，此时使用 git diff 比较的就是工作区和暂存区

git add 的反向命令 git checkout，撤销工作区修改，即把暂存区最新版本转移到工作区，

- git checkout -- readme.txt
- 回到最近一次 git commit 或 git add 时的状态
- 工作区 <<< 暂存区 <<< 仓库
- 暂存区有没有内容，有则从暂存区回退，没有则从仓库回退
- 什么时候暂存区会没有内容？答：git commit 之后

git commit 的反向命令 git reset HEAD，就是把仓库最新版本转移到暂存区。

场景 1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令 git checkout -- file。
场景 2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令 git reset HEAD <file>，就回到了场景 1，第二步按场景 1 操作。
场景 3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。

## git checkout 的划分

版本的 Git 引入了两个新命令 git switch 和 git restore，用以替代现在的 git checkout。git checkout 这个命令承担了太多职责，既被用来切换分支，又被用来恢复工作区文件，对用户造成了很大的认知负担。

git restore <file>
git checkout -- <file>

git restore --staged <file>
git reset HEAD <file>

情景：先添加一个新文件 test.txt 到 Git 并且提交：
情况一：工作区文件删除，无其他操作

1. rm test.txt
   以下命令可恢复文件
   git restore test.txt

情况二：工作区文件删除，版本库文件删除

1. rm test.txt
2. git rm test.txt
3. git commit -m "remove test.txt"
   以下命令可恢复文件：
   git reset --hard HEAD^
```

# 远程仓库

```markdown
要关联一个远程库，使用命令 git remote add origin git@server-name:path/repo-name.git；
关联一个远程库时必须给远程库指定一个名字，origin 是默认习惯命名；
关联后，使用命令 git push -u origin master 第一次推送 master 分支的所有内容；
此后，每次本地提交后，只要有必要，就可以使用命令 git push origin master 推送最新修改；

git remote -v
git remote rm origin
此处的“删除”其实是解除了本地和远程的绑定关系，并不是物理上删除了远程库。远程库本身并没有任何改动。要真正删除远程库，需要登录到 GitHub，在后台页面找到删除按钮再删除。

从远程库克隆
git clone git@github.com:michaelliao/gitskills.git .

Git 支持多种协议，默认的 git://使用 ssh，但也可以使用 https 等其他协议。
Git 支持多种协议，包括 https，但 ssh 协议速度最快。
```

# 分支管理

## 分支创建 | 合并

```markdown
解决合并冲突

查看分支：git branch
  查看远程分支 git branch -r
  查看所有分支 git branch -a
  删除本地分支 git branch -d 分支名  比如 git branch -d dev
  强制删除本地分支 git branch -D 分支名  
  删除远程分支 git push 远程仓库名 :分支名     比如  git push origin :dev
创建分支：git branch <name>

切换分支：git checkout <name>或者 git switch <name>
创建+切换分支：git checkout -b <name>或者 git switch -c <name>
合并某分支到当前分支：git merge <name>

- 先切换到主分支：git checkout master
- 将 dev 分支合并到主分支：git merge dev

删除分支：git branch -d <name>
```

## 分制管理策略

![](img/git/2022-03-18-16-10-25.png)

```markdown
通常，合并分支时，如果可能，Git 会用 Fast forward 模式，但这种模式下，删除分支后，会丢掉分支信息。
如果要强制禁用 Fast forward 模式，Git 就会在 merge 时生成一个新的 commit，这样，从分支历史上就可以看出分支信息。

请注意--no-ff 参数，表示禁用 Fast forward：
  git merge --no-ff -m "merge with no-ff" dev
因为本次合并要创建一个新的 commit，所以加上-m 参数，把 commit 描述写进去。
```

## Bug 分支

```markdown
修复 bug 时，我们会通过创建新的 bug 分支进行修复，然后合并，最后删除；

当手头工作没有完成时，先把工作现场 git stash 一下，然后去修复 bug，修复后，再 git stash pop，回到工作现场；
  git stash
  git stash pop
  git stash list
  git stash apply
  git stash drop

在 master 分支上修复的 bug，想要合并到当前 dev 分支，可以用 git cherry-pick <commit>命令，把 bug 提交的修改“复制”到当前分支，避免重复劳动。
  注意：我们只想复制4c805e2 fix bug 101这个提交所做的修改，并不是把整个master分支merge过来。
  为了方便操作，Git专门提供了一个cherry-pick命令，让我们能复制一个特定的提交到当前分支
```


## feature分支
```markdown
每添加一个新功能，最好新建一个feature分支，在上面开发，完成后，合并，最后，删除该feature分支。

如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除。
```


## 多人协作
```markdown
master分支是主分支，因此要时刻与远程同步；
dev分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步；
bug分支只用于在本地修复bug，就没必要推到远程了，除非老板要看看你每周到底修复了几个bug；
feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。
```


```markdown
# 本地新建的分支如果不推送到远程，对其他人就是不可见的；
git remote -v

推送分支
  推送时，要指定本地分支，这样，Git就会把该分支推送到远程库对应的远程分支上：
    git push origin master
    git push origin dev

当你的小伙伴从远程库clone时，默认情况下，你的小伙伴只能看到本地的master分支
  git branch
解决办法：要在dev分支上开发，就必须创建远程origin的dev分支到本地
  git checkout -b dev origin/dev

你的小伙伴已经向origin/dev分支推送了他的提交，而碰巧你也对同样的文件作了修改，并试图推送；推送失败，因为你的小伙伴的最新提交和你试图推送的提交有冲突。
解决办法：先用git pull把最新的提交从origin/dev抓下来，然后，在本地合并，解决冲突，再推送：
  第一步：指定本地dev分支与远程origin/dev分支的链接；否则 git pull 失败
    git branch --set-upstream-to=origin/dev dev
  第二步：在 git pull后，合并有冲突，需要手动解决，解决的方法和分支管理中的解决冲突完全一样。解决后，提交，再push；
    git pull
  // 上述可以两步可以简写成 git pull origin dev;自动将 远程仓库中的dev分支 与当前分支(git branch查看的) 进行合并
```


## rebase | 衍合过程
```markdown
// https://www.cnblogs.com/pinefantasy/articles/6287147.html

可以看出merge结果能够体现出时间线，但是rebase会打乱时间线。
而rebase看起来简洁，但是merge看起来不太简洁。
最终结果是都把代码合起来了，所以具体怎么使用这两个命令看项目需要。

git pull相当于是git fetch + git merge;
如果此时运行git pull -r，也就是git pull --rebase，相当于git fetch + git rebase


rebase操作可以把本地 未push 的分叉提交历史整理成直线；
rebase的目的是使得我们在查看历史提交的变化时更容易，因为分叉的提交需要三方对比。

// 合并commit
衍合的风险，请务必遵循如下准则：
一旦分支中的提交对象发布到公共仓库，就千万不要对该分支进行衍合操作。
// 因为rebase操作会将历史commit 合并成一次commit。这样回滚的时候，就会有问题
```




# 标签
```markdown
// 注意：标签总是和某个commit挂钩。如果这个commit既出现在master分支，又出现在dev分支，那么在这两个分支上都可以看到这个标签。

通常先在版本库中打一个标签（tag），这样，就唯一确定了打标签时刻的版本
tag就是一个让人容易记住的有意义的名字，它跟某个commit绑在一起。

指向某个commit的指针（跟分支很像对不对？但是分支可以移动，标签不能移动），


git tag
  查看所有标签：
git tag <name> <commit id?>
  打一个新标签;默认为HEAD，也可以指定一个commit id
  还可以创建带有说明的标签，用-a指定标签名，-m指定说明文字：
    $ git tag -a v0.1 -m "version 0.1 released" 1094adb
git show <tagname>
  查看标签信息


git tag -d <tagname>
  删除本地标签
git push origin :refs/tags/<tagname>
  删除远程标签就麻烦一点，先从本地删除；然后再执行上述命令

git push origin <tagname>
  推送某个标签到远程
git push origin --tags
  一次性推送全部尚未推送到远程的本地标签
git push origin master --tags 
  把master分支中的全部标签 推送到远程仓库

git ls-remote --tags origin
  参看远程仓库中的tag
```

# Gitee
```markdown
git init
git remote -v
git remote rm origin // 默认远程包

git remote add github ...
git remote add gitee ...

git remote -v

git push github master
git push gitee master
```

# 自定义Git
## .gitignore文件
```markdown
- 忽略操作系统自动生成的文件，比如缩略图等；
- 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的.class文件；
- 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。


有些时候，你想添加一个文件到Git，但发现添加不了，原因是这个文件被.gitignore忽略了：
  git add -f App.class
    用-f强制添加到Git：
  git check-ignore -v App.class
    用来检查到底哪个规则写错了：

注意事项：
  注释"#"开头
  "!"排除有些文件

```




```.gitignore
# Windows:
Thumbs.db
ehthumbs.db
Desktop.ini

# Python:
*.py[cod]
*.so
*.egg
*.egg-info
dist
build

# My configurations:
db.ini
deploy_key_rsa

# 排除所有.开头的隐藏文件:
.*
# 排除所有.class文件:
*.class

# 不排除.gitignore和App.class:
!.gitignore
!App.class

```



## 配置别名
```markdown
# 命令行添加
  git config --global alias.st status

# 配置文件
局部配置
  每个仓库的Git配置文件都放在.git/config文件中：
全局配置
  而当前用户的Git配置文件放在用户主目录下的一个隐藏文件.gitconfig中：

```

