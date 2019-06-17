package Chapter2.EX03;

import java.util.Scanner;

public class ex03 {

	public static void main(String[] args) {
		
		System.out.print("What is the quote ? ");
		
		String input1 = inputScanner();
		
		System.out.print("Who said it ? ");
		
		String input2 = inputScanner();
		
		outputScanner(input1 , input2);
	}
	
	
	public static String  inputScanner(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return input;
	}
	
	public static void outputScanner(String out1, String out2){
		String printOut = out1 + " says, " + "\"" + out2 + "\""; 
		System.out.println(printOut);
	}

}
