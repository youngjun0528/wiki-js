package Chapter3.EX10;

import java.util.Scanner;

public class ex10_selfCal {

	public static void main(String[] args) {
		// 3가지 물건의 가격과 수량을 입력받는다.
		int [][] itemArr = new int[3][2];
		
		for(int i = 0; i < 3 ; i++){
			System.out.println("Price of item " + i);
			int itemPrice = inputScannerInteger();
			
			itemArr[i][0] = itemPrice;
					
			System.out.println("Quantity of item " + i);
			int itemQuantity = inputScannerInteger();
			
			itemArr[i][1] = itemQuantity;
		}
		
		int subTotal = 0;
		
		for(int i = 0; i < itemArr.length ; i++){
			subTotal = subTotal + (itemArr[i][0] * itemArr[i][1]);
		}
		// 합계를 구한다.
		System.out.println("subTotal : " + subTotal);
		
		// 합계에 대한 5.5% 세금을 부과한다.
		float total = (float) (subTotal + (subTotal * 0.055));
		System.out.println("total : " + total);
		
		// 물건 종류별 수량 과 전체 수량을 출력한 후 가격 소계, 세금, 합계 금액을 출력
		
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
