CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Analysis
 * Design
 * Maintainers

INTRODUCTION
------------

The program functions as a simple password validator. The is the first individual assignment for coursework grade in the academic program: Programming Techniques - ITT103

REQUIREMENTS
------------
The requirement is that the enduser is familiar with running python scripts or running programs from the command line or in an IDE of choice. 

*Application and Software Requirements:
	*Python 3 installed
	*IDE with python configured
	*Some administrator privileges in the event that you need to install an IDE

INSTALLATION
------------

Install as you would normally run a python script or load the file in your preferred IDE and click the 'build and run' or the 'run' option from your IDE menu. 

The same can be achieved from the command line. 

ANALYSIS 
--------

The user enters a password, the tool then validates if it meets the below requirements and then  notifies the enduser that the password is either valid or invalid.

* A password must have at least eight characters.
* A password consists of only letters and digits.
* A password must contain at least two digits.

The password validator tool had three simple requirements. 
These requirements were tested thoroughly in attempt to break the program and to prove completeness:

The program was tested to ensure that the string entered by the user met the minimum required length.
The program was tested to ensure that it contained only letters and numbers. If the user entered a special character the program would throw an error.
The program was tested to ensure that it had at least two numbers in the password. 

One of the challenges was to ensure that that password entered would not pass with just eight to more numbers only. 


DESIGN 
------

PROGRAM Validator
START
	PRINT  welcome message
	PRINT  password requirements 
	GET password from user
	SAVE user password
	WHILE password is not the string 'exit' THEN
		IF length of password is less than 8 THEN
			PRINT "Invalid Password"
		ELSE IF password contains special characters THEN
			PRINT "Invalid Password"
		ELSE IF there are less than 2 numbers in password THEN
			PRINT "Invalid Password"
		ELSE IF password contains only numbers THEN
			PRINT "Invalid Password"
		ELSE
			PRINT "Password is valid"
		END Loop
STOP


MAINTAINERS
-----------

Current maintainers:
 * Camarly Thomas (UCC) - https://github.com/camarly
	* Please note that this code will not be developed further unless it is a requirement in the course: Programming Techniques - ITT103.
 
