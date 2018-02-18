import digital_database
import json
import os
file_path = os.path.dirname(__file__)

class digital_bank_account_data:
    def __init__(self, account_number):
        self.json_file_path = os.path.join(file_path, "bank_data/bank_account_details.json")
        if not account_number:
            print("Account Number is Required")
            return False
        self.account_number = account_number
        self.load_bank_account_data()

    @property
    def get_account_holder_name(self):
        return self.__account_details[self.account_number]['account_holder_name']

    @property
    def get_account_type(self):
        return self.__account_details[self.account_number]['account_type']

    @property
    def get_date_of_birth(self):
        return self.__account_details[self.account_number]['date_of_birth']

    @property
    def get_mobile_number(self):
        return self.__account_details[self.account_number]['mobile_number']

    @property
    def get_address(self):
        return self.__account_details[self.account_number]['address']

    @property
    def get_aadhar_number(self):
        return self.__account_details[self.account_number]['aadhar_number']

    @property
    def get_gender(self):
        return self.__account_details[self.account_number]['gender']


    def upadte_bank_account_data(self, account_type, account_holder_name, date_of_birth, mobile_number, address, aadhar_number, gender, created_on, open_account=True):
        if open_account:
            self.__account_details[self.account_number] = {
                'account_type':account_type,
                'account_holder_name':account_holder_name,
                'date_of_birth':date_of_birth,
                'mobile_number':mobile_number,
                'address':address,
                'aadhar_number':aadhar_number,
                'gender':gender,
                'created_on':created_on}
            print("Account Created Successfully")
        else:
            self.__account_details.pop(self.account_number)
            print("Account Removed Successfully")
        try:
            fp = open(self.json_file_path, 'w')
            json.dump(self.__account_details, fp, indent=3)
            fp.close()
        except:
            print("No permission to Write Data")

    def load_bank_account_data(self):
        if os.path.exists(self.json_file_path):
            try:
                fp = open(self.json_file_path, 'r')
                self.__account_details = json.load(fp)
                fp.close()
            except:
                print("Unable to load Data")
                self.__account_details = {}
        else:
            self.__account_details = {}


if __name__ == "__main__":
    inst_acc = digital_bank_account_data('DGBN00000921')
    print(dir(inst_acc))
    db_inst = digital_database.digital_sql()
    db_inst.digital_insert_command(insert_command="""INSERT INTO account_details VALUES ('DGBN00000921','salary', 'kiran surendra jaddu', '30-07-1995', '9603048784', 'SRNAGAR', '74185963963', 'male')""")
    # print(db_inst.digital_query_command())
    # inst_acc.upadte_bank_account_data('saving', 'surrender', '30-07-1994', 9603048784, 'SRNAGAR', 124124412, 'male')
    print(inst_acc.get_gender)
