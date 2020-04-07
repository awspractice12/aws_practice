package com.sscloudpoc.customer.data.repository;

import org.springframework.data.repository.CrudRepository;
import com.sscloudpoc.customer.data.entity.Customer;
import org.springframework.stereotype.Repository;

@Repository
public interface CustomerRepository extends CrudRepository<Customer, Long> {

}