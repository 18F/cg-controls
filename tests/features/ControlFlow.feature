Feature: Access Control Flow

  Background:
    Given an application
      And a security group that is open to all public outgoing connections
      And a security group that closes all outgoing tcp connections

  Scenario: View Application Security Groups
   Given I am using a master account
     then I can view and print all the ASGs


   Scenario: Close Application Security Group
     Given I am using a master account
       when I bind the application security group with closed settings to the running app
       then the application cannot ping an external site


 Scenario: Open Application Security Group
   Given I am using a master account
     when I bind the application security group with open settings to the running app
     then the application can ping an external site
