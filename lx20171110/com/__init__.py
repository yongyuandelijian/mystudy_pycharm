class MyError(Exception):
    def __str__(self): # 在这里对这个函数有一点新的认识，觉得如果指定了变量就是没找到指定变量返回这个值，如果是没有指定那就是调用类就返回这个值
        return "没有找到字符串的时候就返回这个提示！！"

def my_error_test():
    try:
        raise MyError()
    except MyError as e:
        print(e)

my_error_test()