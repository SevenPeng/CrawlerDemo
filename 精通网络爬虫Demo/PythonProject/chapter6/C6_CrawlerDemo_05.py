# 多线程基础
import threading


class A(threading.Thread):
    def __init__(self):
        # 初始化该线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容
        for i in range(100):
            print("我是线程A")


class B(threading.Thread):
    def __init__(self):
        # 初始化该线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容
        for i in range(100):
            print("我是线程B")


class C(threading.Thread):
    def __init__(self):
        # 初始化该线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容
        for i in range(100):
            print("我是线程C")


class D(threading.Thread):
    def __init__(self):
        # 初始化该线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容
        for i in range(100):
            print("我是线程D")


# 实例化线程A为t1
t1 = A()
# 启动线程t1
t1.start()
# 实例化线程B为t2
t2 = B()
# 启动线程t2
t2.start()
# 实例化线程C为t3
t3 = C()
# 启动线程t3
t3.start()
# 实例化线程D为t4
t4 = D()
# 启动线程t4
t4.start()
