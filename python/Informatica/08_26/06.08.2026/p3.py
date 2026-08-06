print(f" {"Topic: Python_Graphs - Adjacency Matrix"} ".center(90, '-'))

graph = {
    "A": ["B"],
    "B": ["A"]
}

graph["C"] = []
graph["A"].append("C")
graph["C"].append("A")