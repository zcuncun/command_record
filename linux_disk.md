
# 挂载新磁盘
## get DISKPATH

sudo fdisk -l

## get UUID

sudo blkid  [DISKPATH]

## add

mkdir /export

sudo vim /etc/fstab

UUID=[UUDI] /export ext4 defaults 0 0

## 在files展示

edit ~/.config/gtk-3.0/bookmarks


# 批量删除username的文件，用正则筛选

ls -la | grep username | grep -P 'vscode.*?.sock' -o | xargs -d"\n" rm
