package Chapter3.EX07;

import java.util.Scanner;

public class ex07_squareRoom {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("What is the length of room in feet ?");
		String length = inputScanner();
		
		System.out.println("What is the width of the room in feet ?");
		String width = inputScanner();
		
		System.out.println("You enterd dimensions of " + length + "feet by " + width + "feet");
		
		calculationRoom(length, width);
	}
	
	public static String  inputScanner(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return input;
	}
	
	public static void calculationRoom(String length, String width){
		
		int len = Integer.parseInt(length);
		int wid = Integer.parseInt(width);
		
		int area = len * wid;
		
		System.out.println("The area is " + area + " square feet");
		
		double genArea = (double) (area * 0.09290304);
		
		System.out.println(genArea + " square meters");
		
	}

}
