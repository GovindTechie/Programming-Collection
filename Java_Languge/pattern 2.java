public class PascalTriangle {
    public static void main(String[] args) {
        int numRows = 5; // Change this value to print more or fewer rows

        for (int i = 1; i <= numRows; i++) {
            int number = 1;
            for (int j = 1; j <= numRows - i; j++) {
                System.out.print("  "); // Print spaces for formatting
            }
            for (int j = 1; j <= i; j++) {
                System.out.print(number + " ");
                number = number * (i - j) / j;
            }
            System.out.println();
        }
    }
}