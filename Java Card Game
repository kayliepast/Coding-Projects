CARD.JAVA
public class Card {
	// Private fields for suit and rank
	private Suit suit;
	private Rank rank;
	
	// Constructor to initialize suit and rank
	public Card (Suit suit, Rank rank) {	
		this.suit = suit;
		this.rank = rank;
	}
	// Getter methods 
	public Suit getSuit() {
		return this.suit;
	}
	
	public Rank getRank() {
		return this.rank;
	}
	
	public int getValue() {
		if (rank == Rank.Two) return 2;
		else if (rank == Rank.Three) return 3;
		else if (rank == Rank.Four) return 4;
		else if (rank == Rank.Five) return 5;
		else if (rank == Rank.Six) return 6;
		else if (rank == Rank.Seven) return 7;
		else if (rank == Rank.Eight) return 8;
		else if (rank == Rank.Nine) return 9;
		else if (rank == Rank.Ten) return 10;
		else if (rank == Rank.Jack) return 11;
		else if (rank == Rank.Queen) return 12;
		else if (rank == Rank.King) return 13;
		else return 14;
	}
	
	public String toString() {
		return this.rank + " of " + this.suit;

}
}

DECK.JAVA
// add all the card in the Deck

// Shuffle()
//deal()

import java.util.ArrayList;
import java.util.Collections;

public class Deck {
	private ArrayList<Card> deck;

	// constructor to build the deck with 52 cards
	public Deck() {
		this.deck = new ArrayList<Card> ();
		
		// Loop through all 52 cards
		for (Suit s : Suit.values()) {
		    for (Rank r : Rank.values()) {
		      Card c = new Card(s, r);
		      deck.add(c);
		    }
		} 
		
	}
	
	// shuffle 
	public void shuffle() {
		Collections.shuffle(this.deck);
	}
	// deal a card from the top of the deck
	public Card deal() {
		return this.deck.remove(this.deck.size() -1);
	}
	// return a String representation of this deck
	public String toString() {
		return this.deck.toString();
	}
	
}

HIGHCARDGAME.JAVA 

public class HighCardGame {

	public static void main(String[] args) {
		// Create a new Deck object.
		Deck d = new Deck();
		
		// Shuffle the deck.
		d.shuffle();
		
		// Deal one card for Player 1.
		Card p1Card = d.deal();
		// Deal one card for Player 2.
        Card p2Card = d.deal();
        
        // Print both players' cards.
        System.out.println("Player 1 drew: " + p1Card);
        System.out.println("Player 2 drew: " + p2Card);
		

		// Compare the cards and print out who wins (or if it's a tie).
        if (p1Card.getValue() > p2Card.getValue()) {
            System.out.println("Player 1 wins!");
        } 
        else if (p1Card.getValue() < p2Card.getValue()) {
            System.out.println("Player 2 wins!");
        } 
        else {
            System.out.println("It's a tie!");
		}

}
	}

RANK.JAVA

public enum Rank { 
	Two,
	Three,
	Four,
	Five, 
	Six, 
	Seven, 
	Eight, 
	Nine, 
	Ten, 
	Jack, 
	Queen, 
	King,
	Ace;
}

SUIT.JAVA 

public enum Suit {
	Clubs,
	Diamonds,
	Hearts,
	Spades;
}

