import sys

def graph_from(n,line):
    graph = {}
    for node in range(1,n+1):
        graph[node] = []
        for li in line:
            if node in li:
                if li.index(node) == 0:
                    graph[node].append(li[1])
                else:
                    graph[node].append(li[0])
                    
    form = [len(i) for i in graph.values()]
    form.sort()
    return form
    

n1, m1 = map(int,sys.stdin.readline().split())
line1 = [list(map(int,sys.stdin.readline().split())) for i in range(m1)]
n2, m2 = map(int,sys.stdin.readline().split())
line2 = [list(map(int,sys.stdin.readline().split())) for i in range(m2)]

if graph_from(n1,line1) == graph_from(n2,line2):
    print('YES')
else:
    print('NO')