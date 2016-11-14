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
		String name = null;
		
		Scanner scanner = new Scanner(System.in);
		name = scanner.nextLine();
		
		
		return name;
	}
	
	public static String concatScanner(String out){
		String answer = "";
		
		answer = answer.concat("Hello, ");
		answer = answer.concat(out);
		answer = answer.concat(", nice to meet you!");
		
		return answer;
	}
	
	public static void outputScanner(String out){
		System.out.println(out);
	}

}
