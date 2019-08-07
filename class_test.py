class People:
# self points to the object
    def set_name(self, name):
        self.name = name
    def get_name(self, name):
        return self.name
    def greeting(self):
        print(self.name)
        print("Hello, world! I'm {}.".format(self.name))
# define bar and foo as classs
bar = People()
foo = People()
name1 = input("Please input name of player 1: \n")
name2 = input("Please input name of player 2: \n")
bar.set_name(name1)
foo.set_name(name2)
bar.greeting()
foo.greeting()
