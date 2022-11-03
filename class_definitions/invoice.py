"""
Program: invoice.py
Author: Austin Donald
Last date modified: 11/02/2022

This class creates an invoice for a customer
"""
class Invoice:
    _invoice_id = 0
    _customer_id = 0
    _last_name = ""
    _first_name = ""
    _phone_number = ""
    _address = ""
    _items_with_price = dict({})
    def __init__(self, invoice, customer, last, first, phone, ad):
        self._invoice_id = invoice
        self._customer_id = customer
        self._last_name = last
        self._first_name = first
        self._phone_number = phone
        self.address = ad
    def add_item(self, key, value):
        self._items_with_price.update({key: value})
    def create_invoice (self):
        dict_length = len(list(self._items_with_price))
        keys = list(self._items_with_price)
        values = list(self._items_with_price.values())
        total = 0.0
        tax = 0.0
        for x in range(dict_length):
            print(str(keys[x]) + " $"+ str(values[x]))
            total = total+float(values[x])
        tax = total*0.06
        print("Tax: $"+str(tax))
        total = total+tax
        print("Total: $"+str(total))
    def __str__(self):
        return "An invoice for the costumer "+str(self._first_name)+" "+str(self._last_name)
    def __repr__(self):
        return str(self._invoice_id)+" "+str(self._customer_id)+" "+str(self._last_name)+" "+str(self._first_name)+" "+str(self._phone_number)+" "+str(self._address)+" "+str(self._items_with_price)
inv = Invoice(888, 28371, "Smith", "John", "(515)7632-191", "455 Oak dr.")
inv.add_item("Washing Machine", 1500)
inv.add_item("t-shirt", 20)
inv.create_invoice()
del inv