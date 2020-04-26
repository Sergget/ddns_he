# DDNS for Hurricane Electrics
ddns for Hurricane Electrics free DNS written in python

## 关于HE免费DNS

- Free DNS:[https://dns.he.net/](https://dns.he.net/)
- 官方文档：[https://dns.he.net/docs.html](https://dns.he.net/docs.html)

## 基本实现
这只是一个简单的动态更新HE上的dns记录的python脚本，目前功能只能一次性的查询已有的一个域名空间内的所有记录，并通过[https://www.ipify.org](https://www.ipify.org)查询本机公网IP地址，再通过和HE上的记录进行比对，如果不同，则更新，否则不进行任何操作。

## 用法指南

请下载本目录下的python脚本并上传至服务器，修改配置文件。由于脚本没有进行循环，请自行在服务器上利用crontab等工具，根据自己的情况，设置刷新频率。

## config文件
1. 格式：json
2. 说明：
    - dynUrl: 字符串。默认为 `https://dyn.dns.he.net/nic/update?hostname=`
    - TLD: 字符串。顶级域名，如 `example.com`
    - names: 列表：
        - name：字符串。子域名名称，如填写 `sub` ，完整链接则为：`sub.example.com`
        - key：字符串。在[DNS页面](https://dns.he.net/)，进入编辑，点击`DDNS`下的刷新按钮以输入或者生成`key`。请注意，必须在DNS中添加域名且勾选 `Enable entry for dynamic dns` ，才能使用本脚本更新。
