package com.sscloudpoc.account.business.service;

import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.cloud.client.ServiceInstance;
import org.springframework.stereotype.Service;

import com.sscloudpoc.account.business.domain.AccountTO;
import com.sscloudpoc.account.business.util.Util;
import com.sscloudpoc.account.data.entity.Account;
import com.sscloudpoc.account.data.repository.AccountRepository;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Service
public class AccountService {
	
	private AccountRepository  accountRepository;

    @Autowired
    public AccountService(AccountRepository accountRepository) {
        this.accountRepository = accountRepository;
    }
	//-------------------------------------------------------------------------------------------
    public List<AccountTO> getAllAccounts(){
		try {
			System.out.println("AccountService.getAllRoutes() ************** entering");
			List<AccountTO> returnAccounts = new ArrayList<>();
			Iterable<Account> accounts = this.accountRepository.findAll();
			
			accounts.forEach(account->{
				AccountTO accountTO = Util.convertEntityToDTO(account);
				//System.out.println("routeTO = "+routeTO);
				returnAccounts.add(accountTO);
			});
			
			return returnAccounts;
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException();
		}
    }
	//-------------------------------------------------------------------------------------------
    public AccountTO getAccountById(long id){
		//System.out.println("AccountService.getRouteById() ************** entering");
        Account account = this.accountRepository.findById(id).get();
        AccountTO accountTO = Util.convertEntityToDTO(account);
        //System.out.println("routeTO = "+routeTO);
        
        return accountTO;
    }
	//-------------------------------------------------------------------------------------------
    public List<AccountTO> getAccountByCustomerId(long id){
		//System.out.println("AccountService.getRouteById() ************** entering");
		List<AccountTO> returnAccounts = new ArrayList<>();
    	List<Account> accountList = this.accountRepository.findByCustomerId(id);

    	accountList.forEach(account->{
			AccountTO accountTO = Util.convertEntityToDTO(account);
			returnAccounts.add(accountTO);
		});
    	return returnAccounts;
    }
	//-------------------------------------------------------------------------------------------
    public AccountTO saveAccount(AccountTO accountTO){
		//System.out.println("AccountService.saveRoute() ************** entering");
        Account entity = Util.convertDTOToEntity(accountTO);
        entity.setLastModifiedDate(new Date());
        //System.out.println("AccountService.saveRoute():routeTO = "+routeTO);
		Account entity2 = this.accountRepository.save(entity);
        return Util.convertEntityToDTO(entity2);
    }
	//-------------------------------------------------------------------------------------------
    public void deleteAccount(long id){
		//System.out.println("AccountService.deleteRoute() ************** entering");
		this.accountRepository.deleteById(id);
    }
	//-------------------------------------------------------------------------------------------
    public void deleteAllAccounts(){
		//System.out.println("AccountService.deleteAllRoutes() ************** entering");
		this.accountRepository.deleteAll();
    }
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
}
