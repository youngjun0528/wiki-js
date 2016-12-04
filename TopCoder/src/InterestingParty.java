import java.util.HashMap;

public class InterestingParty {
	public static void main(String[] args) {
		// 흥미 있어 하는 주제
		
		String[] first= {"fishing", "gardening", "swimming", "fishing"};
		
		String[] second= {"hunting", "fishing", "fishing", "biting"};
		
		int result = bestInvitationForEx(first, second);
		
		System.out.println("result : " + result);
		
		String[] first2= {"snakes", "programming", "cobra", "monty"};
		
		String[] second2= {"python", "python", "anaconda", "python"};
		
		int result2 = bestInvitationForEx(first2, second2);
		
		System.out.println("result2 : " + result2);
	}
	
	public static int bestInvitation(String[] first, String[] second){
		// 문제 분석
		// 1. 첫번째 주제 그룸 내에서 동일한 주제를 가진 사람 탐색 
		// 2. 두번재 주제 그룸 내에서 동일한 주제를 가진 사람 탐색
		// 3. 첫번재 주제 그룸과 두번재 그룸 내에서 동일한 주제를 가진 사람 탐색
		
		// 조건은 첫번재 주제 그룸 내의 i번째 주제는 두번째 주제 그룸 내의 i번째 주제와는 다르다라고 명시
		// first[i] != second[i]
		// 즉, 한 사람이 동일한 주제를 2개 가질수 없다.
		
		// 해답은 공통 주제가 있는 사람의 수를 구하는 것으로 아래 2가지 상황 중 가장 많은 수를 선택한다.
		// 첫번빼 그룹내 공통 주제 수 + 첫번째 그룹기준으로 두번째 그룹과 공통인 주제 수
		// 두번째 그룹내 공통 주제 수 + 두번째 그룹기준으로 첫번째 그룹과 공통인 주제 수
		
		
		int max = 0;
		
		for(int i = 0; i < first.length ; i++){
			int result1 = 0;
			int result2 = 0;
			for(int j = 0 ; j< second.length ; j++){
				String subject1 = first[i];
				String subject2 = first[j];
				String subject3 = second[i];
				String subject4 = second[j];
				
				// 첫번재 그룸 내에서 일치하는 사람 수 + 1
				if(subject2.equals(subject1)){
					result1++;
				}
				// 두번재 그룹 내에서 일치하는 사람 수 + 1
				if(subject3.equals(subject4)){
					result2++;
				}
				// 첫번째 그룹 기준으로 두번째 그룸 내에서 일치하는 사람 수 + 1
				if(subject1.equals(subject4)){
					result1++;
				}
				// 두번째 그룹 기준으로 첫번째 그룸 내에서 일치하는 사람 수 + 1
				if(subject3.equals(subject2)){
					result2++;
				}
			}
			max = Math.max(result1, max);
			max = Math.max(result2, max);
		}
		return max;
	}
	
	public static int bestInvitationForEx(String[] first, String[] second){
		
		// 솔직히 책에 나와있는대로 사람 기준으로 Loop 태워서 보내는 방법은 그다지 추천하지 않는다.
		// 이해하기도 어렵고 반복문을 돌릴 방법이 명확히 떠올리지 않기 때문이다.
		
		// 처음 생각했던 방법인 HashMap을 사용하여 사람 기준이 주제 기준으로 찾는 것이 훨씬 명확한다.
		// 적어도 내 기준에서는...
		// 결국 응용기술에 나왔다.
		
		int max = 0;
		
		HashMap<String, Integer> map = new HashMap<>();
		
		// 1. 첫번째 그룹 내에서 주제 별로 HashMap에 담는다.
		for(int i = 0 ; i < first.length ; i++){
			if(map.get(first[i]) != null){
				map.put(first[i], map.get(first[i])+1);
			}else{
				map.put(first[i], 1);
			}
		}
		
		// 1. 두번째 그룹 내에서 주제 별로 HashMap에 담는다.
		for(int i = 0 ; i < second.length ; i++){
			if(map.get(second[i]) != null){
				map.put(second[i], map.get(second[i])+1);
			}else{
				map.put(second[i], 1);
			}
		}
		
		for (String key : map.keySet()) {
			max = Math.max(map.get(key), max);
		}
		
		return max;
	}
	
}
