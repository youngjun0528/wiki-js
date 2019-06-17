package Chapter3.EX11;

import java.util.Scanner;

public class ex11_changeDollar {

	public static void main(String[] args) {
		
		System.out.println("How many Euros are you exchanging ? ");
		int euros = inputScannerInteger();
		
		System.out.println("What is the exchange rate ? ");
		String exchangeRate = inputScannerString();
		
		float reExchangeRate = Float.parseFloat(exchangeRate);
		
		float dollars = 0;
		
		dollars = euros * reExchangeRate / 100;
		
		System.out.println(euros + " Euros at an exchange rate of " + exchangeRate + " is " );
		System.out.println(dollars + " dollars");
		
		
		
		
	}
	
	public static String  inputScannerString(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return input;
	}
	
	public static int  inputScannerInteger(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return Integer.parseInt(input);
	}
	
	public static void pizzaParty(int people, int pizza, int pieces){
		
		System.out.println(people + " people with " + pizza);
		
		int totalPieces = pizza * pieces;
		
		int eachPieces = totalPieces / people;
		
		int leftPieces = totalPieces % people;
		
		System.out.println("Each person gets " + eachPieces + " pieces of pizza");
		
		System.out.println("There are " + leftPieces + " leftover pieces.");
		
	}

}
