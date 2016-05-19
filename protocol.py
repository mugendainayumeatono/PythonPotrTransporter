#0                              16                               32
#|-------------------------------|-------------------------------|
#|0|1|2|3|4|5|6|7|8|9|a|b|c|d|e|f|0|1|2|3|4|5|6|7|8|9|a|b|c|d|e|f|
#|-------------------------------|-------------------------------|
#| 8 bit vision    | encrypt type|        head lengt             |
#|-------------------------------|-------------------------------|
#|                              head                             | 以上作为加密混淆头
#|-------------------------------|-------------------------------| 以下是通信协议
#|identification type            |         ket length            |
#|-------------------------------|-------------------------------|
#|                              key                              |
#|-------------------------------|-------------------------------|
#|  16 bit data length           |8 bit data type  |8 bit attach | 
#|-------------------------------|-------------------------------|
#|                              data                             |
#|-------------------------------|-------------------------------|
#
#
#----------------identification type ----------------------------
#0: 密码认证 key字段直接是密码
#1：密匙认证 客户端用私匙加密后的密码
#
#-------------------data type------------------------------------
#0x00： client-->service 申请 session id
#0x01： service-->client 分配 session id
#0x03： client-->service 请求执行一条命令
#0x04： service-->client 命令执行结果
#0x05： client-->service 请求上传文件 attach 前4bit 0:使用当前端口 1新开端口 后4bit 0：服务器发起连接 1：客户端发起连接
#0x06： client-->service 请求下载文件 attach 前4bit 0:使用当前端口 1新开端口 后4bit 0：服务器发起连接 1：客户端发起连接
#0x07： service-->client 可以开始传送数据 发送文件或转发数据前 客户端和服务端都要发送此数据 附带本地使用的端口
#0x08:  client-->service 请求端口转发 附带希望转发到远端的那个端口
#0x09:  
#
#
#客户端 申请新session id 附带上identification type 以及key
#
#
#
#
#
#
#
#
#
#
#
#
def unpackage(data):
    return "echo",data