print(f" {"Topic: Python_Graphs - Adjacency List"} ".center(90, '-'))

graph = {
    "A" : ["B", "C"],
    "B" : ["A", "D"],
    "C" : ["A", "D"],
    "D" : ["B", "C"]
}

graph["E"] = []
graph["D"].append("E")
graph["E"].append("D")