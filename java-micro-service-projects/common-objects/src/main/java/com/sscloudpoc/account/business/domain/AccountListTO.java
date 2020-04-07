package com.sscloudpoc.account.business.domain;

import java.util.ArrayList;
import java.util.List;

public class AccountListTO {
	private List<AccountTO> accountList = new ArrayList<AccountTO>();

	public List<AccountTO> getAccountList() {
		return accountList;
	}

	public void setAccountList(List<AccountTO> accountList) {
		this.accountList = accountList;
	}

	@Override
	public String toString() {
		return "AccountListTO [accountList=" + accountList + "]";
	}

}
