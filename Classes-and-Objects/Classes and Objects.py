class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        print("New name is", self.name)

    def change_age(self, new_age):
        self.age = int(new_age)
        print("New age is", self.age)

    def add_track(self, new_track):
        added_track = self.tracks
        added_track.append(new_track)
        print(added_track)

    def get_score(self):
        print("Score is", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
