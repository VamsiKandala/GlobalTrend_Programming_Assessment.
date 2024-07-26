import java.util.Scanner;

public class Q1 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the str1: ");
		String str1=sc.nextLine();
		System.out.println("Enter the str2: ");
		String str2=sc.nextLine();
		int length=lcs(str1,str2);
		System.out.println("The LCS is : "+length);
		

	}
	public static int lcs(String str1, String str2) {
		int n=str1.length();
		int m=str2.length();
		int [][] tb=new int[n+1][m+1];
		for (int i=0;i<=n;i++) {
			for(int j=0;j<=m;j++) {
				if(i==0||j==0) {
					tb[i][j]=0;
				}
				else if(str1.charAt(i-1)==str2.charAt(j-1)) {
					tb[i][j]=tb[i-1][j-1]+1;
				}
				else {
					tb[i][j]=Math.max(tb[i-1][j],tb[i][j-1]);
				}
			}
		}
	return tb[n][m];
	}

}
