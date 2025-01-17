import java.util.*;

class Dcoder {
    public static void main(String args[]) { 
        int n = 12;
        for(int i = 1; i <=n; i++) {
            for(int j = 1; j <= 1; j++) {
                System.out.print("*");
            }
            
            for(int j = (i * 1 - 2); j >= 1; j--) {
                System.out.print(" ");
            }
            
            for(int j = i; j > (i - 1); j--) {
                if(j == 1) {
                    continue;
                }
                System.out.print("*");
            }
            
            int spaces = 2 * (n-i);
           for(int j=1; j<=spaces; j++) {
               System.out.print(" ");

           }
                       for(int j = 1; j <= 1; j++) {
                System.out.print("*");
            }
            
            for(int j = (i * 1 - 2); j >= 1; j--) {
                System.out.print(" ");
            }
            
            for(int j = i; j > (i - 1); j--) {
                if(j == 1) {
                    continue;
                }
                System.out.print("*");
            }
            
            System.out.println();
        }
        for(int i = n; i >=1; i--) {
            for(int j = 1; j <= 1; j++) {
                System.out.print("*");
            }
            
            for(int j = (i * 1 - 2); j >= 1; j--) {
                System.out.print(" ");
            }
            
            for(int j = i; j > (i - 1); j--) {
                if(j == 1) {
                    continue;
                }
                System.out.print("*");
            }
            
            int spaces = 2 * (n-i);
           for(int j=1; j<=spaces; j++) {
               System.out.print(" ");

           }
                       for(int j = 1; j <= 1; j++) {
                System.out.print("*");
            }
            
            for(int j = (i * 1 - 2); j >= 1; j--) {
                System.out.print(" ");
            }
            
            for(int j = i; j > (i - 1); j--) {
                if(j == 1) {
                    continue;
                }
                System.out.print("*");
            }
            
            System.out.println();
        }
    }
}