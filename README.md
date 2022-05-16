# GoHealth_test
Python  app for reading JSON 

GoHealth_test.py contains code for parsing Json
1) Carrier name is one of the options ‘Humana, WellCare, Anthem’. 
   code is checking are the name, and if it's wrong print error message
 
 2) Effective date is not empty and is in the desired format: year-month-day.
    String date I make datetime for python, and if format is not y-m-d it's  print error message 
    
  3) Plan id only contains numbers and ‘-’ sign
    Code is reading it, and if it's not contains numbers and ‘-’ sign, it just don't print anything
   
   4) Plan name contains plan id.
      Code is only prints Plan ID 
      
   5) Submission Attempt Count is not higher than 5.
       If Submission Attempt Count hieger than 5 code print error message
       
   
= Test_login.py =  
Here I made simple automated test for entering login info and press enter button to see error messages

= Answers for questions =

1. Describe your understanding of the term 'Specification by example'.
   Specification by example is  a way to quickly come up with requirements in test-cases, using examples to clarify things early. 

2. What content makes good bug report?
   Clear and understanding title 
   Informative description
   Clear steps to replicate the issue

3. What content makes good test run report?
	Detailed description of the testing activity
	Information in the test report should be short and clearly understandable



