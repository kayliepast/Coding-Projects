/**
 * Rock, paper, scissors 
 * Plays a single round of human vs. computer
 * 
 * CMS 121
 */

import java.util.Scanner;

public class RockPaperScissors {
	
    public static void main(String[] args) {
        // 1. Declare final variables representing the three moves
        final int ROCK = 1;
        final int PAPER = 2;
        final int SCISSORS = 3;
        
        // 2. Create a new Scanner
        Scanner input = new Scanner(System.in);
        
        //3. Print the welcome message and list the three moves
        System.out.println("Welcome to Rock, Paper, Scissors!");
        System.out.println("Choose your move:");
        System.out.println("1 - Rock");
        System.out.println("2 - Paper");
        System.out.println("3 - Scissors");
        
        // 4. Read the player's move
        System.out.println("Enter your choice (1, 2, or 3): ");
        int playerMove = input.nextInt();
        
        // 5. Check for valid input
        if (playerMove < 1 || playerMove > 3) {
            System.out.println("That's not a valid move, meatbag.");
            return;
        }
        
        // 6. Randomly generate the CPU's move
        int cpuMove;
        double r = Math.random();
        if (r < 0.3333) {
            cpuMove = ROCK;
        } else if (r < 0.6666) {
            cpuMove = PAPER;
        } else {
            cpuMove = SCISSORS;
        }
        
        // 7. Print CPU's move
        if (cpuMove == ROCK) {
            System.out.println("I choose Rock.");
        } else if (cpuMove == PAPER) {
            System.out.println("I choose Paper.");
        } else {
            System.out.println("I choose Scissors.");
        }
        
        // 8. Determine the outcome
        if (playerMove == cpuMove) {
            System.out.println("Draw! I'll get you next time, human.");
        } else if (playerMove == ROCK && cpuMove == PAPER) {
            System.out.println("Paper covers Rock!");
            System.out.println("Humans...so soft...so weak.");
        } else if (playerMove == PAPER && cpuMove == SCISSORS) {
            System.out.println("Scissors cut Paper!");
            System.out.println("You're so easy to beat.");
        } else if (playerMove == SCISSORS && cpuMove == ROCK) {
            System.out.println("Rock smashes Scissors!");
            System.out.println("I knew I would win");
        } else {
            System.out.println("You win this round...but we'll see who wins next time!");
        }
        
        // Close the scanner
        input.close();
    }
}
