
public class Cryptography {

	public static void main(String[] args) {
		
		int[] numbers1 = {1,2,3};
		
		long result1 = encrypt(numbers1);
		
		System.out.println("result1 : " + result1);
		
		int[] numbers2 = {1,3,2,1,1,3};
		
		long result2 = encrypt(numbers2);
		
		System.out.println("result2 : " + result2);
		
	}
	
	public static long encrypt(int[] numbers){
		long tas = 0;
		
		long temp1 = 1;
		// 먼저 각 배열 요소의 곱을 구한다.
		for(int i = 0; i < numbers.length ; i++){
			temp1 = temp1 * numbers[i]; 
		}
		//System.out.println("temp1 " + temp1);
		
		long temp2 = 1;
		// 각 배열 요소를 +1 을 하도록 한다.
		for(int i = 0; i < numbers.length ; i++){
			 temp2 = numbers[i] + 1;
			 //System.out.println("temp2 " + temp2);
		}
		
		// 변수 초기화
		temp1 = 1;
		
		// 각 배열 요소를 +1을 하면서 곱을 구한다.
		// 위 2개의 for문을 합친다.
		for(int i = 0; i < numbers.length ; i++){
			temp1 = numbers[i] + 1;
			for(int j = 0; j < numbers.length ; j++){
				if(i != j){
					temp1 = temp1 * numbers[j];
				}
			}
			//System.out.println("max : " + temp1);
			tas = Math.max(tas, temp1);
		}
		
		return tas;
	}
	
}
