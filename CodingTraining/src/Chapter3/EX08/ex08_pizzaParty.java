package Chapter3.EX08;

import java.util.Scanner;

public class ex08_pizzaParty {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("How many people ? ");
		String people = inputScanner();
		
		System.out.println("How many pizzas do you have ? ");
		String pizza = inputScanner();
		
		int peopleCount = Integer.parseInt(people);
		int pizzaCount = Integer.parseInt(pizza);
		
		
		int piecesCount = 0;
		
		while(true){
			
			System.out.println("How many pieces are in a pizza ? ");
			String pieces = inputScanner();
			
			piecesCount = Integer.parseInt(pieces);
			
			if(piecesCount % 2 == 0 && piecesCount >= 1){
				break;
			}
		}
		
		pizzaParty(peopleCount, pizzaCount, piecesCount);

	}
	
	public static String  inputScanner(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return input;
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
