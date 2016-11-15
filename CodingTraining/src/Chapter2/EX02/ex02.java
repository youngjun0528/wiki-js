package Chapter2.EX02;

import java.util.Scanner;

public class ex02 {

	public static void main(String[] args) {
		
		System.out.print("What is the input string ? ");
		
		String input = inputScanner();
		
		int count = countString(input);
		
		outputScanner(input, count);
	}
	
	
	public static String  inputScanner(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return input;
	}
	
	public static int countString(String out){
		int output = 0;
		
		if(out != null){
			output = out.length();
		}
		
		return output;
	}
	
	public static void outputScanner(String in, int out){
		String printOut = in + " has " + Integer.toString(out) + " characters.";
		System.out.println(printOut);
	}

}
