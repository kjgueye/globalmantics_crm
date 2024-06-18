
class BuisnessCustomer:
    #this is a a typ of overserver, which is a buisness customer.
    #When they fall behing on payments, the program should automatically robocall thier finance Dept.

    def __init__(self, acct_id, money_owed):
        # Constructor to store the acct ID and current Amount of money owed
        self.acct_id = acct_id
        self.money_owed = money_owed

    def update(self):
        # When the acct system (the subject, or puplisher) needs to notify all observers (or subscribers)
        # about some event, this is the method that will be invoked.  Perhaps it is the end of month or
        # some other important event.
        if self.money_owed > 0:
            print(f"{self.acct_id}: Call the company's finance deptartment")
        else:
            print(f"{self.acct_id}: Corporate balance paid")

class ConsumerCustomer:
    # This is another type of observer,  a consumer customer.  WHen they fall behind on payments
    # they are jsut individuals who dont have departments working for them, so lets send a siumpler email reminder.

    def __init__(self, acct_id, money_owed):
        # Constructor to store the acct ID and current amount of money owed
        self.acct_id = acct_id
        self.money_owed = money_owed

    def update(self):
        # When the acct system (the subject, or puplisher) needs to notify all observers (or subscribers)
        # about some event, this is the method that will be invoked.  Perhaps it is the end of month or
        # some other important event.

        if self.money_owed > 0:
            print(f"{self.acct_id}: Send a polite reminder email")
        else:
            print(f"{self.acct_id}: Individual balance paid!")

class AccountingSystem:
    # This is the subject (or observer) that maintains a list of observers (or subscribers)
    # and is capable of notifyin them.  THere could be a mix
    # of different observers too, as we have both buisness and consumer-grade custoemrs.

    def __init__(self):
        # Constructor creates a new, empty accounting system with an emtpy set of consumers.

        self.customers = set()

    def register(self, customer):
        #A new customer has signed up, so add them to the set.

        self.customers.add(customer)

    def unregister(self, customer):

        self.customers.remove(customer)

    def notify(self):
        # Notify all current customers about some event.  This is iteratively steps through the set and
        # invokes the "updated()" method on each type of custoemr.
        for customer in self.customers:
            customer.update()

def main():
        # Execution starts here.


        # Create a mix of buisness and consumer customers with varying balances
        cust1 = BuisnessCustomer("ACCT100", 10)
        cust2 = BuisnessCustomer("ACCT200", 0)
        cust3 = ConsumerCustomer("ACCT300", -10)
        cust4 = ConsumerCustomer("ACCT400", 20)

        # Create the account system (subject) and register our new customers
        accounting_sys =AccountingSystem()
        accounting_sys.register(cust1)
        accounting_sys.register(cust2)
        accounting_sys.register(cust3)
        accounting_sys.register(cust4)

        # some event occured; notify all subscribers about thier bills
        accounting_sys.notify()


        #One customer has cnacelled thier account; unregister them
        print("** cust2 has cancelled their account")
        accounting_sys.unregister(cust2)

        #Event occured again, and notice how cust2 isn't displayed
        accounting_sys.notify()

if __name__ == "__main__":
    main()




