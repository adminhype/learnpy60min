todos = ['Apfel', 'Banane']

for _ in range(10000):
    newItem = input("Was möchtest du hinzufügen? ")
    todos.append(newItem)
    print("Meine Liste hat diese Elemente: ")

    for todo in todos:
        print(f"- {todo}")


print("Programm beendet.")