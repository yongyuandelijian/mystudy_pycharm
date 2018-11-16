# 写入记事本的方法,返回写入结果,重复写入的时候，我们使用列表追加，所以每次追加原来的内容，重新写入的时候将原内容清空
def writeFile(path,content):
    result=''
    try:
        file = open(file=path, mode='w+',encoding='utf-8')
        file.write(content)
        result='1'
        print("write sucess", file.name)

    except Exception as e:
        result = '2'
        print("write failed", e)
    finally:
        file.close()
    return result


# 读取记事本的方法,返回读取的内容；  r 只读  w 写，文件存在的话，清空文件在写入  a 追加，如果文件不存在就创建文件  添加+的话，就是全部增加读写的功能
def readFile(path):
    try:
        file=open(file=path,mode='r+',encoding='utf-8')
        readstr=file.read()
        # print("读取的内容是:\n",readstr)
    except Exception as e:
        print("read failed!!!!",e)
    finally:
        file.close()
    return readstr
