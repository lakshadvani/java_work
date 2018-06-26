import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class diag {

    // Complete the diagonalDifference function below.

    static int diagonalDifference(int[][] ar) {  
    int d1 = 0;
    int d2 = 0;
    int n = ar.length;
    int sum = 0;
    int sum2 = 0;
    for(int i =0;i<n;i++)
    {
         for(int j =0;j<n;j++)
         {
         
         if(i==j)
         {
             sum = ar[i][j] + sum;
         }
         if(i == n-j-1)
         {
         sum2 = ar[i][j] + sum2;
         }
         
         
         }
    }
    int final_sum = 0;
    final_sum = Math.abs(sum-sum2);

    return final_sum;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[][] arr = new int[n][n];

        for (int i = 0; i < n; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < n; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int result = diagonalDifferaence(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
