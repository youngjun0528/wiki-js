
public class InterestingParty {
	public static void main(String[] args) {
		// 흥미 있어 하는 주제
		
		String[] first= {"fishing", "gardening", "swimming", "fishing"};
		
		String[] second= {"hunting", "fishing", "fishing", "biting"};
		
		int result = bestInvitation(first, second);
		
		System.out.println("result : " + result);
		
		String[] first2= {"snakes", "programming", "cobra", "monty"};
		
		String[] second2= {"python", "python", "anaconda", "python"};
		
		int result2 = bestInvitation(first2, second2);
		
		System.out.println("result2 : " + result2);
	}
	
	public static int bestInvitation(String[] first, String[] second){
		int result = 0;
		
		for(int i = 0; i < first.length ; i++){
			String subject1 = first[i];
			for(int j = 0 ; j< second.length ; j++){
				String subject2 = second[j];
				String subject3 = first[j];
				if(j != i && subject2.equals(subject1)){
					result++;
				}
				if(j != i && subject1.equals(subject3)){
					result++;
				}
			}
		}
		
		for(int i = 0; i < first.length ; i++){
			String subject1 = first[i];
			for(int j = 0 ; j< second.length ; j++){
				String subject2 = second[j];
				if(j != i && subject2.equals(subject1)){
					result++;
				}
			}
		}
		return result;
	}
}
