# csv 文件操作工具
import csv
# import codecs

# 将数据写入csv
def write_csvFile(path,head,data):
    try:
        with open(path,"w",newline="",encoding="utf-8-sig") as csvFile:  # 制定编码，否则会提示编码不匹配
            writer=csv.writer(csvFile,dialect='excel')
            if head is not None:
                writer.writerow(head)  # 这东西报错
            for row in data:
                writer.writerow(row)
            print("写入CSV文件成功，路径是%s"%path)
    except Exception as e:
        print("写入CSV失败\n",e)
    finally:
        csvFile.close()

