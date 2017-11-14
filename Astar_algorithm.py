
import math

romania_map_location = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Dobreta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesi=(320, 368), RimnicuVilcea=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))



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

def ASTAR(start,destination):

       parent = {}
       hurestic_cost = {}
       hurestic_cost[start] = math.sqrt((romania_map_location[start][0]-romania_map_location[destination][0])**2 + (romania_map_location[start][1]-romania_map_location[destination][1])**2)
       cost = {}
       cost[start] = 0
       visited={}
       visited[start]=1

       temp = start
       #print("cost is: ",cost)

       while temp !=None:
           print("temp is: ",temp)
           if temp==destination:
               break

           for i in romania_map[temp]:

                   if cost.get(i, 0) == 0:
                       cost[i] = cost[temp] + romania_map[temp][i]
                       temp_cost = math.sqrt((romania_map_location[i][0] - romania_map_location[destination][0]) ** 2 + (romania_map_location[i][1] - romania_map_location[destination][1]) ** 2)
                       hurestic_cost[i] = cost[i] + temp_cost
                       parent[i] = temp

                   elif cost[i] > cost[temp] + romania_map[temp][i]:
                       cost[i] = cost[temp] + romania_map[temp][i]
                       temp_cost = math.sqrt((romania_map_location[i][0] - romania_map_location[destination][0]) ** 2 + (romania_map_location[i][1] - romania_map_location[destination][1]) ** 2)
                       hurestic_cost[i] = cost[i] + temp_cost
                       parent[i] = temp
                       visited[i]=0
                       
                       
           now = sorted(hurestic_cost.items(), key=lambda x: x[1])
         

           temp=None
           for i in now:
               if visited.get(i[0], 0) == 0:
                   temp = i[0]
                   visited[temp]=1
                   break

       print("length is: ", len(cost))
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

ASTAR(start,destination)


