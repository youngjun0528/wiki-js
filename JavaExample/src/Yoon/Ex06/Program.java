package Yoon.Ex06;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.InputMismatchException;
import java.util.List;

public class Program {
	
	private int choice; // ¸Þ´º¼±ÅÃ
	private BankVO bank;
	private List<CustomerVO> customerList;
	private ScannerManage scan;
	private boolean result;
	
	public Program() {
		this.bank = new BankVO();
		new CustomerVO();
		this.scan = new ScannerManage();
		this.customerList = new ArrayList<CustomerVO>();
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

	public void setChoice() { // choice ¿¡ ´ëÇÑ InputMismatchException¿¹¿ÜÃ³¸®
		while(true){
			try{
				this.choice = scan.inputScannerInt();
				break;
			}
			catch(InputMismatchException ime){
				System.out.println("1,2,3,4,5 Áß¿¡ ÀÔ·ÂÇØÁÖ¼¼¿ä.");
			}
		}
	}

	public void startProgram() {
		int choice = 0;
		bank.setTotalMoney(1000000000); // ÃÊ±â ÀºÇà µ· 10¾ïÀ¸·Î ¼³Á¤
		while ( true ) {
			System.out.println("========bank ±¹¹ÎÀºÇà ´ëÃâ========");
			System.out.println("1.´ëÃâ");
			System.out.println("2.µ·°±±â");
			System.out.println("3.´ëÃâ³»¿ªº¸±â");
			System.out.println("4.ÆÄ»ê½ÅÃ»");
			System.out.println("5.Á¾·á");
			System.out.println("==============================="); // ¸Þ´º
			
			this.setChoice();
			choice = this.getChoice(); // choice ÀÔ·Â¹Þ°í ¿¹¿ÜÃ³¸®
			
			if ( choice == 1 ) {
				while(true){
					System.out.println("ÀÌ¸§, ÀüÈ­¹øÈ£, ºô¸®°í ½ÍÀº µ·(¿ø), ´ãº¸¸¦ ÀÔ·ÂÇÏ¼¼¿ä.(ÃÖ´ë ´ëÃâ °¡´É¾×: 1¾ï)");
					String name = scan.inputScanner();
					if(scan.checkScanner("^[°¡-ÆRa-zA-Z]*$", name)){ //ÀÌ¸§¿¡ ´ëÇÑ Ã¼Å©
						System.out.println("ÀçÀÔ·Â");
					}
					else{
						if ( this.checkName(name) ){
							String phoneNumber = scan.inputScanner();
							int money = scan.inputScannerInt();// ¿¹¿ÜÃ³¸®ÇØ¾ßÇØ
							this.checkInputMoney(name, phoneNumber, money);
							bank.printBankInfo(); // ´ëÃâ ÈÄ ÀºÇà µ· Ãâ·Â
							break;
						}
						else {
							System.out.println("»õ·Î¿î Á¤º¸·Î °¡ÀÔÇØÁÖ¼¼¿ä.");
						}
					}//else
				}//while
			}//if
			else if ( choice == 2 ) { // µ·°±±â
				while (true) {
					System.out.println("ÀÌ¸§À» ÀÔ·ÂÇØÁÖ¼¼¿ä.");
					String searchName = scan.inputScanner();
					if(scan.checkScanner("^[°¡-ÆRa-zA-Z]*$", searchName)){ //searchName  Ã¼Å©
					}
					else{
						if ( this.returnMoney(searchName) ){
							break;
						}
						else {
							System.out.println(searchName + "ÀÇ °í°´ Á¤º¸°¡ ¾ø½À´Ï´Ù.");
							break;
						}//else					
					}//else
				}//while
			}//else if
			else if ( choice == 3 ) { // ´ëÃâ³»¿ª È®ÀÎ
				while(true){
					System.out.println("ÀÌ¸§À» ÀÔ·ÂÇØÁÖ¼¼¿ä.");
					String searchName = scan.inputScanner();
					if ( scan.checkScanner("^[°¡-ÆRa-zA-Z]*$", searchName) ){// searchName Ã¼Å©
					}
					else {
						this.searchMyInfo(searchName);
						bank.printBankInfo(); // ÀºÇàÁ¤º¸ Ãâ·Â
						break;
					}
				}
			}
			else if ( choice == 4 ) { // ÆÄ»ê½ÅÃ»
				while (true) {
					System.out.println("ÀÌ¸§À» ÀÔ·ÂÇÏ¼¼¿ä.");
					String deleteName = scan.inputScanner();
					if ( scan.checkScanner("^[°¡-ÆRa-zA-Z]*$", deleteName) ){ // deleteName Ã¼Å©
					}
					else{ 
						this.bankruptcy(deleteName);
						bank.printBankInfo();//ÀºÇàÁ¤º¸ Ãâ·Â
						break;
					}//if
				}//while
			}//else if
			else if ( choice == 5){//ÇÁ·Î±×·¥ Á¾·á
				System.exit(0);
			}
		}//while
	}
	
	public boolean isResult() {
		return result;
	}

	public boolean setResult(boolean result) {
		this.result = result;
		return result;
	}
	
	/**
	 * inputMoney¸¦ Ã¼Å©ÇÏ´Â ¸Þ¼Òµå
	 * ÇÁ·Î¼¼½º
	 * 1) ´ãº¸ Ã¼Å© (ÀÌ¹Ì ±¸Çö µÈ »çÇ×)
	 * 2) 1¾ï ÀÌ»ó ´ëÃâ ºÒ°¡ 
	 * 3) ÀºÇà¿¡ ÀÖ´Â µ·º¸´Ù Å©¸é ´ëÃâ ºÒ°¡
	 * 4) ´ëÃâÀÌ °¡´ÉÇÑ »óÅÂ¶ó¸é °¡ÀÔ ÁøÇà
	 * 5) ÇØ´ç ±Ý¾×¿¡ ´ëÇØ¼­ ´ëÃâ
	 * 6) ÀºÇà¿¡ ÀÖ´Â µ·ÀÌ 0 ÀÌ¸é ½Ã½ºÅÛ Á¾·á
	 * 
	 * @param name
	 * @param phoneNumber
	 * @param money
	 */
	public void checkInputMoney( String name, String phoneNumber, int money ) { // 
		String dambo = scan.inputScanner();
		if(scan.checkScanner("^[°¡-ÆRa-zA-Z]*$", dambo)){ // ´ãº¸¿¡ ´ëÇÑ Ã¼Å©
			System.out.println("ÀçÀÔ·Â");
		}
		else if (money > bank.MAX_LOAN){ // 1¾ï ÀÌ»ó ºô¸®¸é ÀçÀÔ·Â
			System.out.println("1¾ï ±îÁö¸¸ ºô¸± ¼ö ÀÖ½À´Ï´Ù.");
		}
		else if(money > bank.getTotalMoney()) { // ÀºÇà¿¡ ÀÖ´Â µ·º¸´Ù ´ëÃâÇÏ·Á´Â µ·ÀÌ Å©¸é
			System.out.println("ÀºÇà¿¡ µ·ÀÌ ¸ðÀÚ¸¨´Ï´Ù.");
		}
		else {
			Date curDate = new Date();
			Calendar now = Calendar.getInstance();
			long dateTime = now.getTimeInMillis();
			CustomerVO customer = new CustomerVO();
			
			customer.setName(name);
			customer.setPhoneNumber(phoneNumber);
			//customer.setMoney(money);
			customer.setDambo(dambo);
			customer.setLoanTime(curDate);
			customer.setMillisTime(dateTime);
			customer.setLoanMoney(money);
			
			this.customerList.add(customer);
			System.out.println("ºô¸° ½Ã°£ : " + customer.getLoanTime()); // °¡ÀÔ (´ëÃâ ÁøÇà)
			
			int out = bank.getTotalMoney() - money; // ÀºÇàµ·¿¡¼­ ºô¸°µ· »©
			bank.setTotalMoney(out); // ±×µ·À» ÀºÇà ÃÑ±Ý¾×¿¡ ³Ö¾î
			System.out.println(money + "¿øÀÇ µ·À» ºô·È½À´Ï´Ù.");
			
			if ( bank.getTotalMoney() == 0 ) {
				System.exit(0); // ÀºÇàµ·ÀÌ 0¿øÀÌ¸é Á¾·á
			}
		}
	}
	
	/**
	 * ÀÌ¸§À» ¹Þ¾Æ ÆÄ»êÇÏ´Â ¸Þ¼Òµå
	 * ÇÁ·Î¼¼½º
	 * 1) customerList¿¡ ¿øÇÏ´Â °í°´ Á¤º¸°¡ ÀÖ´ÂÁö Á¶È¸
	 * 2) ÀÖ´Ù¸é nameCheck = true, ÇØ´ç °í°´ Á¤º¸¸¦ ÀÓ½Ã ÀúÀå
	 * 3) ¾ø´Ù¸é nameCheck = false
	 * 3) Á¶°Ç ¹®¿¡ µû¶ó¼­ °í°´ÀÇ ´ãº¸ Á¤º¸¸¦ Ãâ·ÂÇÏ°í customerList¿¡¼­ »èÁ¦
	 * @param deleteName
	 */
	public void bankruptcy(String deleteName) { // ÆÄ»êÇÏ´Â ¸Þ¼Òµå
		
		boolean nameCheck = false;
		CustomerVO checkedCustomer = new CustomerVO();
		
		for ( CustomerVO customer : this.customerList ) {
			if ( customer.getName().equals(deleteName) ){
				checkedCustomer = customer;
				nameCheck =  true;
			}
		}
		nameCheck = false;
		
		if ( this.setResult(nameCheck) ){ //Á¸ÀçÇÏ¸é
				System.out.println("´ç½ÅÀÇ ´ãº¸ " + checkedCustomer.getDambo() + "´Â ³»°¡ °¡Á®°£´Ù." );// ´ãº¸ »¯±â
				this.customerList.remove(checkedCustomer); // ±â·Ï »èÁ¦
				System.out.println("Á¤º¸»èÁ¦´Â ÇØÁÙ°Ô");
		}
		else{ //ÀÌ¸§ÀÌ Á¸ÀçÇÏÁö¾ÊÀ¸¸é
			System.out.println(deleteName+"ÀÇ Á¤º¸°¡ ¾ø½À´Ï´Ù.\n");
		}//else
	}
	
	/**
	 * ÀÌ¸§À» ÀÔ·ÂÇÏ¿© ´ëÃâ ³»¿ªÀ» È®ÀÎ
	 * ÇÁ·Î¼¼½º
	 * 1) customerList¿¡ ¿øÇÏ´Â °í°´ Á¤º¸°¡ ÀÖ´ÂÁö Á¶È¸
	 * 2) ÀÖ´Ù¸é nameCheck = true, ÇØ´ç °í°´ Á¤º¸¸¦ ÀÓ½Ã ÀúÀå
	 * 3) ¾ø´Ù¸é nameCheck = false
	 * 3) Á¶°Ç ¹®¿¡ µû¶ó¼­ °í°´ Á¤º¸ Ãâ·Â È¤Àº °í°´ Á¤º¸ ¾øÀ½ ¸Þ¼¼Áö Ãâ·Â
	 * @param searchName
	 */
	public void searchMyInfo(String searchName) { // ³»°¡ ºô¸° µ·ÀÇ Á¤º¸¸¦ Ã£´Â´Ù.
		
		boolean nameCheck = false;
		CustomerVO selectedCustomer = new CustomerVO();
		
		for ( CustomerVO customer : this.customerList ) {
			if ( customer.getName().equals(searchName) ){
				selectedCustomer = customer;
				nameCheck =  true;
			}
		}
		nameCheck = false;
		
		if ( this.setResult(nameCheck)) { 
			this.printInfo(selectedCustomer);//ÇØ´çÇÏ´Â Á¤º¸ Ãâ·Â
			System.out.println("");
		}
		else { 
			System.out.println(searchName + "ÀÇ °í°´ Á¤º¸°¡ ¾ø½À´Ï´Ù.");
		}
	}
	
	/**
	 * ºô¸° µ·À» °±´Â ¸Þ¼Òµå
	 * ÇÁ·Î¼¼½º
	 * 1) °±°íÀÚ ÇÏ´Â »ç¶÷ÀÇ Á¤º¸ È®ÀÎ
	 * 2) °±¾Æ¾ßÇÒ µ· °è»ê ( ÀüÃ¼ ´ëÃâ ±Ý¾× Áß °±Àº ±Ý¾× Á¦¿Ü)
	 * 3) °±À» ±Ý¾×ÀÌ 0ÀÌ µÉ ¶§ ±îÁö ¹Ýº¹ÇÏ¿© °±À» µ·À» ÀÔ·ÂÇÑ´Ù.
	 * @param searchName
	 * @return
	 */
	public boolean returnMoney( String searchName ) { // µ· °±À» ¶§ 
		boolean nameCheck = false;
		CustomerVO selectedCustomer = new CustomerVO();
		System.out.println("¾ó¸¶¸¦ °±À» °Ç°¡¿ä?");
		int money = scan.inputScannerInt();
		
		for ( CustomerVO customer : this.customerList ) {
			if ( customer.getName().equals(searchName) ){
				selectedCustomer = customer;
				nameCheck =  true;
			}
		}
		nameCheck = false;
		
		if (this.setResult(nameCheck)) {
			this.printInfo(this.getInfo(searchName)); // Ã£ÀºÁ¤º¸ Ãâ·Â
			
			Calendar when = Calendar.getInstance();
			long time = when.getTimeInMillis();
			long result = ((time - selectedCustomer.getMillisTime()) / 1000);
			int sc = (int)Math.round((double)result);
			double down = Math.floor(sc/5); // ¼Ò¼öÁ¡ ³»¸²
			double pow = Math.pow((1+bank.RATE),down);
			int totalLoan = (int)(selectedCustomer.getLoanMoney() * pow);
			
			int loan = totalLoan	-  this.getInfo(searchName).getRepayMoney(); // °±¾Æ¾ßÇÒ µ· °è»ê
			System.out.println("");
			bank.printBankInfo();// ÀºÇà Á¤º¸ Ãâ·Â
			if (money > loan) { // °±¾Æ¾ßÇÒ µ·º¸´Ù ¸¹À¸¸é
				System.out.println("±×·¸°Ô ¸¹ÀÌ ¾ÈÁàµµ µÇ´Âµ¥...;;");
			} else if (money == loan) {
				System.out.println("µ·À» ÀüºÎ °±À¸¼Ì½À´Ï´Ù.");
				
				selectedCustomer.setRepayMoney(money); // °í°´ÀÌ °±Àº µ· ½×±â
				bank.setTotalMoney(bank.getTotalMoney() + money); // ÀºÇà¿¡ °±Àº µ· ¸¸Å­ ÃÑ±Ý¾×¿¡ Ãß°¡
				System.out.println(money + "¸¸Å­ÀÇ µ·À» °±¾Ò½À´Ï´Ù.");
				
				this.getCustomerList().remove(this.getInfo(searchName)); // ´Ù°±¾ÒÀ¸´Ï
																				// Á¤º¸»èÁ¦
				System.out.println("Á¤º¸°¡ »èÁ¦µÇ¾ú½À´Ï´Ù.\n");
			} else {
				selectedCustomer.setRepayMoney(money); // °í°´ÀÌ °±Àº µ· ½×±â
				bank.setTotalMoney(bank.getTotalMoney() + money); // ÀºÇà¿¡ °±Àº µ· ¸¸Å­ ÃÑ±Ý¾×¿¡ Ãß°¡
				System.out.println(money + "¸¸Å­ÀÇ µ·À» °±¾Ò½À´Ï´Ù.");
				bank.printBankInfo();
				System.out.println("");
			}
			return true;
		} else {
			return false;
		}
	}
	
	/**
	 * ÀÌ¹Ì Á¸ÀçÇÏ´Â °í°´ÀÎÁö Ã¼Å©
	 * @param searchName ÀÔ·Â¹ÞÀº ÀÌ¸§
	 * @return
	 */
	public boolean checkName ( String searchName ){ 
		boolean nameCheck = false;
		
		for ( CustomerVO customer : this.customerList ) {
			if ( customer.getName().equals(searchName) ){
				nameCheck =  true;
			}
		}
		nameCheck = false;
		
		if ( this.setResult(nameCheck)) { 
			System.out.println("ÀÌ¹Ì Á¸ÀçÇÏ´Â °í°´ÀÔ´Ï´Ù.");
			return false;
		}
		else { 
			return true;
		}
		
	}

	/**
	 * Á¤º¸ Ãâ·Â
	 * @param customer
	 */
	public void printInfo(CustomerVO customer){
		System.out.println("ÀÌ¸§ : " + customer.getName());
		System.out.println("ÀüÈ­¹øÈ£ : " + customer.getPhoneNumber());
		System.out.println("´ëÃâ±Ý¾× : " + customer.getLoanMoney());
		System.out.println("°±Àº ±Ý¾× :" + customer.getRepayMoney());
		System.out.println("´ãº¸ : " + customer.getDambo());
		System.out.println("´ëÃâ½Ã°£ : " + customer.getLoanTime());
	}
	
	/**
	 * ÇØ´ç°í°´Á¤º¸°¡Á®¿À±â
	 * @param name
	 * @return
	 */
	public CustomerVO getInfo( String name ) {
		CustomerVO selectedCustomer = new CustomerVO();
		for ( CustomerVO customer : this.customerList ) {
			if ( customer.getName().equals(name)){
				selectedCustomer = customer;
				return selectedCustomer;
			}
		}
		return new CustomerVO();
	}
	
}
