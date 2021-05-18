# 1.客户端生成公私钥

本地客户端生成公私钥：（一路回车默认即可）

```
ssh-keygen
```

# 2.上传公钥到服务器

```
ssh-copy-id -i ~/.ssh/id_rsa.pub [user]@[host]
```

