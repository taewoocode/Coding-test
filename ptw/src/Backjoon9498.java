import java.util.Scanner;

public class Backjoon9498 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner( System.in );

        int A = scanner.nextInt();

        if (90 >= A){
            System.out.println("A");
        }else if (80 >= A) {
            System.out.println("B");
        }else if (80 >= A) {
            System.out.println( "C" );
        }else if (80 >= A) {
            System.out.println( "D" );
        }else
            System.out.println("F");
    }
}
