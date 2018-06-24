import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class arraysum {

    static int simpleArraySum(int[] ar) {
    int sum = 0;
    for(int i:ar){
    sum = sum+i;
    }
   System.out.println(sum);
    return sum;
    }

    

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {


        int[] arc = {
        100,200,300,
        400,500,600
        };
        arraysum s = new arraysum();
        int ss = s.simpleArraySum(arc);
    }
}
