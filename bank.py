class bank:
    def __int__(self, name):
        self.name = name
        self.clients = []
        self.money = 0.0

class cleint:
    def __int__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.client_accounts = []
        self.client_total_money = 0.0

class cuenta_corriente:
    def __int__(self,account_id,client_id):
        self.acoount_id = account_id
        self.client_id = client_id
        self.acoount_money = 0.0
        