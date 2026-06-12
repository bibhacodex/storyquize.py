
print("THE HONEST WOODCUTTER")
name=input("Enter your name: ")
print("Hellow!",name)
print(name,"you are a woodcutter.")
print("One day your iron axe fall into a river.")
print("A appear goddness and show you an axe")
print("Is gold your axe?")
choice=input("""
A. Yes
B. No
_____""")
if choice=="a":
       print("you lied to the goddness")
elif choice=="b":
       print("Is silver you axe?")
       choice=input("""
 A. Yes
 B. No
 _______
 """)
       if choice=="a":
              print("you lied to the goddness")
       elif choice=="b":
              print("Is iron your axe?")
              choice=input("""
  A. Yes
 B. No
 ______
  """)
              if choice=="a":
                     print("you are honest")
                     print("you won!")
              elif choice=="b":
                     print("you lose!")

else:
       print("Ivalid choice")
       print("Try again")



print("_______________________")
print("complete")
       