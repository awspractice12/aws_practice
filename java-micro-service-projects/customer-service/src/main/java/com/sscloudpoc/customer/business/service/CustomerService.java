package com.sscloudpoc.customer.business.service;

import com.sscloudpoc.customer.business.domain.CustomerTO;
import com.sscloudpoc.customer.business.util.Util;
import com.sscloudpoc.customer.data.entity.Customer;
import com.sscloudpoc.customer.data.repository.CustomerRepository;
import com.sscloudpoc.customer.business.domain.CustomerTO;
import com.sscloudpoc.customer.data.repository.CustomerRepository;

import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.cloud.client.ServiceInstance;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

@Service
public class CustomerService {
	
	private CustomerRepository  customerRepository;

    @Autowired
    public CustomerService(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }
	//-------------------------------------------------------------------------------------------
    public List<CustomerTO> getAllCustomers(){
		try {
			System.out.println("CustomerService.getAllCustomers() ************** entering");
			List<CustomerTO> returnCustomers = new ArrayList<>();
			Iterable<Customer> customers = this.customerRepository.findAll();
			
			customers.forEach(customer->{
				CustomerTO customerTO = Util.convertEntityToDTO(customer);
				//System.out.println("customerTO = "+customerTO);
				returnCustomers.add(customerTO);
			});
			
//			System.out.println("CustomerService.getAllCustomers() ************** discoveryClient="+discoveryClient);
//			List<ServiceInstance> instances=discoveryClient.getInstances("METRO-TRAIN-SERVICE");
//			System.out.println("CustomerService.getAllCustomers() ************** instances="+instances);
//			ServiceInstance serviceInstance=instances.get(0);
//			String baseUrl=serviceInstance.getUri().toString(); 
//			System.out.println("CustomerService.getAllCustomers() ************** baseUrl="+baseUrl);
			
			return returnCustomers;
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException();
		}
    }
	//-------------------------------------------------------------------------------------------
    public CustomerTO getCustomerById(long id){
		System.out.println("CustomerService.getCustomerById() ************** entering");
        Customer customer = this.customerRepository.findById(id).get();
        CustomerTO customerTO = Util.convertEntityToDTO(customer);
        //System.out.println("customerTO = "+customerTO);
        
        return customerTO;
    }
	//-------------------------------------------------------------------------------------------
    public CustomerTO saveCustomer(CustomerTO customerTO){
		System.out.println("CustomerService.saveCustomer() ************** entering");
        Customer entity = Util.convertDTOToEntity(customerTO);
        entity.setLastModifiedDate(new Date());
        //System.out.println("CustomerService.saveCustomer():customerTO = "+customerTO);
		Customer entity2 = this.customerRepository.save(entity);
        return Util.convertEntityToDTO(entity2);
    }
	//-------------------------------------------------------------------------------------------
    public void deleteCustomer(long id){
		System.out.println("CustomerService.deleteCustomer() ************** entering");
		this.customerRepository.deleteById(id);
    }
	//-------------------------------------------------------------------------------------------
    public void deleteAllCustomers(){
		System.out.println("CustomerService.deleteAllCustomers() ************** entering");
		this.customerRepository.deleteAll();
    }
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
	//-------------------------------------------------------------------------------------------
}
