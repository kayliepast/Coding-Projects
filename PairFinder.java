/**
 *Pair Finder
 *Assignment 4, Question 2
 *find pairs in a one dimensional array that add up to a given target sum
 */

import java.util.Scanner;

public class PairFinder {
    public static void main(String[] args) {
    	
        Scanner sc = new Scanner(System.in);

        // given example array
        int[] arr = {1, 2, 3, 4, 5, 6};

        // Get the target sum from the user
        System.out.println("Enter the target sum:");
        int target = sc.nextInt();

        // Find pairs
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] + arr[j] == target) {
                    System.out.println("Pair found: (" + arr[i] + ", " + arr[j] + ")");
                }
            }
        }
    }
}


	
