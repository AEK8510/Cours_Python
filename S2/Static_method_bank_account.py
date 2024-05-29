class BankAccount:
	total_accounts = 0

	def __init__(self, account_number, balance):
		self.account_number = account_number
		self.balance = balance
		BankAccount.total_accounts += 1  # Increment total accounts count


    # Magic method
    def __str__(self):
        return self.account_number
	@classmethod
	def get_total_accounts(cls):
		return cls.total_accounts




class basiclemon:
	def __init__(self, color="yellow", size="standard"):
		self.color = "yellow"
		self.standard = "standard"

	def __str__(self):
		return "Your lemon is of color", self.color
		"and of size", self.size