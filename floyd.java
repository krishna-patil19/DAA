import java.util.Scanner;
 public class Floyd_Warshall{
    final static int INF = 99999;
   public static void Floyd_Warshall (int graph[][],int V){
        int dist[][] = new int[V][V];
        
        for(int i = 0 ; i < V ; i++){
            
            for(int j = 0 ; j < V ; j++){
                
                dist[i][j] = graph[i][j];
            }
        }

        for(int k = 0 ; k < V ; k++){
            for(int i = 0 ; i < V ; i++){
                for(int j = 0 ; j < V ; j++){
                    if(dist[i][k] != INF && dist[k][j] != INF){
                        dist[i][j] = Math.min(dist[i][j],dist[i][k] + dist[k][j]);
                    }
                }
            }
        }

        displaysol(dist,V);
    }

  public static void displaysol(int dist[][],int V){
      
        System.out.println("The matrix with minimum distance is :");

        for(int i = 0 ; i < V ; i++){
            for(int j = 0 ; j < V ; j++){
                if(dist[i][j] == INF)
                System.out.print("INF");
                else
                System.out.print(dist[i][j] + " ");
            }
            System.out.println();
        }
    }
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of offices (vertices): ");
        int V = sc.nextInt();
        int graph[][] = new int[V][V];
        
        System.out.println("Enter the cost matrix (enter "+INF+" for no direct connection.)");
        

        for(int i = 0 ; i < V ; i++){
            
            for(int j = 0 ; j < V ; j++){
               
                graph[i][j] = sc.nextInt();
            }
        }
       
          Floyd_Warshall(graph, V);
    }
}
