#!/usr/bin/env python3
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class CreditCard:
  """A consumer credit card."""

  def __init__(self, customer, bank, acnt, limit, balance=0):
    """Create a new credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = balance

  def get_customer(self):
    """Return name of the customer."""
    return self._customer

  def get_bank(self):
    """Return the bank's name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Return current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed; False if charge was denied.
    """
    try:
      if price + self._balance > self._limit:  # if charge would exceed limit,
        return False                           # cannot accept charge
      else:
        self._balance += price
        return True
    except TypeError:
        return False

  def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    try:
      self._balance -= amount
      if amount < 0:
        raise ValueError("check again ! ValueError ! amount must >= 0")
    except TypeError:
      print("check again ! TypeError")
    except ValueError as ve:
      print(ve)

if __name__ == '__main__':
  a = CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500)
  print(a.charge(10))
  print(a.charge('df'))
  a.make_payment(5)
  a.make_payment(-5)
  a.make_payment("dfs")
