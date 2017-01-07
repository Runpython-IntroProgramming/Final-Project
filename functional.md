Currency Converter


## Functional Specification
The goal of this program is essentially to be able to convert from one currency to another based on current exchange rates. A user of the program can enter a currency and an amount and can convert that amount from that currency to any other currency. 

The user can access the program via runpython.com. 

The program involves no graphics or mouse input, but does involve keyboard input. The user of the program must enter in a currency and an amount to convert. Then the user must always enter in a currency that they would like to convert to. After the first input by the user, the name of a currency, the program goes to the dictionary containing the exchange rates for that currency. Then the user enters the amount they would like to convert, and the currency they would like to convert to. The program finds the exchange rate for that currency based on the first currency entered, and multiples the exchange rate by the currency. That is how the program responds to keyboard input. No graphical assets are used, this is simply a program using the vast computational power of python 3. The user does not need to do anything to install the program. 



This document should become the functional specification of the project you are working on.

A functional specification describes in great detail how a device or program will appear to an
outside user. That is, it treats all hardware as a "black box", the contents of which are completely
unknown to the user. The functional specification should include sections with the following information:

Your specification **should include** the following types of information:

* A title. Replace the title at the beginning of this document.
* Summary or introduction. In general, in a few lines or less, what is your program about or what is it about?
* How does the user access your program? Is it shared via http://runpython.com? Is a web site? Embedded in 
  a single board computer? 
* If there are graphics screens involved, describe every screen that the user will experience: what is it for? 
  What did the user have to do to get there and how does she move on to the next?
* For each graphics screen, describe every active control input and what it does. What elements on the screen will
  change in response to user input?
* Does the program respond to mouse input? What, exactly, does the mouse do?
* Does the program respond to keyboard input? How?
* What graphical assets will be used?
* Does the user have to do anything to install the program?

Your specification should **not** include the following types of information:

* The language you will use to create it.
* Names of any specific files in the project.
* How you will structure the classes, functions and code in your program.
* The name of any files or tools that you will use to design the program.
