import MySQLdb

class digital_sql:
    def __init__(self, digital_host='localhost', digital_user='root', digital_passwd='', digital_db='dg_bank'):
        self.digital_db_connect = MySQLdb.Connect(host=digital_host, user=digital_user, passwd=digital_passwd, db=digital_db)
        self.digital_cur = self.digital_db_connect.cursor()

    def digital_query_command(self, query_command='SELECT * FROM account_details'):
        self.digital_cur.execute("{}".format(query_command))
        return self.digital_cur.fetchall()

    def digital_insert_command(self, insert_command="""INSERT INTO account_details VALUES ('DGBN00000921','salary', 'kiran surendra jaddu', '30071994', '9603048784', 'SRNAGAR', '74185963963', 'male')"""):
        self.digital_cur.execute("{}".format(insert_command))
        self.digital_db_connect.commit()

    def digital_delete_command(self, delete_command="""DELETE FROM employee WHERE emp_phone=''"""):
        self.digital_cur.execute('{}'.format(delete_command))
        self.digital_db_connect.commit()




if __name__ == "__main__":
    inst_db = digital_sql()
    # inst_db.digital_delete_command()
    inst_db.digital_insert_command()
    # print(inst_db.digital_query_command())
    #     print(item)