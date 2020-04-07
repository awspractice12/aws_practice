package com.sscloudpoc.account.business.util;

import java.util.Date;

import com.sscloudpoc.account.business.domain.AccountTO;
import com.sscloudpoc.account.data.entity.Account;

public class Util {
	//------------------------------------------------------------------------------------
	public static AccountTO convertEntityToDTO(Account entity) {
		AccountTO to = new AccountTO();
		to.setAccountId        (entity.getId               ());
		to.setCustomerId       (entity.getCustomerId       ());
		to.setAccountType      (entity.getAccountType      ());
		to.setInterestRate     (entity.getInterestRate     ());
		to.setBalance          (entity.getBalance          ());
		to.setLastModifiedDate (entity.getLastModifiedDate ());
		return to;
	}
	
	public static Account convertDTOToEntity(AccountTO to) {
		Account entity = new Account();
		entity.setId               (to.getAccountId        ());
		entity.setCustomerId       (to.getCustomerId       ());
		entity.setAccountType      (to.getAccountType      ());
		entity.setInterestRate     (to.getInterestRate     ());
		entity.setBalance          (to.getBalance          ());
		entity.setLastModifiedDate (to.getLastModifiedDate ());
		return entity;
	}
	//------------------------------------------------------------------------------------
	//------------------------------------------------------------------------------------
	//------------------------------------------------------------------------------------
}


