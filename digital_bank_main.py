import sys
import random
import time

from PyQt4 import QtGui
from PyQt4 import QtCore
from __ui import digitalbankUI
from digital_bank_database import *

class digital_bank(QtGui.QMainWindow, digitalbankUI.Ui_MainWindow, digital_bank_account_data):
    def __init__(self, parent=None):
        super(digital_bank, self).__init__()
        self.setupUi(self)
        self.set_ui()
        self.generate_account_num_pushButton.clicked.connect(self.generate_account_number)
        self.reset_pushButton.clicked.connect(self.reset)
        self.open_acc_checkBox.clicked.connect(self.validate_open_account)
        self.close_acc_checkBox.clicked.connect(self.validate_close_account)
        self.create_pushButton.clicked.connect(self.open_close_bank_account)
        self.loadAccount_pushButton.clicked.connect(self.load_bank_account_details)
        self.populate_account_type()



    def set_ui(self):
        self.create_pushButton.setText("Update")
        self.date_lineEdit.setEnabled(False)
        self.date_lineEdit.setText(time.strftime("%d-%m-%Y"))
        self.account_holder_name_lineEdit.setPlaceholderText('Enter Your Full Name')
        self.date_of_birth_lineEdit.setPlaceholderText('DD-MM-YYYY')
        self.mobile_num_lineEdit.setPlaceholderText('Enter Your Mobile Number')
        self.address_lineEdit.setPlaceholderText('Enter Your Address')
        self.aadhar_num_lineEdit.setPlaceholderText('Enter Your Aadhar Number')


    def validate_open_account(self):
        if self.open_acc_checkBox.isChecked():
            self.create_pushButton.setText('Update')
            self.close_acc_checkBox.setChecked(False)
            self.close_acc_checkBox.setEnabled(False)
        else:
            self.close_acc_checkBox.setChecked(False)
            self.close_acc_checkBox.setEnabled(True)

    def validate_close_account(self):
        if self.close_acc_checkBox.isChecked():
            self.create_pushButton.setText('Remove')
            self.open_acc_checkBox.setChecked(False)
            self.open_acc_checkBox.setEnabled(False)

        else:
            self.open_acc_checkBox.setChecked(False)
            self.open_acc_checkBox.setEnabled(True)

    def reset(self):
        ''' reset method is to resetting the all the lineEdits in the Digital_bank mian window


        :return:
        '''
        self.generate_account_num_lineEdit.clear()
        self.generate_account_num_lineEdit.setEnabled(True)
        self.account_type_comboBox.setCurrentIndex(0)
        self.account_holder_name_lineEdit.clear()
        self.date_of_birth_lineEdit.clear()
        self.mobile_num_lineEdit.clear()
        self.address_lineEdit.clear()
        self.aadhar_num_lineEdit.clear()
        self.male_radioButton.setChecked(False)
        self.female_radioButton.setChecked(False)
        self.other_radioButton.setChecked(False)


    def open_close_bank_account(self):
        '''
        open_close_bank_account method is used for crating and closing account details

        :return:
        '''
        get_account_num = str(self.generate_account_num_lineEdit.text())
        if get_account_num:
            digital_bank_account_data.__init__(self, get_account_num)
            if str(self.account_type_comboBox.currentText()) == '_select':
                print ('Please Select an Account')
                return False
            acc_hld_name = str(self.account_holder_name_lineEdit.text())
            acc_dob = str(self.date_of_birth_lineEdit.text())
            acc_mobile = str(self.mobile_num_lineEdit.text())
            acc_address = str(self.address_lineEdit.text())
            acc_aadhar = str(self.aadhar_num_lineEdit.text())
            if self.male_radioButton.isChecked():
                acc_gender = str(self.male_radioButton.text())
            elif self.female_radioButton.isChecked():
                acc_gender = str(self.female_radioButton.text())
            else:
                acc_gender = str(self.other_radioButton.text())
            if self.open_acc_checkBox.isChecked():
                self.upadte_bank_account_data(account_type=str(self.account_type_comboBox.currentText()),
                                                 account_holder_name=acc_hld_name,
                                                 date_of_birth=acc_dob,
                                                 mobile_number=acc_mobile,
                                                 address=acc_address,
                                                 aadhar_number=acc_aadhar,
                                                 gender=acc_gender,
                                                 created_on=str(self.date_lineEdit.text()))
            else:
                self.upadte_bank_account_data(account_type=str(self.account_type_comboBox.currentText()),
                                              account_holder_name=acc_hld_name,
                                              date_of_birth=acc_dob,
                                              mobile_number=acc_mobile,
                                              address=acc_address,
                                              aadhar_number=acc_aadhar,
                                              gender=acc_gender,
                                              created_on=str(self.date_lineEdit.text()), open_account=False)
        else:
            print("Account Number is Required")
            return False
        self.reset()


    def populate_account_type(self):
        '''
        populate_account_type is used to first clear the combobox and next select the default _select

        :return:
        '''
        self.account_type_comboBox.clear()
        list_of_account_type = ['_select', 'savings', 'current', 'salary']
        list_of_account_type.sort()
        self.account_type_comboBox.addItems(list_of_account_type)
        self.account_type_comboBox.setCurrentIndex(0)

    def generate_account_number(self):
        self.generate_account_num_lineEdit.clear()
        bank_name_tag = 'DGBN'
        random_number = random.randrange(100000)
        bank_account_number = bank_name_tag + str(random_number).zfill(9)
        self.generate_account_num_lineEdit.setText(bank_account_number)
        self.generate_account_num_lineEdit.setEnabled(False)


    def load_bank_account_details(self):
        load_acc_num = str(self.generate_account_num_lineEdit.text())
        if not load_acc_num:
            print("Account Number is Required")
            return False
        digital_bank_account_data.__init__(self, load_acc_num)
        if load_acc_num in self.account_details:
            acc_type = str(self.account_details[load_acc_num]['account_type'])
            self.account_type_comboBox.setCurrentIndex(self.account_type_comboBox.findText(acc_type, QtCore.Qt.MatchFixedString))
            self.account_holder_name_lineEdit.setText(str(self.account_details[load_acc_num]['account_holder_name']))
            self.date_of_birth_lineEdit.setText(str(self.account_details[load_acc_num]['date_of_birth']))
            self.mobile_num_lineEdit.setText(str(self.account_details[load_acc_num]['mobile_number']))
            self.address_lineEdit.setText(str(self.account_details[load_acc_num]['address']))
            self.aadhar_num_lineEdit.setText(str(self.account_details[load_acc_num]['aadhar_number']))
            get_gender = str(self.account_details[load_acc_num]['gender'])
            if get_gender == 'male':
                self.male_radioButton.setChecked(True)
            elif get_gender == 'female':
                self.female_radioButton.setChecked(True)
            else:
                self.other_radioButton.setChecked(True)



def main():
    app = QtGui.QApplication(sys.argv)
    buildapp = digital_bank()
    buildapp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()