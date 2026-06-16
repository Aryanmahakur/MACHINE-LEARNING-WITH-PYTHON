class animal:
    def voice(self):
        print("animal make a voice")

class dog(animal):
 pass

class cat(dog):
   lists=[1,2,3,4,5]
   for i in lists:
      print(i);
   def voice(self):
      print("cat is making voices")
answer=cat()
answer.voice();
