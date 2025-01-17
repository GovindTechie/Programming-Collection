import java.util.*;
import java.math.BigInteger;

 // Compiler version JDK 11.0.2

 public class Dcoder
 {
   public static void main(String args[])
   {
     BigInteger a = new BigInteger("0");
     BigInteger b = new BigInteger("1");
     BigInteger c;
     long n=20L,i; 
     System.out.println("Fibonacci term "+1+" is :0");
     System.out.println("Fibonacci term "+2+" is :1");
     for(i=3;i<=n;i++){
     c=a.add(b);
     a=b;
     b=c;
    System.out.println("Fibonacci term "+i+" is :"+c);
   }
   }
 }
