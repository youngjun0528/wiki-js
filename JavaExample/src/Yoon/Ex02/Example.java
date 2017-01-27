package Yoon.Ex02;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
 
public class Example {
 
    public static void main(String[] args) {
        
        Example main = new Example();
        main.start();
    }
    
    private void start() {
        
        String names = "이유덕,이재영,권종표,이재영,"
                + "박민호,강상희,이재영,김지완,최승혁,이성연,박영서,"
                + "박민호,전경헌,송정환,김재성,이유덕,전경헌";
        
        String[] nameList = names.split(",");
        List<String> list = this.nameCount(nameList);
        List<String> uniqueNames = this.removeDupliacate(list);
        List<String> ascNames = this.removeASC(list);
        
    }
    
    public List<String> nameCount(String[] nameList){
    	 int count_kim = 0;
         int count_lee = 0;
         int count_ljy = 0;
         
         List<String> list = new ArrayList<String>();
         
         /**
          * To-Do
          */
         for(int i =0 ; i <= nameList.length-1 ; i++){
        	 if(nameList[i].substring(0, 1).equals("김")){
        		 count_kim++;
        	 }else if(nameList[i].substring(0, 1).equals("이")){
        		 count_lee++;
        	 }
        	 if(nameList[i].equals("이재영")){
        		 count_ljy++; 
        	 }
        	 list.add(i, nameList[i]);
         }
         
         System.out.println("김씨:" + count_kim);
         System.out.println("이씨:" + count_lee);
         System.out.println("이재영:" + count_ljy);
         
         return list;
    }
    
    public List<String> removeDupliacate(List<String> list){
    	//중복제거
        List<String> uniqueNames = new ArrayList<String>();
        /**
         * To-Do
         */
        HashMap<String, String> nameMap = new HashMap<String, String>();
        
        for(int i  = 0; i < list.size() ; i++){
        	nameMap.put(list.get(i), list.get(i));
        }
        
        System.out.println("중복제거:"+ nameMap);
        System.out.println("중복제거:"+ nameMap.values());
        
        return uniqueNames;
    }
    
    public List<String> removeASC(List<String> uniqueNames){
    	//오름차순정렬
        /**
         * To-Do
         */
    	Collections.sort(uniqueNames);
    	
    	System.out.println("오름정렬:"+uniqueNames);
    	
    	Collections.reverse(uniqueNames);
    	
        System.out.println("내림정렬:"+uniqueNames);
        
        return uniqueNames;
    }
}