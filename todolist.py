todos = ['Apfel', 'Banane']


newItem = input("Was möchtest du hinzufügen? ")
todos.append(newItem)
print("Meine Liste hat diese Elemente: ")

for todo in todos:
    print(f"- {todo}")


print("Programm beendet.")