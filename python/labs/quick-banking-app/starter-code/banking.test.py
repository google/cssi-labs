#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from banking import BankAccount

acc = BankAccount("test acc", 1000)
print("Created bank account 'test acc' with initial balance 1000")

print("\nTest 0: __init__")
print("label: %s" % acc.label)
assert acc.label == "test acc", "Expected 'test acc', instead saw %s" % acc.label
print("balance: %s" % acc.balance)
assert acc.balance == 1000, "Expected 1000, instead saw %s" % acc.balance
print("Test 0 passed!")

print("\nTest 1: __str__")
print(acc)
assert "1000" in str(acc) and "test acc" in str(acc), \
    "Missing info from __str__, should contain '1000' and 'test acc'"
print("Test 1 passed!")

print("\nTest 2: withdraw")
print("Withdrawing 100")
acc.withdraw(100)
print(acc)
assert acc.balance == 900, "Expected balance 900, instead saw %s" % acc.balance
print("Test 2 passed!")

print("\nTest 2.1: withdraw negative")
print("Withdrawing -200")
acc.withdraw(-200)
print(acc)
assert acc.balance == 900, "Expected balance 900, instead saw %s" % acc.balance
print("Test 2.1 passed!")

print("\nTest 2.2: withdraw overlimit")
print("Withdrawing 10000")
acc.withdraw(10000)
print(acc)
assert acc.balance == 900, "Expected balance 900, instead saw %s" % acc.balance
print("Test 2.2 passed!")

print("\nTest 3: deposit")
print("Depositing 500")
acc.deposit(500)
print(acc)
assert acc.balance == 1400, "Expected balance 1400, instead saw %s" % acc.balance
print("Test 3 passed!")

print("\nTest 3.1: deposit negative")
print("Depositing -200")
acc.deposit(-200)
print(acc)
assert acc.balance == 1400, "Expected balance 1400, instead saw %s" % acc.balance
print("Test 3.1 passed!")

print("\nTest 4: rename")
print("Renaming to 'real acc'")
acc.rename("real acc")
print(acc)
assert acc.label == "real acc", \
    "Expected label to be 'real acc', instead saw %s" % acc.label
print("Test 4 passed!")

print("\nTest 4.1: rename blank")
print("Renaming to ''")
acc.rename("")
print(acc)
assert acc.label == "real acc", \
    "Expected label to be 'real acc', instead saw %s" % acc.label
print("Test 4.1 passed!")

cont = input("\nDid you do level 2? [y|n]: ").lower()
if cont == "n":
    sys.exit()

acc2 = BankAccount("new acc", 200)
print("\nCreated bank account 'new acc' with initial balance 200")

print("\nTest 5: transfer")
print("Transferring 300 from 'real acc' to 'new acc'")
acc.transfer(acc2, 300)
print(acc)
print(acc2)
assert acc.balance == 1100, \
    "Expected 'real acc' balance 1100, instead saw %s" % acc.balance
assert acc2.balance == 500, \
    "Expected 'new acc' balance 500, instead saw %s" % acc.balance
print("Test 5 passed!")

print("\nTest 5.1: transfer negative")
print("Transferring -100 from 'real acc' to 'new acc'")
acc.transfer(acc2, -100)
print(acc)
print(acc2)
assert acc.balance == 1100, \
    "Expected 'real acc' balance 1100, instead saw %s" % acc.balance
assert acc2.balance == 500, \
    "Expected 'new acc' balance 500, instead saw %s" % acc.balance
print("Test 5.1 passed!")

print("\nTest 5.2: transfer")
print("Transferring 5000 from 'real acc' to 'new acc'")
acc.transfer(acc2, 5000)
print(acc)
print(acc2)
assert acc.balance == 1100, \
    "Expected 'real acc' balance 1100, instead saw %s" % acc.balance
assert acc2.balance == 500, \
    "Expected 'new acc' balance 500, instead saw %s" % acc.balance
print("Test 5.2 passed!")