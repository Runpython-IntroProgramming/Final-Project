Currency Converter

## Design Specification

The design specificaiton is a counterpart to the Functional Speciffication. Where a functional specification concerns itself
with inputs and outputs from the program, or the *experience* of a user running the program, the design specification is concerned with decisions that the engineer and programmer must make during its creation.

To create this program I will use runpython, and Python 3. The program begins by asking the user to input a name of a currency. This is the currency they would like to convert from. Then the program says if the currency entered is "US Dollar", for example, it goes and finds the dictionary containing the exchange rates for the US Dollar. There are dictionaries for each currency that can be entered as the respone to the first question. Then once the program has found the currency entered by the user, it asks the user to enter an amount of that currency to convert. After this, the programs asks the user to enter the name of the currency they would like to convert to. Then the program goes through and finds the exchange rate for that currency in the dictionary of the first currency entered. It multiplies the exchange rate by the amount entered and returns a new, converted value in the second currency. 
After the programs asks the user to enter a currency, there a serious of if statements. Each if statement has the same syntax, and there is an if statement for each currency that can be entered in response to the first question. The if statement says if the currency is this (any of the currencies in the world) then the user should enter an amount of that currency to convert. Then within each if statement, there is a dictionary, containing the exchange rates with all the different currencies across the world for the currency entered. After the dictionary, the program asks the user what currency they would like to convert to. After this the user stores the value for the exchange rate (value for a key in a dictionary) in "k". The program takes k and multiplies it by the amount entered for conversion. It stores this value in "m", and then prints "m" rounded to two decimal places, followed by the name of the currency the original amount has been converted to. Each if loop contains the same syntax and function, with a different dictionary containing the exchange rates. There are over 30 dictionaries and if loops, representing over half the currencies in the world. The programs stores tons of data, the exchange rates for each currency to any other currency, in dictionaries, and there are over 30 of them. Each if statement simply sorts through the selected dictionary and returns the correct exchange rate by accessing the value to a key (which is the name of the currency to be converted to). 

The design specification should include information like:

* What tools or frameworks will you use to build the project (e.g. http://runpython.com or ggame)?
* What language will you use for coding (usually Python 3)?
* For every element of the Functional Specification, what code will need to be written to support it?
* What data will be stored or manipulated by the program? How will it be encoded and organized?
* Describe the logic and/or code behind every interaction with the user, and behind everything displayed.
* If your program uses an unusual or notable *algorithm*, what is the algorithm and how does it work?
