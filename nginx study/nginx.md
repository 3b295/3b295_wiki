# connection
对TCP连接的封装 *ngx_connection_t结构体*

### 最大并发量
**worker_connections**
每个worker进程所能建立连接的最大值   

1. 对于HTTP请求本地资源来说，能够支持的最大并发数量是worker_connections * worker_processes
2. 是HTTP作为反向代理来说，最大并发数量应该是worker_connections * worker_processes/2。因为作为反向代理服务器，每个并发会建立与客户端的连接和与后端服务的连接，会占用两个连接

# request
**ngx_http_request_t** 保存 解析请求和响应输出相关的数据  
行请求头会保存在ngx_http_request_t的域headers_in


# 常用配置
## 变量
1. 类似php的写法。
2. Nginx 变量值容器的生命期是与当前正在处理的请求绑定的，而与 location 无关(有别于一般编程语言的作用域)
## 内建变量
类似$arg_xxx $cookie_xxx  并非预先加载好。而是惰性的获取。
