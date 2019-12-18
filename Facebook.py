users = []
posts = []

class User():
	def __init__(self, name, email, password, friends_list=[]):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list=[]
	def add_friend(self, email):
		self.friends_list.append(email)
		print(self.name + " has added " + email + " as a friend")
	def remove_friend(self, email):
		self.friends_list.remove(email)
		print(self.name + " has removed " + email + " from his friends list")
	def add_post(self, text):
		post1 = Post(text, self.email)
		posts.append(post1)
		for post in posts:
			if user1.email == post.name:
				print(post)
		print(self.name + " has posted: " + text)
	def get_userInfo(self):
		print("Name: " + self.name)
		print("Email: " + self.email)
		print("Password: " + self.password) 
		print("Friends: ", self.friends_list)
		print("Posts: ", posts)


class Post():
	def __init__(self, name, caption, comments=[]):
		self.name = name
		self.caption = caption
		self.comments = []
	def add_caption(self, caption_text):
		self.caption_text = caption_text
		self.caption.append(caption_text)
		print(self.name + " has added the caption " + caption_text)
	def add_comment(self, comment_text):
		self.comment_text = comment_text
		self.comment.append(comment_text)
		print(self.name + " has added a comment: " + comment_text)
	def like_post(self):
		print(self.name + " has liked you post!")


class Comment(Post):
	pass

user1 = User("Wadi", "wnaoum@gmail.com", "mycoolamazingpassword4354")
user2 = User("BeastMaster64", "BeastMaster64@gmail.com", "BeastMode123")
user2.add_friend("wnaoum@gmail.com")
user1.add_post("text")
user1.get_userInfo()
user2.get_userInfo()
user2.remove_friend("wnaoum@gmail.com")
user1.add_post("my cool trip")
user2.add_post("amazing origami")



