connect 'jdbc:derby://localhost:1527/metrodb;create=true;traceFile=trace.out;user=shibu;password=shibu';


---------------------------------------------------------------------------------------------------------
DROP TABLE BANK.ACCOUNT;
DROP SEQUENCE hibernate_sequence restrict;
--DROP PUBLIC SYNONYM hibernate_sequence;

---------------------------------------------------------------------------------------------------------
drop schema bank restrict;
create schema bank;

---------------------------------------------------------------------------------------------------------
CREATE TABLE BANK.ACCOUNT (
  ACCOUNT_ID               INTEGER PRIMARY KEY,
  CUSTOMER_ID              INTEGER NOT NULL,
  ACCOUNT_TYPE             VARCHAR(100),
  INTEREST_RATE            INTEGER NOT NULL,
  BALANCE                  INTEGER NOT NULL,
  LAST_MODIFIED_DATETIME   DATE  DEFAULT CURRENT_DATE
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
