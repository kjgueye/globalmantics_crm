
class Database:

    def __init__(self, path):

        with open(path, "r") as handle:
            """
            import json
            self.data = json.load(handle)
            
            import yaml
            self.data = yaml.safe_load(handle)
            """

            import xmltodict
            self.data = xmltodict.parse(handle.read()) ["root"]
            print(self.data)

    def balance(self, acct_id):
        acct = self.data.get(acct_id)
        if acct:
            bal = float(acct["due"]) - float(acct["paid"])
            return f"{bal:.2f} USD"
            # return f"${bal:.2f}"
        return None
    def owes_money(self, acct_id):
        """
        Returns true if the account holder owes us money. Returns
        false if they are up to date on payments or have credit
        from a past overpayment.
        """
        acct = self.data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"]) > 0

        return None