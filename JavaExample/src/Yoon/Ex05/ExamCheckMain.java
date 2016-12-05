package Yoon.Ex05;

import java.util.ArrayList;
import java.util.Scanner;


public class ExamCheckMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		System.out.println("1. 전체 학생의 이름과 점수 출력 하세요. >>>>>");
		System.out.println("2. 전체 학생 의 국어 점수의 평균을 구하세요. >>>>>");
		System.out.println("3. 전체 학생 의 국어 점수의 평균에 가장 가까운 사람을 구하세요. >>>>>");
		System.out.println("4. 윤씨 성을 가진 사람의 영어 점수의 평균을 구하세요. >>>>>");
		System.out.println("5. 모든 학생 중에서 수학 점수의  최대값과 최소값을 구하세요. >>>>>");
		System.out.println("6. 수학 점수를 기준으로 오름차순 정렬하세요. >>>>>");
		System.out.println("7. 영어 점수를 기준으로 내림차순 정렬하세요. >>>>>");
		System.out.println("8. 학생 중에서 가장 많은 성씨를 가진 성을 구하세요. >>>>>");
		
		ExamFileReader file= new ExamFileReader();
		ArrayList<ExamDao> daoList = new ArrayList<ExamDao>();
		daoList = file.reader();
		Scanner sc = new Scanner(System.in);
		System.out.print("메뉴를 입력하세요. >>>>>");
		ExamBiz biz = new ExamBiz();
		while(true){
			int input = sc.nextInt();
			if(input == 1){
				 //모든 학생과 점수를 출력
				biz.print(daoList);
				System.out.print("메뉴를 입력하세요. >>>>>");
			}else if(input == 2){
				//국어 점수 평균을 출력
				int sum = biz.fnSummury(daoList, "korean");
				System.out.println("국어 점수의 총합은 : " + sum );
				System.out.println("국어 점수의 평균은 : " + sum / daoList.size());
				System.out.print("메뉴를 입력하세요. >>>>>");
			}else if(input == 3){
				String name = null;
				name = biz.fnNear(daoList, "korean");
				System.out.println("평균에 가장 근접한 사람은 " + name);
				System.out.print("메뉴를 입력하세요. >>>>>");
			}else if(input == 4){
				int avg = 0;
				avg = biz.fnAverage(daoList, "english", "윤");
				System.out.println("윤씨 성을 가진 사람의 영어 평균 " + avg);
				System.out.print("메뉴를 입력하세요. >>>>>");
			}else if(input == 5){
				int[] minMax = null;
				minMax = biz.fnMinMax(daoList, "math");
				System.out.println("수학 점수의 최대값 :  " + minMax[0] +  " 최소값  : " +minMax[1]);
				System.out.print("메뉴를 입력하세요. >>>>>");
			}else if(input == 6){
				System.out.println("수학 점수 기준 오름차순 정렬 ");
				biz.fnASC(daoList, "math");
				System.out.print("메뉴를 입력하세요. >>>>>");
			}else if(input == 7){
				System.out.println("영어 점수 기준 내림차순 정렬" );
				biz.fnDESC(daoList, "english");
				System.out.print("메뉴를 입력하세요. >>>>>");
			}else if(input == 8){
				String nameSub = null;
				nameSub = biz.fnMode(daoList);
				System.out.println("학생 중에 가장 많은 성씨는 " + nameSub);
				System.out.print("메뉴를 입력하세요. >>>>>");
			}
		}
	}
}
