connect 'jdbc:derby://localhost:1527/metrodb;create=true;traceFile=trace.out;user=shibu;password=shibu';



DROP TABLE BANK.CUSTOMER;
DROP SEQUENCE hibernate_sequence restrict;
--DROP PUBLIC SYNONYM hibernate_sequence;

drop schema BANK restrict;



create schema BANK;


CREATE TABLE BANK.CUSTOMER (
  CUSTOMER_ID             INTEGER PRIMARY KEY,
  CUSTOMER_NAME           VARCHAR(100),
  LAST_MODIFIED_DATETIME DATE  DEFAULT CURRENT_DATE
);

---------------------------------------------------------------------------------------------------------
--This sequence is required by Hibernate for AUTO_INCREMENTING columns across the application
CREATE SEQUENCE hibernate_sequence
  INCREMENT BY 1
  MINVALUE 1
  MAXVALUE 2147483647
;

--CREATE PUBLIC SYNONYM hibernate_sequence FOR BANK.hibernate_sequence;
---------------------------------------------------------------------------------------------------------
