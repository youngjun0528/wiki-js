package Yoon.Ex01;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class BicycleBiz {
	
	private List<CustomerVO> customerList;
	private CustomerVO customer;
	private BicycleVO high;
	private BicycleVO mid;
	private BicycleVO low;
	private Scanner input;
	private static Date curDate;
	private int choice; // ¸Þ´º
	private int choiceBicycle; // ÀÚÀü°Å¼±ÅÃ
	private boolean result;
	
	public BicycleBiz() {
		this.customerList = new ArrayList<CustomerVO>();
		this.input = new Scanner(System.in);
		this.high = new BicycleVO("°í±ÞÇü", 5000, 2);
		this.mid = new BicycleVO("Áß±ÞÇü", 3000, 5);
		this.low = new BicycleVO("º¸±ÞÇü", 1000, 15);
	}

	public List<CustomerVO> getCustomerList() {
		return customerList;
	}

	public void setCustomerList(List<CustomerVO> customerList) {
		this.customerList = customerList;
	}

	public int getChoice() {
		return choice;
	}

	public void setChoice() { // ¸Þ´º choice ¿¡ ´ëÇÑ InputMismatchException¿¹¿ÜÃ³¸®
		while(true){
			try{
				this.choice = this.inputScannerInt();
				break;
			}
			catch(InputMismatchException ime){
				System.out.println("1,2 Áß¿¡ ÀÔ·ÂÇØÁÖ¼¼¿ä.");
			}
		}
	}
	
	public int getChoiceBicycle() {
		return choiceBicycle;
	}

	public void setChoiceBicycle() { // ÀÚÀü°Å ¼±ÅÃ choice ¿¡ ´ëÇÑ ¿¹¿Ü Ã³¸®
		while(true){
			try{
				this.choiceBicycle = this.inputScannerInt();
				break;
			}
			catch(InputMismatchException ime){
				System.out.println("1,2,3 Áß¿¡ ÀÔ·ÂÇØÁÖ¼¼¿ä.");
			}
		}
	}

	public int inputScannerInt(){
		input = new Scanner(System.in);
		return input.nextInt();
	}
	
	public void startProgram() {
		int choice = 0;
		
		while ( true ) {
			this.customer = new CustomerVO();
			//customer.bicycleList = new ArrayList<String>();
			System.out.println("=====ÀÚÀü°Å ´ë¿© ÇÁ·Î±×·¥ ÀÔ´Ï´Ù.=====");
			System.out.println("1. ´ë¿©");
			System.out.println("2. ¹Ý³³");
			System.out.println("3. Á¾·á");
			System.out.println("===================================");
			
			this.setChoice();
			choice = this.getChoice();
			
			if ( choice == 1 ) { // ´ë¿©
				int choiceBicycle = 0;				
				while(true){
					System.out.println("ºô¸± ÀÚÀü°Å¸¦ ¼±ÅÃÇÏ¼¼¿ä.");
					System.out.println("1. º¸±Þ");
					System.out.println("2. Áß±Þ");
					System.out.println("3. °í±Þ");
					System.out.println("ÀÚÀü°Å º¸À¯ ÇöÈ²");
					low.currentCount(); // ÀÚÀü°Å Á¤º¸ Ãâ·Â
					mid.currentCount();
					high.currentCount();
				
					this.setChoiceBicycle(); 
					choiceBicycle = this.getChoiceBicycle();
					
					if ( choiceBicycle == 1 ) { //º¸±ÞÇü¼±ÅÃÇßÀ» ¶§ 
						rent(low);
						this.addNewCustomerInfo(customer);
						break;
					}
					else if ( choiceBicycle == 2 ){
						rent(mid);
						this.addNewCustomerInfo(customer);
						break;
					}
					else if (choiceBicycle == 3){
						rent(high);
						this.addNewCustomerInfo(customer);
						break;
					}
					else{
						System.out.println("´Ù½ÃÀÔ·ÂÇØÁÖ¼¼¿ä.");//if
					}
				}//while
			}
			else if ( choice == 2 ) { // ¹Ý³³
				while(true) {
					System.out.println("¹Ý³³ÇÒ ÀÌ¸§À» ÀÔ·ÂÇÏ¼¼¿ä.");
					String deleteName = input.next();
					if ( checkScanner("^[°¡-ÆRa-zA-Z]*$", deleteName) ){
					}
					else{ 
						if (this.result = this.deleteCustomerByName(deleteName) ){ //Á¸ÀçÇÏ¸é
							Calendar cal = Calendar.getInstance();
							long time = cal.getTimeInMillis() + 1800000; //Å×½ºÆ®¿ë
							//long time = cal.getTimeInMillis();
							this.checkCount(getInfo(deleteName), high, time);
							this.checkCount(getInfo(deleteName), mid, time);
							this.checkCount(getInfo(deleteName), low, time);// ¾î¶² ÀÚÀü°Å ºô·È¾ú´ÂÁö °Ë»ç ÇØ¼­ ¹Ý³³
							this.customerList.remove(getInfo(deleteName)); // °í°´ Á¤º¸ »èÁ¦
							System.out.println(deleteName + "´ÔÀÇ Á¤º¸°¡ »èÁ¦µÇ¾ú½À´Ï´Ù.\n");
							break;
						}
						else{ //ÀÌ¸§ÀÌ Á¸ÀçÇÏÁö¾ÊÀ¸¸é
							System.out.println(deleteName+"ÀÇ Á¤º¸°¡ ¾ø½À´Ï´Ù.\n");
							break;
						}//else
					}//else
				}//while
			}//else if
			else if ( choice == 3 ) {
				System.exit(0);
			}
		}//while
	}
	
	private void rent(BicycleVO type){
		curDate = new Date();
		Calendar now = Calendar.getInstance();
		customer.setRentTime(now.getTimeInMillis());
		if ( type.checkCount() ){ // ³²Àº ¼ö È®ÀÎ
			System.out.println("ÀÚÀü°Å°¡ 0´ë¿¡¿ä.");
		}
		else{ // ÀÚÀü°Å°¡ ³²¾Æ ÀÖ´Ù¸é
			System.out.println("ÀÌ¸§°ú °¡Áø µ·À» ÀÔ·ÂÇÏ¼¼¿ä."); // °í°´ Á¤º¸ µî·Ï
			String name = input.next();
			customer.setName(name);
			int money = input.nextInt();
			customer.setMoney(money);
			customer.setType(type.getType());
			type.rent(); // º¸±ÞÇüÀÇ count¸¦ 1 ÁÙÀÎ´Ù.
			System.out.println(name + ": " + type.getType() + "ÀÚÀü°Å¸¦ ÇÑ´ë ´ë¿©ÇÏ¼Ì½À´Ï´Ù.");
			System.out.println("´ë¿©ÇÑ ½Ã°£ : " + curDate); // ´ë¿©ÇÑ ½Ã°£ Ãâ·Â
		}		
	}
	
	public void checkCount ( CustomerVO customer , BicycleVO type, long time) { //  ¹Ý³³ °è»ê ¸Þ¼Òµå
		if ( customer.getType() == type.getType()){ // °í°´ÀÌ °í±ÞÇüÀ» °¡Áö°í ÀÖ´Ù¸é
			type.back(); // °í±ÞÇü ÀÚÀü°Å count 1 Áõ°¡ (¹Ý³³ÇßÀ¸¹Ç·Î)
			long result = (time - customer.getRentTime()) / 1000;
			int minute = (int)Math.round((double)result / 60); //½Ã°£À¸·Î µ·°è»ê
			System.out.println("ÀÌ¿ë½Ã°£(ºÐ) : " + minute);
			if ( minute < 10) { // 10ºÐº¸´Ù ÀûÀ¸¸é µ· ¾È³»µµ µÈ´Ù°í
				System.out.println("ÀÌ¿ëÇÏ½Å ½Ã°£ÀÌ 10ºÐ ¹Ì¸¸ÀÔ´Ï´Ù. µ· ¾È³»µµ´ï");
				System.out.println("¹Ý³³µÇ¾ú½À´Ï´Ù. °í°´´ÔÀÇ ÀÜ¾× : " + customer.getMoney());
			}
			else {
				int cost = (minute / 10) * type.getCost(); // 10ºÐ´ç µ· °è»ê
				System.out.println("±Ý¾× :" + cost);
				customer.setMoney(customer.getMoney() - cost);
				System.out.println("¹Ý³³µÇ¾ú½À´Ï´Ù. °í°´´ÔÀÇ ÀÜ¾× : " + customer.getMoney());
			}
		}
		else{
		}
	}
	
	public boolean deleteCustomerByName( String name ) {
		for ( CustomerVO customer : this.customerList ) {
			if( customer.getName().equals(name) ) {
				return true;
			}
		}
		return false;
	}
	
	public CustomerVO getInfo( String name ) {
		for ( CustomerVO customer : this.customerList ) {
			if ( customer.getName().equals(name) ){
				this.customer = customer;
				return customer;
			}
		}
		return new CustomerVO();
	}
	
	public boolean checkScanner( String checkScan, String whatString ) {
		if ( !whatString.matches(checkScan) ) {
			System.out.println("ÀçÀÔ·Â");
			return true;
		}
		else {
			return false;
		}
	}
	
	public void addNewCustomerInfo(CustomerVO customer){
		this.customerList.add(customer);
	}

}