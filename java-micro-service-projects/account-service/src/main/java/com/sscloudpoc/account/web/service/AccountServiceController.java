package com.sscloudpoc.account.web.service;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.sscloudpoc.account.business.domain.AccountListTO;
import com.sscloudpoc.account.business.domain.AccountTO;
import com.sscloudpoc.account.business.service.AccountService;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@RestController
public class AccountServiceController {

    @Autowired
    private AccountService accountService;
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.GET, value="/account/all")
    public AccountListTO getAllRoutes() throws Exception {
		try {
			List<AccountTO> accounts = this.accountService.getAllAccounts();
			AccountListTO accountList = new AccountListTO();
			accountList.setAccountList(accounts);
			System.out.println("AccountServiceController.getAllAccounts() ***accounts="+accounts);
			return accountList;
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException();
		}
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.GET, value="/account/{id}")
    public AccountTO getAccountById(@PathVariable(value="id")String id) throws Exception {
		AccountTO account = this.accountService.getAccountById(Long.valueOf(id));
		//System.out.println("AccountServiceController.getRouteById() ***route="+account);
        return account;
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.GET, value="/accountByCustomer/{id}")
    public AccountListTO getAccountByCustomerId(@PathVariable(value="id")String id) throws Exception {
		List<AccountTO> accountList = this.accountService.getAccountByCustomerId(Long.valueOf(id));
		//System.out.println("AccountServiceController.getRouteById() ***route="+account);
		AccountListTO accountListTO = new AccountListTO();
		accountListTO.setAccountList(accountList);
		System.out.println("AccountServiceController.getAllAccounts() ***accounts="+accountListTO);
		return accountListTO;
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.POST, value="/account/save")
    public void saveAccount(@RequestBody AccountTO accountTO) throws Exception {
		//System.out.println("AccountServiceController.saveRoute():***routeTO="+accountTO);
		AccountTO dto = this.accountService.saveAccount(accountTO);
		//System.out.println("AccountServiceController.saveRoute():***dto="+dto);
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.DELETE, value="/account/{id}")
    public void deleteAccount(@PathVariable(value="id")String id) throws Exception {
		//System.out.println("AccountServiceController.deleteRoute():***id="+id);
		this.accountService.deleteAccount(Long.valueOf(id));
		//System.out.println("AccountServiceController.deleteRoute():***dto=");
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.DELETE, value="/account/deleteAll")
    public void deleteAllAccounts() throws Exception {
		//System.out.println("AccountServiceController.deleteAllRoutes().enter");
		this.accountService.deleteAllAccounts();
		//System.out.println("AccountServiceController.deleteAllRoutes().exit");
    }
    //------------------------------------------------------------------------------------------------------------------------------
    
}
