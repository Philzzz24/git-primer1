from datetime import datetime

name =  input("What is your name? ")
hour = datetime.now().time.hour
greetings = greeting = "Good morning" if 4 <= hour < 12 else "Good afterno"
print(f"Hello, {name}!"


