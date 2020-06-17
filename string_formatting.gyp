
name = input("Enter name: ")
surname = input("Enter surname: ")
when = "today"

message="Hello %s %s" % (name, surname)

message1 = f"Hello {name} {surname}! What's up {when}" 
print(message1)


def sum(a,b):
    a=a+b

print(sum(1,2))

