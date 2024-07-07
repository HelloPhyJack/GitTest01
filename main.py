# 打印输出
print("Hello, World!")

# 变量和数据类型
name = "Alice"
age = 25
height = 1.65
is_student = True

# 条件语句
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# 循环
for i in range(5):
    print(i)

# 列表
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # 输出第一个元素

# 函数
def greet(name):
    print("Hello, " + name + "!")

greet("Bob")

# 类
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)

person = Person("Alice")
person.say_hello()