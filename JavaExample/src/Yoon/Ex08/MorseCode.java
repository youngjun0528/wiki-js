package Yoon.Ex08;

import java.util.HashMap;
import java.util.Map.Entry;

public class MorseCode {

	private static HashMap<String, String>  morseCode = new HashMap<String,String>();
	private static HashMap<String, String>  reverseCode = new HashMap<String,String>();
	
	public static void main(String[] args){
		morseCodeSetting();
		
		String encodeData = "he sleeps early";
		String decodeData = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--";
		
		//글자와 글자 사이는 공백 하나, 단어와 단어 사이는 공백 두개로 구분한다.
		
		String result = encodeMorse(encodeData);
		
		System.out.println("encodeData result \n" + result);
		
		reverseMap();
		
		result = decodeMorse(decodeData);
		
		System.out.println("decodeData result \n" + result.toLowerCase());
	}
	
	public static String decodeMorse(String Data){
		String result = "";
		
		String[] word = Data.split("  ");
		
		for(int i = 0; i < word.length ; i++){
			String[] charSet = word[i].split(" ");
			for(int j = 0 ; j < charSet.length ; j++){
				result += reverseCode.get(charSet[j]);
			}
			result += " ";
		}
		
		return result;
	}
	
	public static void reverseMap (){
		for(Entry<String, String> entity : morseCode.entrySet()){
			reverseCode.put(entity.getValue(), entity.getKey());
		}
	}
	
	public static String encodeMorse(String Data){
		String result = "";
		
		for(int i = 0; i< Data.length() ; i++){
			if(Data.charAt(i) == ' '){
				result += " ";
			}else{
				result += morseCode.get(Data.toUpperCase().charAt(i)+"") + " ";
			}
		}
		return result;
	}
	
	public static void morseCodeSetting(){
		morseCode.put("A", ".-");
		morseCode.put("B", "-...");
		morseCode.put("C", "-.-.");
		morseCode.put("D", "-..");
		morseCode.put("E", ".");
		morseCode.put("F", "..-.");
		morseCode.put("G", "--.");
		morseCode.put("H", "....");
		morseCode.put("I", "..");
		morseCode.put("J", ".---");
		morseCode.put("K", "-.-");
		morseCode.put("L", ".-..");
		morseCode.put("M", "--");
		morseCode.put("N", "-.");
		morseCode.put("O", "---");
		morseCode.put("P", ".--.");
		morseCode.put("Q", "--.-");
		morseCode.put("R", ".-.");
		morseCode.put("S", "...");
		morseCode.put("T", "-");
		morseCode.put("U", "..-");
		morseCode.put("V", "...-");
		morseCode.put("W", ".--");
		morseCode.put("X", "-..-");
		morseCode.put("Y", "-.--");
		morseCode.put("Z", "--..");
	}
}
