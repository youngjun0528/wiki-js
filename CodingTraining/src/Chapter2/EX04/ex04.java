package Chapter2.EX04;

import java.util.Scanner;

public class ex04 {

	public static void main(String[] args) {
		
		System.out.print("Enter a noun : ");
		
		String input1 = inputScanner();
		
		System.out.print("Enter a verb : ");
		
		String input2 = inputScanner();
		
		System.out.print("Enter a adjective : ");
		
		String input3 = inputScanner();
		
		System.out.print("Enter a adverb : ");
		
		String input4 = inputScanner();
		
		outputScanner(input1 , input2 , input3 , input4);
	}
	
	
	public static String  inputScanner(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return input;
	}
	
	public static void outputScanner(String out1, String out2, String out3, String out4){
		String printOut = "Do you @verb your @adjective @noun @adverb ?";
		String printAnswer = "That's hilarious";
		
		printOut = printOut.replace("@verb", out4);
		printOut = printOut.replace("@adjective", out3);
		printOut = printOut.replace("@noun", out1);
		printOut = printOut.replace("@adverb", out2);
		
		System.out.println(printOut);
		System.out.println(printAnswer);
	}

}
