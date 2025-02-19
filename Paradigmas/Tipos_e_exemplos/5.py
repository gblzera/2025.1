import threading

def tarefa():
    print("Executing in parallel")

t = threading.Thread(target=tarefa)
t.start()
t.join()