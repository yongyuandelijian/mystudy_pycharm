# 20171110
print('my name is lpc');

# declare list
myList=[1,2,3,4];
# declare tuple
myTuple=(1,2,myList);

print('列表是',myList,'元组是',myTuple);

myList.append('23');
print('修改后列表是',myList,'元组是',myTuple);

list1=myList[2:30];
print('切片月截止后',list1);  #  切片月结之后不会存在报错情况，能获取到返回对应的元素，不能获取到返回空

# tuple1 =myTuple[1,3];
# print('元组切片',tuple1)


