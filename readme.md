# Mirage-Web开发包
## 说明
本开发包适用于中小型个人或企业网站前后台的开发。

开发包使用前后端分离开发理念，可以最大程度的支持前后端技术人员并行开发，降低开发成本和周期。

开发包前端基于vue，uikit，打包环境使用webpack，可以挂载于任何支持反向代理功能的主流webserver上,推荐使用nginx。

开发包后端基于python，使用flask作为api框架，orm为mongo-engine，后台数据库为mongodb。

可选的基于异步事件驱动支撑的网络驱动框架，后台api可以支撑大流量的并发长连接，除应用于普通展示性网站和页面之外，亦适用于需要处理大量长连接场合的后台系统，如在线咨询，物联网后台，即时通讯系统等等。

本开发包可部署于实体主机，云主机，或者-按照本文提示，部署于docker集群之上。


# 部署说明
## 编译准备
### 环境
编译和部署环境为安装了最新版本docker及docker-compose的linux主机，建议使用ubuntu，centos不推荐使用。

### 代码修改
将webapi/run.py中mongodb的host地址和端和口改为实际使用的地址。这里为：
```py
app.config['MONGODB_HOST'] = "mongo"
app.config['MONGODB_PORT'] = 27017
```
>这里使用未启用auth的mongodb，实际生产环境中，建议开启auth。

修改debug代码为实际运行代码：
```py
log.info('running...')
#app.run(debug=True, host='0.0.0.0')

http = WSGIServer(('', 5000), app)
http.serve_forever()
```

将webui/src/common/common.js中的api地址改为将要部署的api实际地址。这里为：
```js
var APIRoot = '//webapi:5000/api/'
```

将mirage.conf中的前端文件夹和api地址修改为将要部署的实际值。这里为：
```ini
root   /srv/mirage;
...
proxy_pass          http://webapi:5000/api/;
```

## 编译
### webapi
到webapi/build中执行：
```
build-docker.sh
build-webapi.sh
```

### webui
到webui中执行：
```
build.sh
```

## 部署

### 编译后的文件
- 将生成的webapi.tgz复制到部署文件夹并解压。
- 将生成的webui.tgz复制到部署文件夹并解压。

### 配置文件
- 复制mirage.conf到部署文件夹。
- 复制docker-compose.yml.deploy到部署文件夹并改名为docker-compose.yml。

### 运行

到部署文件夹，执行：
```
docker-compose up -d
```

等待脚本准备执行完毕并运行，即可访问网站查看效果，网站地址为：
http://ip:8080
其中ip为部署主机的地址。

系统内置三个账户，分别为：
admin/password
master/password
user/password
