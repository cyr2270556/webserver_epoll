import re
from select import *
from socket import  *


class WebServer:
    def __init__(self,host='0.0.0.0',port=8888,html=None):
        self.host=host
        self.port=port
        self.html=html
        self.create_socket()
        self.bind()
        self.e=epoll()
        self.e.register(self.socket, EPOLLIN | EPOLLET)
        self.map = {self.socket.fileno(): self.socket}


    def create_socket(self):
        self.socket=socket()
        self.socket.setblocking(False)

    def bind(self):
        self.address=(self.host,self.port)
        self.socket.bind(self.address)

    def start(self):
        self.socket.listen(5)
        print(f'listen to the port{self.port}')
        while True:
            self.socket.setblocking(False)
            events = self.e.poll()
            print('你有新的io事件需要处理哦', events)
            for fd,event in events:
                if fd == self.socket.fileno():
                    connfd,addr=self.map[fd].accept()
                    print('connect from {}'.format(addr))
                    connfd.setblocking(False)
                    self.e.register(connfd,EPOLLIN|EPOLLET)
                    self.map[connfd.fileno()]=connfd

                else:
                    try:
                        self.handle(fd)
                    except:
                        self.e.unregister(fd)
                        self.map[fd].close()
                        del self.map[fd]

    def handle(self, fd):
        # 浏览器发送了HTTP请求
        request = self.map[fd].recv(1024 * 10).decode()
        print(request)
        pattern = "[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, request)  # match对象 None
        if result:
            info = result.group('info')  # 提取请求内容
            print("请求内容:", info)
            # 发送响应内容
            self.send_response(self.map[fd], info)
        else:
            # 没有获取请求断开客户端
            self.e.unregister(fd)
            self.map[fd].close()
            del self.map[fd]


    # 根据请求组织响应内容，发送给浏览器
    def send_response(self, fd, info):
        if info == '/':
            # 主页
            filename = self.html + "/index.html"
        else:
            filename = self.html + info

        try:
            fds = open(filename,'rb') # 有可能有文本还有图片
        except:
            # 请求的文件不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry....</h1>"
            response = response.encode()
        else:
            # 请求的文件存在
            data = fds.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n"%len(data) # 发送图片
            response += "\r\n"
            response =response.encode() + data # 转换字节拼接
        finally:
            # 给客户端发送响应
            fd.send(response)
if __name__ == '__main__':
    httpd=WebServer(host='0.0.0.0',port=8888,html='/home/tarena/static')
    httpd.start()