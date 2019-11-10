class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!! " + self.name + " is eating " + food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self):
		print("bark, bark, bark")
animal1 = Animal(" bark "," Kyle "," 1001 "," 50 shades of black ")
animal1.eat(" pasta ")
animal1.description()
animal1.make_sound()

class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self):
		print("Yummy!! " + self.name + " is eating " + " his favorite breakfast")
	def table_flip(self):
		print(self.name + " is flipping tables")
person1 = Person("Jim","900000000","Jerusalem","Other")
person1.eat()
person1.table_flip()

class Bird(object):
	def __init__(self,name,color,speed):
		self.name = name
		self.color = color
		self.speed = speed
	def Get_Speed(self):
		print(self.name + " is going at a speed of " + self.speed)
	def Bite_Head(self):
		print(self.name + " is biting its head off")
bird1 = Bird("the Steve Jobs of birds","Bleen","1000000kmph")
bird1.Get_Speed()
bird1.Bite_Head()




