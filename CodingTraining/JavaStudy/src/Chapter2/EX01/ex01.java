package Chapter2.EX01;

import java.util.Scanner;

public class ex01 {

	public static void main(String[] args) {
		
		System.out.print("What is your name ? ");
		
		String name = inputScanner();
		
		String answer = concatScanner(name);
		
		outputScanner(answer);
	}
	
	
	public static String  inputScanner(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return input;
	}
	
	public static String concatScanner(String out){
		String output = "";
		
		output = output.concat("Hello, ");
		output = output.concat(out);
		output = output.concat(", nice to meet you!");
		
		return output;
	}
	
	public static void outputScanner(String out){
		System.out.println(out);
	}

}
