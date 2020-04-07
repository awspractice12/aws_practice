package com.sscloudpoc.customer.business.domain;

import java.util.ArrayList;
import java.util.List;

public class CustomerListTO {

	private List<CustomerTO> customerList = new ArrayList<CustomerTO>();

	public List<CustomerTO> getCustomerList() {
		return customerList;
	}

	public void setCustomerList(List<CustomerTO> customerList) {
		this.customerList = customerList;
	}

	@Override
	public String toString() {
		return "CustomerListTO [customerList=" + customerList + "]";
	}
	
}
