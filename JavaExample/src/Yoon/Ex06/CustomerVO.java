package Yoon.Ex06;

import java.util.Date;

public class CustomerVO {

	private String name;
	private String phoneNumber;
	private int loanMoney; // ºô¸°µ·
	private String dambo; // ´ãº¸
	private Date loanTime; //Ãâ·Â¿ë ½Ã°£
	private long millisTime; // °è»ê¿ë ½Ã°£
	private int repayMoney;//°±Àºµ·
	
	public long getMillisTime() {
		return millisTime;
	}
	public void setMillisTime(long millisTime) {
		this.millisTime = millisTime;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPhoneNumber() {
		return phoneNumber;
	}
	public void setPhoneNumber(String phoneNumber) {
		this.phoneNumber = phoneNumber;
	}

	public Date getLoanTime() {
		return loanTime;
	}
	public void setLoanTime(Date loanTime) {
		this.loanTime = loanTime;
	}
	public int getLoanMoney() {
		return loanMoney;
	}
	public void setLoanMoney(int loanMoney) {
		this.loanMoney = loanMoney;
	}
	public String getDambo() {
		return dambo;
	}
	public void setDambo(String dambo) {
		this.dambo = dambo;
	}
	public int getRepayMoney() {
		return repayMoney;
	}
	public void setRepayMoney(int repayMoney) {
		this.repayMoney = this.repayMoney + repayMoney; // °±À»¶§ ¸¶´Ù ½×¾Æ°£´Ù.
	}

}
