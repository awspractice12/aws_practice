package com.sscloudpoc.customer.data.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.Date;

@Entity
@Table(schema="BANK", name="CUSTOMER")
public class Customer {
    @Id
    @Column(name="CUSTOMER_ID")
    @GeneratedValue(strategy= GenerationType.AUTO)
    private long id;
	
	@Column(name="CUSTOMER_NAME")
    private String customerName;
	
	@Column(name="LAST_MODIFIED_DATETIME")
    private Date lastModifiedDate;

    public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getCustomerName() {
		return customerName;
	}

	public void setCustomerName(String customerName) {
		this.customerName = customerName;
	}

	public Date getLastModifiedDate() {
		return lastModifiedDate;
	}

	public void setLastModifiedDate(Date lastModifiedDate) {
		this.lastModifiedDate = lastModifiedDate;
	}

}
