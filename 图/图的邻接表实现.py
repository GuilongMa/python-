from queue import Queue


class Graph(object):
    def __init__(self, v=0):
        self.v = v
        self.adj = []
        if self.v:
            for i in range(self.v):
                self.adj.append([])
        self.found = False

    def add_edge(self, s, t):
        self.adj[s].append(t)
        self.adj[t].append(s)

    # 是最短路径的一种,时间复杂度为O(E),E为边的个数，空间复杂度为O(V),V为节点个数
    def bfs(self, s, t):
        if s == t:
            return
        visited = [None] * self.v
        visited[s] = True
        q = Queue()
        q.put(s)
        prev = [-1] * self.v
        while not q.empty():
            cur = q.get()
            for i in range(len(self.adj[cur])):
                element = self.adj[cur][i]
                if not visited[element]:
                    prev[element] = cur
                    if element == t:
                        self.print_(prev, s, t)
                        return
                    visited[element] = True
                    q.put(element)

    # 不一定是最短路径中的一种，时间复杂度为O(E),E为边的个数，空间复杂度为O(V),V为节点个数
    def dfs(self, s, t):
        self.found = False
        visited = [None] * self.v
        prev = [-1] * self.v
        self.recur_dfs(s, t, visited, prev)
        self.print_(prev, s, t)

    def recur_dfs(self, s, t, visited, prev):
        if self.found:
            return
        if s == t:
            self.found = True
            return
        visited[s] = True
        for i in range(len(self.adj[s])):
            element = self.adj[s][i]
            if not visited[element]:
                prev[element] = s
                self.recur_dfs(element, t, visited, prev)

    # 不一定是最短路径中的一种
    def dfs2(self, s, t):
        self.found = False
        visited = [None] * self.v
        prev = [-1] * self.v
        self.recur_dfs(s, t, visited, prev)
        self.print_(prev, s, t)

    # 自己实现
    def recur_dfs2(self, s, t, visited, prev):
        visited[s] = True
        for i in range(len(self.adj[s])):
            if self.found:
                return
            element = self.adj[s][i]
            if not visited[element]:
                prev[element] = s
                if element == t:
                    visited[element] = True
                    self.found = True
                    return
                self.recur_dfs(element, t, visited, prev)

    def print_(self, prev, s, t):
        if prev[t] != -1 and t != s:
            self.print_(prev, s, prev[t])
        print(str(t)+" ")

    # s的num度好友
    def bfs_get_friend(self, s, num):
        q = Queue()
        q.put(s)
        friend_lists = []
        count = 0
        while not q.empty():
            if count > num:
                break
            size = q.qsize()
            friend_list = []
            for i in range(size):
                element = q.get()
                if element != s and element not in friend_list:
                    friend_list.append(element)
                for j in range(len(self.adj[element])):
                    q.put(self.adj[element][j])
            if friend_list:
                friend_lists.append(friend_list)
            count += 1
        return friend_lists

    def dfs_get_friend(self, s, num):
        pass


if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(3, 5)
    graph.add_edge(4, 1)
    graph.add_edge(4, 5)
    graph.bfs(0, 5)
    graph.dfs(0, 5)
    print(graph.bfs_get_friend(3, 3))








