from multiprocessing import Process
from threading import Thread,Lock
import time
import socket

# def dask(name):
#     print('%s is running' % name)
#     time.sleep(1)
#     print('%s is over' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=dask, args=('zhangs',))
#     t2 = Thread(target=dask, args=('ssss',))
#     t.daemon = True
#     t2.daemon =True
#     t.start()
#     t2.start()
#     print("主")

# class MyThead(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print('%s is running' % self.name)
#         time.sleep(1)
#         print('%s is over' % self.name)
#
#
# if __name__ == '__main__':
#     t = MyThead('egon')
#     t.start()
#     print('主')

"""
服务端：
1、要有固定的IP和PORT
2、24小时不间断提供服务
3、能够支持并发
"""

# server = socket.socket()  # 括号内不加参数默认就是TCP协议
# server.bind(('127.0.0.1', 8080))
# server.listen(5)
#
#
# #将服务的代码单独封装成一个函数
#
# def talk(conn):
#     # 通信循环
#     while True:
#         try:
#             data = conn.recv(1024)
#             # 针对mac lunux 客户端断开链接后
#             if len(data) == 0:
#                 break
#             print(data.decode('utf-8'))
#             conn.send(data.upper())
#
#         except ConnectionResetError as e:
#             print(e)
#             break
#     conn.close()
# # 链接循环：
# while True:
#     conn, address = server.accept()  #接客
#     # 叫其他人来服务
#     t = Thread(target=talk,args=(conn,))
#     t.start()


# money = 100
#
#
# def task():
#     global money
#     mutex.acquire()
#     tmp = money
#     money = tmp - 1
#     mutex.release()
#
#
# if __name__ == '__main__':
#     mutex = Lock()
#     t_list = []
#     for i in range(100):
#         t = Thread(target=task)
#         t.start()
#         t_list.append(t)
#
#     for t in t_list:
#         t.join()
#
#     print(money)
