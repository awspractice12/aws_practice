package com.sscloudpoc.account.business.domain;

import java.util.Date;

public class AccountTO {
    private long   accountId           ;
    private long   customerId          ;
	private String accountType         ;
    private long   interestRate        ;
    private long   balance             ;
    private Date   lastModifiedDate    ;
    
	public long getAccountId() {
		return accountId;
	}
	public void setAccountId(long accountId) {
		this.accountId = accountId;
	}
    public long getCustomerId() {
		return customerId;
	}
	public void setCustomerId(long customerId) {
		this.customerId = customerId;
	}
	public String getAccountType() {
		return accountType;
	}
	public void setAccountType(String accountType) {
		this.accountType = accountType;
	}
	public long getInterestRate() {
		return interestRate;
	}
	public void setInterestRate(long interestRate) {
		this.interestRate = interestRate;
	}
	public long getBalance() {
		return balance;
	}
	public void setBalance(long balance) {
		this.balance = balance;
	}
	public Date getLastModifiedDate() {
		return lastModifiedDate;
	}
	public void setLastModifiedDate(Date lastModifiedDate) {
		this.lastModifiedDate = lastModifiedDate;
	}
	@Override
	public String toString() {
		return "AccountTO [accountId=" + accountId + ", customerId=" + customerId + ", accountType=" + accountType
				+ ", interestRate=" + interestRate + ", balance=" + balance + ", lastModifiedDate=" + lastModifiedDate
				+ "]";
	}
}
