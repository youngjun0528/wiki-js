package Chapter2.EX05;

import java.util.Scanner;

import javax.swing.CellEditor;

public class ex05 {

	public static void main(String[] args) {
		
		System.out.print("What is the first number ? ");
		
		String input1 = inputScanner();
		
		System.out.print("What is the second number ? ");
		
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
		int firstInt = Integer.parseInt(out1);
		int secondInt = Integer.parseInt(out2);
		
		int sum = firstInt + secondInt;
		int minus = firstInt - secondInt;
		int complex = firstInt * secondInt;
		int div = firstInt / secondInt;
		
		String out = 
		firstInt + " + " + secondInt + " = " + sum + "\n" + 		
		firstInt + " - " + secondInt + " = " + minus + "\n" +
		firstInt + " * " + secondInt + " = " + complex + "\n" +
		firstInt + " / " + secondInt + " = " + div + "\n";
		
		System.out.println(out);
	}

}
