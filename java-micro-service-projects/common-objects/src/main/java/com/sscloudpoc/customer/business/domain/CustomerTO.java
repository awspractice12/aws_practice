package com.sscloudpoc.customer.business.domain;

import java.util.Date;
import java.util.List;
import com.sscloudpoc.account.business.domain.AccountTO;

public class CustomerTO {
    private long            customerId          ;
    private String          customerName        ;
    private List<AccountTO> accountList         ;
    private Date            lastModifiedDate    ;

    public long getCustomerId() {
		return customerId;
	}
	public void setCustomerId(long customerId) {
		this.customerId = customerId;
	}
	public String getCustomerName() {
		return customerName;
	}
	public void setCustomerName(String customerName) {
		this.customerName = customerName;
	}
	public List<AccountTO> getAccountList() {
		return accountList;
	}
	public void setAccountList(List<AccountTO> accountList) {
		this.accountList = accountList;
	}
	public Date getLastModifiedDate() {
		return lastModifiedDate;
	}
	public void setLastModifiedDate(Date lastModifiedDate) {
		this.lastModifiedDate = lastModifiedDate;
	}
	@Override
	public String toString() {
		return "CustomerTO [customerId=" + customerId + ", customerName=" + customerName + ", accountList="
				+ accountList + ", lastModifiedDate=" + lastModifiedDate + "]";
	}
}
