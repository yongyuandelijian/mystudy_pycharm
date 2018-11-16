'''
def myexcept(x,y):
    try:
        a = x / y;
        print(a);
        return a
    except Exception as e: # 如果不想自己定义错误提示就可以通过as对象使用系统给的提示，也可以不用捕获对象，自己写一个
        print("程序异常，小丁很生气！！！",e)   # 如果不使用raise就只有这个指定的提示
        # raise;  # 如果使用raise那就会和系统报出来的一样，提示行和具体的提示信息,
    # except NameError:  当然也可以再次进行追加多个except
    #     print('多个except捕获异常！！！');
    # except(NameError,ZeroDivisionError,IOError):  当然也可以使用一个except捕获多个异常
    #     print("一个except捕获多个异常！！！")
    # except (NameError,ZeroDivisionError,IOError) as e:  当然也可以通过as 名称来获取一个异常的对象
    #     print(e);
    # except:
    #     print("捕捉所有的异常，这样做到好处就是可以防止有些异常不没有捕获到，坏处就是隐藏了所有的异常！！！")
    else:
        print("如果上面没有异常就走这个部分！！！"); # 好处就是可以更加细致的判断程序走向
    finally:
        print("无论是否异常，都需要走finally中的语句！！！");

myexcept(2,0);
'''



# raise NameError('这是一个名称错误异常');  直接输出异常的情况