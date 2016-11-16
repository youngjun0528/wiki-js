
public class KiwiJuiceEasy {

	public static void main(String[] args) {
		// 병의 용량
		int[] capacities = {20, 20};
		
		// 주스의 용량
		int[] bottles = {5, 8};
		
		// 어느 병으로부터 어느 병으로 넣을 것인가?
		int[] fromId = {0};
		int[] toId = {1};
		
		thePouring(capacities, bottles, fromId, toId);
	}
	
	// Level 1
	public static int[] thePouring(int[] capacities, int[] bottles, int[] fromId, int toId[]){
		
		// 시작병의 indes를 순회한다.
		for(int i = 0; i < fromId.length ; i++){
			// 시작병의 index 추출
			int from = fromId[i];
			// 도착병의 index 추출
			int to = toId[i];
			
			// 넣을수 있는 용량은 도착별의 남아 있는 용량
			int space = capacities[to] - bottles[to];
			
			if(space >= bottles[from]){
				// 만약 시작병의 주스 용량이 도착병의 남아 있는 공간보다 작다면
				// 모든 주스는 도착병 안에 넣어 버린다.
				int vol = bottles[from];
				bottles[to] = bottles[to] + vol;
				bottles[from] = 0;
			}else{
				// 만약 시작병의 주스 용량이 도착병의 남아 있는 공간보다 크다면
				// 도착병에 남아 있는 용량을 모두 채우고
				// 시작병은 남아 있는 용량을 따른 만큼 남아 있다. 
				int vol = space;
				bottles[to] = bottles[to] + vol;
				bottles[from] = bottles[from] - vol;
			}
			
		}
		
		return bottles;
	}

}
