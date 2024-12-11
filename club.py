import math
from queue import PriorityQueue

class Node:
    def __init__(self, cost, level, assigned):
        self.cost = cost
        self.level = level
        self.assigned = assigned
    
    def __lt__(self, other):
        return self.cost < other.cost

def calculate_cost_matrix(cost_matrix):

    n = len(cost_matrix)
    
    pq = PriorityQueue()
    
    root = Node(cost=0, level=0, assigned=[-1] * n)
    pq.put(root)
    
    min_cost = math.inf
    min_assignment = []
    
    while not pq.empty():
        node = pq.get()
        
        if node.level == n:
            if node.cost < min_cost:
                min_cost = node.cost
                min_assignment = node.assigned.copy()
            continue
        
        for j in range(n):
            if j not in node.assigned:
                new_cost = node.cost + cost_matrix[node.level][j]
                new_assigned = node.assigned.copy()
                new_assigned[node.level] = j
                
                new_node = Node(cost=new_cost, level=node.level + 1, assigned=new_assigned)
                
                if new_cost < min_cost:
                    pq.put(new_node)
    
    return min_cost, min_assignment

def main():
    n = int(input("Enter the number of students (and clubs): "))
    
    cost_matrix = []
    print("Enter the cost matrix (row-wise):")
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        cost_matrix.append(row)
    
    min_cost, assignment = calculate_cost_matrix(cost_matrix)
    
    print("\nMinimum cost of assignment:", min_cost)
    print("Optimal assignment of students to clubs:")
    for i in range(len(assignment)):
        print(f"  Student {i + 1} -> Club {assignment[i] + 1}")

if __name__ == "__main__":
    main()
