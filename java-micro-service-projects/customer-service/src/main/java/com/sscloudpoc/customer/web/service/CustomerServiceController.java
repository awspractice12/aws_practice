package com.sscloudpoc.customer.web.service;




import java.util.List;

import org.springframework.web.client.RestTemplate;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.sscloudpoc.account.business.domain.AccountListTO;

import com.sscloudpoc.customer.business.domain.CustomerListTO;
import com.sscloudpoc.customer.business.domain.CustomerTO;
import com.sscloudpoc.customer.business.service.CustomerService;

@RestController
public class CustomerServiceController {
	@Value("${account.server.url.base}") //working because of @Controller
	private String accountServerUrlBase;	

    @Autowired
    private CustomerService customerService;
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.GET, value="/customer/all")
    public CustomerListTO getAllCustomers() throws Exception {
		try {
			List<CustomerTO> routes = this.customerService.getAllCustomers();
			CustomerListTO custList = new CustomerListTO();
			custList.setCustomerList(routes);
			System.out.println("RouteServiceController.getAllRoutes() ***routes="+routes);
			return custList;
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException();
		}
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.GET, value="/customer/{id}")
    public CustomerTO getCustomerById(@PathVariable(value="id")String id) throws Exception {
		CustomerTO customerTO = this.customerService.getCustomerById(Long.valueOf(id));
		//System.out.println("RouteServiceController.getRouteById() ***route="+route);
		
		
        RestTemplate restTemplate = new RestTemplate();

       	String uri = accountServerUrlBase+"/accountByCustomer/"+id;
		System.out.println("Customer-to-Account-Web-Service call to : "+uri);
		AccountListTO accountListTO = restTemplate.getForObject(uri, AccountListTO.class);

		customerTO.setAccountList(accountListTO.getAccountList());
        return customerTO;
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.POST, value="/customer/save")
    public void saveCustomer(@RequestBody CustomerTO customerTO) throws Exception {
		//System.out.println("RouteServiceController.saveRoute():***routeTO="+routeTO);
		CustomerTO dto = this.customerService.saveCustomer(customerTO);
		//System.out.println("RouteServiceController.saveRoute():***dto="+dto);
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.DELETE, value="/customer/{id}")
    public void deleteCustomer(@PathVariable(value="id")String id) throws Exception {
		//System.out.println("RouteServiceController.deleteRoute():***id="+id);
		this.customerService.deleteCustomer(Long.valueOf(id));
		//System.out.println("RouteServiceController.deleteRoute():***dto=");
    }
    //------------------------------------------------------------------------------------------------------------------------------
    @RequestMapping(method= RequestMethod.DELETE, value="/customer/deleteAll")
    public void deleteAllCustomer() throws Exception {
		//System.out.println("RouteServiceController.deleteAllRoutes().enter");
		this.customerService.deleteAllCustomers();
		//System.out.println("RouteServiceController.deleteAllRoutes().exit");
    }
    //------------------------------------------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------------------------------------------
    //------------------------------------------------------------------------------------------------------------------------------
    
}
