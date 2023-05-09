#!/opt/homebrew/bin/python3
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name
d = Dog('Fido')
e = Dog('Buddy')
d.kind="Neel"
#d.kind.append('Venky')
#d.kind="Testing"
print(d.kind)
print(e.kind)
del d.kind
print(d.kind)
print(e.kind)