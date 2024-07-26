import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

public class Q2 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the no of vertices");
		int numVertices=sc.nextInt();
		sc.nextLine();
		System.out.println("Enter the graph: ");
		Map<Integer,Map<Integer,Integer>>graph=new HashMap<>();
		for (int i=0;i<numVertices;i++) {
			String line=sc.nextLine();
			line=line.substring(1,line.length()-1);
			String[] parts =line.split(", ");
			Map<Integer, Integer> neighbors =new HashMap<>();
			for(String part:parts) {
				String[] neighborParts=part.split(": ");
				int neighbor=Integer.parseInt(neighborParts[0]);
				int weight=Integer.parseInt(neighborParts[1]);
				neighbors.put(neighbor, weight);
				
			}
			graph.put(i, neighbors);
			
		}
		System.out.println("Enter the source vertex:");
		int sourcevertex=sc.nextInt();
		Map<Integer,Integer> shortestPaths=dijk(graph,sourcevertex);
		System.out.println("Shortest paths from source vertex: "+sourcevertex+":");
		System.out.println(shortestPaths);
	}
	public static Map<Integer, Integer>dijk(Map<Integer, Map<Integer, Integer>>graph, int sourcevertex){
		Map<Integer,Integer> distances=new HashMap<>();
		Set<Integer> visited=new HashSet<>();
		PriorityQueue<Node> priorityQueue=new PriorityQueue<>(Comparator.comparingInt(n -> n.distance));
		for(Integer vertx:graph.keySet()) {
			distances.put(vertx, Integer.MAX_VALUE);
		}
		distances.put(sourcevertex,0);
		priorityQueue.add(new Node(sourcevertex,0));
		
		while(!priorityQueue.isEmpty()) {
			Node current=priorityQueue.poll();
			if(visited.contains(current.vertex)) {
				continue;
				
			}
			visited.add(current.vertex);
			for(Map.Entry<Integer, Integer>neighborEntry:graph.get(current.vertex).entrySet()) {
				int neighbor=neighborEntry.getKey();
				int weight=neighborEntry.getValue();
				if(distances.get(current.vertex)+weight<distances.get(neighbor)) {
					distances.put(neighbor, distances.get(current.vertex)+weight);
					priorityQueue.add(new Node(neighbor,distances.get(neighbor)));
				}
			}
		}
		return distances;
	}
	static class Node{
		int vertex;
		int distance;
		public Node(int vertex,int distance) {
			this.vertex=vertex;
			this.distance=distance;
		}
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

}
