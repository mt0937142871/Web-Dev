class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last Name - " + self.last_name)
		print("Eye Color - " + self.eye_color)

billy_cyrus = Parent("Cyrus", "blue")


class Child(Parent):
	def __init__(self, last_name, eye_color, num_toys):
		print("Child Constructor Called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = num_toys

	def show_info(self):
		Parent.show_info(self)
		print("Num of Toys - " + str(self.number_of_toys))

miley_cyrus = Child("Cyrussss", "blueeeee", 10)

billy_cyrus.show_info()
miley_cyrus.show_info()