
# get DISKPATH

sudo fdisk -l

# get UUID

sudo blkid  [DISKPATH]

# add

mkdir /export

sudo vim /etc/fstab

UUID=[UUDI] /export ext4 defaults 0 0

# 在files展示

edit ~/.config/gtk-3.0/bookmarks
