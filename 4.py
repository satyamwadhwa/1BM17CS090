class Student:
     def  __init__(self):
          self.sid=0
          self.age=0
          self.marks=0

     def put(self,sid,age,marks):
          self.sid=sid
          self.age=age
          self.marks=marks

     def val_marks(self):
          if self.marks in range(0,101):
               return True
          return False
     def val_age(self):
          if self.age>=20:
               return True
          return False
     def check_qualification(self):
          if self.marks>=65:
               return True
          return False

s=Student()
i=int(input("enter id:"))
a=int(input("enter age"))
m=int(input("enter marks"))
s.put(i,a,m)

if s.val_marks() and s.val_age():
     if s.check_qualification():
          print("admission granted!")

     else:
          print("not eligiible :(")

else:
     print("not eligiible :(")
