from xpinyin import Pinyin

def get_pinyin(hanzi,splitter):
    obj=Pinyin();
    return obj.get_pinyin(hanzi,splitter=splitter)

if __name__ == '__main__':
    hanzi=input("请输入要转为拼音的汉字")
    pinyin=get_pinyin(hanzi)
    print(pinyin)