class Account_Payable:
    def __init__(self, id, description, 
                amount, due_date, priority, 
                to_company_id, from_company_id):

        self.__id=id
        self.description=description
        self.amount=amount
        self.due_date=due_date
        self.priority=priority
        self.to_company_id=to_company_id
        self.from_company_id=from_company_id

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id