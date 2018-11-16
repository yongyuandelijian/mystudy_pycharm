import types

# 获取对象的类型
# print(abs(-2323))

# print(type(abs)==types.FunctionType)  # 函数类型      Builtin
# print(type(abs)==types.BuiltinFunctionType)
# print(type(abs)==types)

print(isinstance([1, 2, 3], (list, tuple)))  # 还可以判断是否为后面类型中的其中一个

# 获取一个对象的所有属性和方法  这个类似于linux中的man方法了，非常使用，可以直接查看和使用
print(dir([1,2,3]))