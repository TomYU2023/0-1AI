# 函数的基础语法
def hello():
    print("hello world")
    print("hello python")

   # print("=======================这是函数的基础语法=======================")

# # 带参数的函数
# def Hello1(name):
#     print("hello",name)

#     Hello1("python") # 传入参数name
#     Hello1("java")
#     Hello1("c++")

#     print("=======================带参数的函数=======================")


def fn1(x, y):
    return x + y

if __name__ == '__main__': # 运行时执行，不会被调用到其他程序中
    print('__name__ is __main__')
    print(fn1(1, 2)) 
    # 注意缩进    
    print("=======================魔法方法__name__=======================")
        