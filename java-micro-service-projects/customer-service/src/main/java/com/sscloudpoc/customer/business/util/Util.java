package com.sscloudpoc.customer.business.util;

import com.sscloudpoc.customer.business.domain.CustomerTO;
import com.sscloudpoc.customer.data.entity.Customer;

import java.util.Date;

public class Util {
	//------------------------------------------------------------------------------------
	public static CustomerTO convertEntityToDTO(Customer entity) {
		CustomerTO to = new CustomerTO();
		to.setCustomerId       (entity.getId               ());
		to.setCustomerName     (entity.getCustomerName     ());
		to.setLastModifiedDate (entity.getLastModifiedDate ());
		return to;
	}
	
	public static Customer convertDTOToEntity(CustomerTO to) {
		Customer entity = new Customer();
		entity.setId               (to.getCustomerId       ());
		entity.setCustomerName     (to.getCustomerName     ());
		entity.setLastModifiedDate (to.getLastModifiedDate ());
		return entity;
	}
	//------------------------------------------------------------------------------------
	//------------------------------------------------------------------------------------
	//------------------------------------------------------------------------------------
	//------------------------------------------------------------------------------------
}
