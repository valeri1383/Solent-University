class Child:
    def __init__(self, name, year, kind):
        self.name = name
        self.year = year
        self.kind = kind

    def __str__(self):
        return f"{self.name} -> {self.year} = {self.kind}"


class Family:
    def __init__(self):
        self.members = []

    def __str__(self):
        return " ".join([x.name for x in self.members])


child1 = Child("Emil", 2004, "homo-sapiens")
child2 = Child("Tobias", 2007, "human")
child3 = Child("Linus", 2011, "barbarian")

family = Family()

family.members.append(child1)
family.members.append(child2)
family.members.append(child3)

print(family)

for x in family.members:
    print(x)