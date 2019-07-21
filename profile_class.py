class Profile:
    def __init__(self, name, age, gender, hobby):
        self.name = name
        self.age = age
        self.gender = gender
        self.hobby = hobby
        self.stock = 0
        if age < 18:
            self.vote = False
        else:
            self.vote = True
        
#program begins below

profile1 = Profile("Rifat Roufe", 17, "female", "reading")
profile2 = Profile("Derek Stampone", 30, "male", "reading")
profiles = [profile1, profile2]
for profile in profiles:
    if profile.age < 18:
        print("You cannot vote")
    else:
        print("You are allowed to vote")

print(profile1)
print(profile1.name)
print(profile1.age)
print(profile1.gender)
print(profile1.hobby)
print(profile1.vote)
print("Name: " + profile1.name)