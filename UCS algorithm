# the main technique of UCS is expanding the node which has lowest value
# given a romanian city map as a dictionary with path cost.find lowest cost to reach destination from starting point. I used python to solve this problem

romania_map = {
   "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
   "Zerind": {"Arad": 75, "Oradea": 71},
   "Oradea": {"Zerind": 71, "Sibiu": 151},
   "Timisoara": {"Arad": 118, "Lugoj": 111},
   "Lugoj": {"Timisoara": 111, "Mehadia": 70},
   "Mehadia": {"Lugoj": 70, "Dobreta": 75},
   "Dobreta": {"Mehadia": 75, "Craiova": 120},
   "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138},
   "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu": 80},
   "Sibiu": {"Arad": 140, "Oradea": 151, "RimnicuVilcea": 80, "Fagaras": 99},
   "Fagaras": {"Sibiu": 99, "Bucharest": 211},
   "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138},
   "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
   "Giurgiu": {"Bucharest": 90},
   "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
   "Hirsova": {"Urziceni": 98, "Eforie": 86},
   "Eforie": {"Hirsova": 86},
   "Vaslui": {"Urziceni": 142, "Iasi": 92},
   "Iasi": {"Vaslui": 92, "Neamt": 87},
   "Neamt": {"Iasi": 87}
}

def ucs(start,destination):

       parent = {}
       cost = {}
       cost[start] = 0
       visited={}
       visited[start]=1

       temp = start
       #print("cost is: ",cost)

       while temp !=None:

           for i in romania_map[temp]:

                   if cost.get(i, 0) == 0:
                       cost[i] = cost[temp] + romania_map[temp][i]
                       parent[i] = temp

                   elif cost[i] > cost[temp] + romania_map[temp][i]:
                       cost[i] = cost[temp] + romania_map[temp][i]
                       parent[i] = temp
                       visited[i]=0
          # print(cost)
           now = sorted(cost.items(), key=lambda x: x[1])
          # print(now)

           temp=None
           for i in now:
               if visited.get(i[0], 0) == 0:
                   temp = i[0]
                   visited[temp]=1
                   break





       path = []
       path.append(destination)
       now = destination

       while True:

           path.append(parent[now])
           now = parent[now]

           if (now == start):
               break


       path.reverse()
       print("lowest costing path from ",start," to ",destination," is: ",path)
       print("cost is: ",cost[destination])



start = "Arad"
destination = "Bucharest"

ucs(start,destination)


