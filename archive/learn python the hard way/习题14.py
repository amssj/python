from sys import argv

script, user_name, major, supervisor = argv

prompt = " >"

print(f"Hi, welcome you to Uva {user_name}")
print("I'd like to ask you a few questions. Are you ready?")
input(prompt)
print(f"Do you like your {user_name}?")
likes = input(prompt)
print(f"I heard your supervisor is {supervisor}, do you see him a lot?")
frequency = int(input(prompt))
print(f"Your major is {major},it is an interesting field,what you will learn?")
things = input(prompt)

print(f"""
So, {user_name},thanks for the information, 
you have a great supervisor and you visited him {frequency} times a semester,
your major is also interesting,
you told me you will learn {things},
Nice.""")
