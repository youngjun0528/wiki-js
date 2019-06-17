package Chapter3.EX12;

import java.util.Scanner;

public class ex12_calRate {

	public static void main(String[] args) {
		System.out.println("Enter the principal : ? ");
		int principal = inputScannerInteger();
		
		System.out.println("Enter the rate of interest ? ");
		String interest = inputScannerString();
		
		float rateOfInterest = Float.parseFloat(interest);
		
		System.out.println("Enter the number of years ? ");
		int years = inputScannerInteger();
		
		float investment = 0;
		
		investment = principal * ( 1 + rateOfInterest/100 * years);
		
		System.out.println("After " + years + " years at " + rateOfInterest +"%, the investment will be worth $" + investment);
		
		
		
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
