import java.util.*;

class Game {
  int random;
  int count;

  // Constructor
  Game() {
    Random rand = new Random();
    random = rand.nextInt(100);
  }

  void play() {
    Scanner sc = new Scanner(System.in);
    System.out.println("Please enter a number that you guess");
    int your = sc.nextInt();
    count++;
    if (your == random) {
      
     System.out.println("Correct! You guessed in " + count + " times");
   System.out.println("random is "+ random);
    } else if (your > random) {
      System.out.println("Your number is greater");
      play();
    } else {
      System.out.println("Your number is less");
      play();
    }
  }
}

public class Main {
  public static void main(String args[]) {
    System.out.println("Welcome to Game");
    Game a = new Game();
    a.play();
  }
}