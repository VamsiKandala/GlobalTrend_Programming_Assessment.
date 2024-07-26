import java.util.Scanner;

public class Q3 {
	public static int knapsack(int[] weights, int[] values, int capacity) {
		int n=weights.length;
		int [][]dp=new int[n+1][capacity+1];
		for(int i=0;i<=n;i++) {
			dp[i][0]=0;
		}
		for(int j=0;j<=capacity;j++) {
			dp[0][j]=0;
			
		}
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=capacity;j++) {
				if(weights[i-1]>j) {
					dp[i][j]=dp[i-1][j];
				}
				else {
					dp[i][j]=Math.max(values[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j]);
				}
			}
		}
		return dp[n][capacity];
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the number of items: ");
		int n=sc.nextInt();
		System.out.println("Enter the weights : ");
		int [] weights=new int[n];
		for(int i=0;i<n;i++) {
			weights[i]=sc.nextInt();
			
		}
		System.out.println("Enter the values :");
		int [] values=new int[n];
		for(int i=0;i<n;i++) {
			values[i]=sc.nextInt();
			
		}
		System.out.println("Enter the knapsack capacity: ");
		int capacity=sc.nextInt();
		int maxval=knapsack(weights,values,capacity)-10;
		System.out.println("Maximum values : "+maxval);

	}

}
