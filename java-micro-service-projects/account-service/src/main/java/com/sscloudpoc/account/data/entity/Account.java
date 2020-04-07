package com.sscloudpoc.account.data.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.Date;

@Entity
@Table(schema="BANK", name="ACCOUNT")
public class Account {
    @Id
    @Column(name="ACCOUNT_ID")
    @GeneratedValue(strategy= GenerationType.AUTO)
    private long id;
	
    @Column(name="CUSTOMER_ID")
    private long customerId;
	
    @Column(name="ACCOUNT_TYPE")
    private String accountType;
	
    @Column(name="INTEREST_RATE")
    private long interestRate;
    
	@Column(name="BALANCE")
    private long balance;

	@Column(name="LAST_MODIFIED_DATETIME")
    private Date lastModifiedDate;

	
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
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

	public long getCustomerId() {
		return customerId;
	}

	public void setCustomerId(long customerId) {
		this.customerId = customerId;
	}

}
