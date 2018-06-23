
# Quick Banking App

## Background

Financial apps are all the craze now.  Robinhood, Acorn, you name it.  Let's get in on this hype by creating our own, simple, banking app.

## Task

In the provided `banking.py` file, create a `BankAccount` class that represents a bank account.

The first thing you should do is create the constructor, the `__init__` method.  Have the `__init__` method accept two arguments (after `self`):
* `label`, which represents the name of the bank account
* `balance`, which represents the amount of money in the bank account

Have the constructor initialize  `self.label` and `self.balance` to the given `label` and `balance` values.

Then, run `banking.test.py` to see if you pass test 0.  If you did, then everything is good and you can continue!

Next, create the following methods/behaviors:
* `__str__` - print out all the information for the BankAccount - the label and balance.
* `withdraw` - remove money from the balance of the BankAccount.  Prevent people from withdrawing more than they have, or withdrawing a negative amount
* `deposit` - add money to the balance of the BankAccount.  Prevent people from depositing a negative amount
* `rename` - change the label of the BankAccount.  Prevent people from naming it blank.

After completing each method (in order), you can test your object by running `banking.test.py`.

## Extensions

## Level 2
Add a method to the `BankAccount` class called `transfer` that transfers some amount of money from one `BankAccount` to another.  Similar to withdrawing, prevent people from transferring more than they have, or transferring a negative amount.  The method should take two arguments in this order: `dest_account`, which represents the destination `BankAccount` object, and `amount`, which represents the amount to transfer.

You can test your object by running `banking.test.py`.

## Level 3
In addition to having a `BankAccount` class, have a `Transaction` class that contains the following states/fields:
* `time` - the time of the transaction (use unix time given by `time.time()` after `import time`)
* `type` - the type of transaction - withdrawal, deposit, or transfer
* `amount` - the amount involved in the transaction
* `dest_account` - (for transfers only) - the label of the account money was transferred into
* `__str__` - print out the transaction information, in a way such as: `<timestamp>: withdraw $1000` or `<timestamp>: transfer $1532 to account 'Savings'`.

Then add a new field to the `BankAccount` class called `transactions` which contains a list of `Transaction` objects.  These objects should be created and added to `transactions` every time the user interacts with the account (by withdrawing, depositing, or transferring).

Then add a new option to the main program loop to allow the user to see all the transactions for a specific bank account.

`banking.test.py` does not include tests for this level, so you will have to write your own, or perform testing yourself.
