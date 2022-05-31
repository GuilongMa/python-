"""
一个图用字典表示，一个节点对应一个映射关系比如graph["you"] = ["Jhon", "Amy"],即you指向Jhon和Amy
工作原理：含图边加权值的最短路径
"""


def dkstl(graph, cost, parents):
    processed = []
    node = find_lowest_cost_node(cost, processed)
    while node is not None:
        neighbors = graph[node]
        for child_node in neighbors:
            new_cost = cost[node] + neighbors[child_node]
            if cost[child_node] > new_cost:
                cost[child_node] = new_cost
                parents[child_node] = node
        processed.append(node)
        node = find_lowest_cost_node(cost, processed)
    path = ["fin"]
    node = parents.get("fin")
    while node:
        path.insert(0, node)
        node = parents.get(node)

    path_str = '-'.join(path)
    return path_str, cost["fin"]


def find_lowest_cost_node(cost, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in cost:
        cost_num = cost[node]
        if cost_num < lowest_cost and node not in processed:
            lowest_cost = cost_num
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == "__main__":
    graph = {}
    graph["start"] = {"Amy": 5, "Bob": 0}
    graph["Amy"] = {"Jhon": 15, "Mike": 20}
    graph["Bob"] = {"Jhon": 30, "Mike": 35}
    graph["Jhon"] = {"fin": 20}
    graph["Mike"] = {"fin": 10}
    graph["fin"] = {}

    cost = {}
    infinity = float("inf")
    cost["Amy"] = 5
    cost["Bob"] = 0
    cost["Jhon"] = infinity
    cost["Mike"] = infinity
    cost["fin"] = infinity

    parents = {}
    parents["Amy"] = "start"
    parents["Bob"] = "start"
    parents["Jhon"] = None
    parents["Mike"] = None
    parents["fin"] = None
    print(dkstl(graph, cost, parents))
