package Chapter2.EX06;

import java.sql.Date;
import java.util.Calendar;
import java.util.Scanner;

public class ex06 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.print("What is your current age ? ");
		String start = inputScanner();
		
		System.out.print("At what age would you like to retire ? ");
		String end = inputScanner();
		
		exfireCalculate(start, end);
		
		
	}
	
	public static int exfireCalculate(String start, String end){
		int result = 0;
		
		int startAge = Integer.parseInt(start);
		int endAge = Integer.parseInt(end);
		
		Calendar cal = Calendar.getInstance();
		int year = cal.get(Calendar.YEAR);
		
		int current = endAge - startAge;
		int exfire = year + current;
		
		if(current >= 0){
			System.out.println("You have " + current + " years left until you can retire.");
			System.out.println("It's " + year + ", so you can retire in " + exfire);
		}
		
		return result;
	}
	
	public static String  inputScanner(){
		String input = null;
		
		Scanner scanner = new Scanner(System.in);
		input = scanner.nextLine();
		
		return input;
	}

}
