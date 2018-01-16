from types import MethodType
def set_age(self,age):
	self.age = age
class Student(object):
	pass
# 这个MethodType用于将一个外部方法连接到一个实例对象或者类对象
# 连接到实例就只对该实例起作用
# 连接到类就是类方法，操作类属性

# 第一种情况
s1 = Student()
# 给s创建一个方法，把外部的set_age方法链接到Student内
# 这个方法只有s有，Student 类的其他实例没有
s1.set_age = MethodType(set_age,s1)
s1.set_age(25)
s2 = Student()
# 给s创建一个方法，把外部的set_age方法链接到Student内
# 这个方法只有s有，Student 类的其他实例没有
s2.set_age = MethodType(set_age,s2)
s2.set_age(18)
print(s1.age,s2.age)

'''
# 第二种情况
Student.set_age = MethodType(set_age,Student)
s1 = Student()
s2 = Student()
s1.set_age(25)
s2.set_age(18)
Student.set_age(17)
print(s1.age,s2.age)
'''