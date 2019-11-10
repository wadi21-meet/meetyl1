class User():
	def __init__(self, name, email, password, friends_list=[],posts=[]):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self, email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as a friend")
	def remove_friend(self, email):
		self.friends_list.remove(email)
		print(self.name + " has removed " + email + " from his friends list")
	def post(self, text):
		self.text = text
		self.posts.append(text)
		print(self.name + " has posted: " + text)
	def get_userInfo(self):
		print("Name: " + self.name)
		print("Email: " + self.email)
		print("Password: " + self.password) 
		print("Friends: ", self.friends_list)
		print("Posts: ", self.posts)
user1 = User("Wadi", "wnaoum@gmail.com", "mycoolamazingpassword4354")
user2 = User("BeastMaster64", "BeastMaster64@gmail.com", "BeastMode123")
user2.add_friend("wnaoum@gmail.com")
user1.post("text")
user1.get_userInfo()
user2.get_userInfo()
user2.remove_friend("wnaoum@gmail.com")
