package Yoon.Ex03;

import java.util.Scanner;

public class study_main {

	/**
	 * @param 시작 연도와 종료 연도를  입력 받아서 그 사이의 윤년이 얼마나 포함되어 있는지 확인하는 프로그램
	 *  윤년인지 확인하는 방법
	 *  1. 해당 연도가 4로 나누어 떨어지면서 100으로  나누어 떨어지지 않는 경우
	 *  2. 해당 연도가 400으로 나누어 떨어지는 경우
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);      // 문자 입력을 인자로 Scanner 생성
        
        System.out.println("시작 년도를 입력하세요.");
        String startYearToString = null;
        startYearToString = scan.nextLine();            // 키보드 문자 입력
        
        String endYearToString = null;
        System.out.println("종료 년도를 입력하세요.");
        endYearToString = scan.nextLine();
        
        System.out.println("입력하신 시작년도는 " + startYearToString + " 종료년도는 " + endYearToString);
        
        int count = checkYear(startYearToString, endYearToString );
        
        System.out.println(count);
	}
	
	public static int checkYear(String startYearToString, String endYearToString ){
		int countYear = 0;
		int startYear = 0;
		int endYear = 0;
		
		try {
			startYear = Integer.parseInt(startYearToString);
			endYear = Integer.parseInt(endYearToString);
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("정수를 입력하지 않았습니다. 프로그램을 종료합니다.");
		}
		
		int count = endYear - startYear;
		
		for( int i = 0; i <  count; i++){
			if(startYear % 4 == 0 && startYear % 100 > 0){
				countYear++;
			}else if(startYear % 400 ==0 ){
				countYear++;
			}
			startYear++;
		}
		return countYear;
	}

}
