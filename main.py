class Student:
    # class initialization
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    # methods
    def change_name(self, name):
        self.name = str(name)
        print("\nMy name is name:", self.name)
    
    def change_age(self, age):
        self.age = int(age)
        print("I am", self.age,)
    
    def add_track(self, tracks):
        # 1. Insert the new track "UI/UX" into the list.
        # 2. len(self.tracks) returns the number of items in the array as the index(location) to add the new track.

        self.tracks.insert(len(self.tracks), tracks)
        print(self.tracks)
        
    def get_score(self):
        print("Score is:", self.score, "\n")

# Instance of the class -> Student
Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
