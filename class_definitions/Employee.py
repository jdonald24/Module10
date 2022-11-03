""" 
Program: employee.py
Author: Austin Donald
Last date modified: 11/01/2022

This class stores and outputs information about employees.
"""
import datetime as dt
class Employee:
    """Employee Class"""
    _last_name = ""
    _first_name = ""
    _address = ""
    _phone_number = ""
    _salaried = False
    _start_date = dt.datetime.now()
    _salary = 0.0
    # Constructor
    def __init__(self, lname, fname):
         self._last_name = lname
         self._first_name = fname

    def set_last_name(self, lname):
         self._last_name = lname

    def set_first_name(self, fname):
         self._first_name = fname

    def set_address(self, ad):
        self._address = ad
    
    def set_phone_number(self, pn):
        self._phone_number = pn

    def set_salaried(self, s):
        self._salareied = s

    def set_start_date(self, sd):
        self._start_date = sd

    def set_salary(self, sa):
        self._salary = sa

    def display(self):
        if(self._salaried):
            return str(self._first_name)+" "+str(self._last_name)+"\n"+str(self._address)+"\nSalaried employee: $"+str(self._salary)+"/year\nStart date: "+str(self._start_date)
        else:
            return str(self._first_name)+" "+str(self._last_name)+"\n"+str(self._address)+"\nHourly employee: $"+str(self._salary)+"/hour\nStart date: "+str(self._start_date)
    def __str__(self):
        return "Employee with the name "+str(self._first_name)+" "+str(self._last_name)
    def __repr__(self):
        return "Employee name: "+str(self._first_name)+" "+str(self._last_name)+" address: "+str(self._address)+" phone number: "+str(self._phone_number)+" salaried: "+str(self._salaried)+" start date: "+str(self._start_date)+" salary: "+str(self._salary)
# Driver
emp = Employee('Ruiz', 'Matthew')   # call the construtor, needs to have a first and last name in parameter
emp.set_first_name('Matt')
print(emp.display())                # display returns a str, so print the information
del emp                             # clean up! 