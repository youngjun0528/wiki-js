package Yoon.Ex07;

import java.util.Scanner;

public class Collatz {
	public static void main(String[] args) {
		Scanner num = new Scanner(System.in);
		int a = num.nextInt();
		int b = num.nextInt();
		
		int max = Integer.MIN_VALUE;
		int cout = 1;
		for(int j = a ; j <= b ; j++){
			int i = j;
			cout = 1;
			while(i >= 1){
				if(i % 2 == 0){
					i = i / 2;
				}else if(i % 2 == 1){
					i = i*3 + 1;
				}
				cout++;
				if(i == 1){
					break;
				}
			}
			if(max < cout){
				max = cout;
			}
		}
		System.out.println(max);
	}
}
