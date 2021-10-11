import queries.q_admins as q_admins
import os.path
import csv
import datetime
from . import m_output as q_output

from colorama import Fore, Style
from prettytable import *


class Admins():
    def process(self, driver, line):
        args = line.split()
        if not driver.status():
            return
        if len(args) < 1:
            print(Fore.RED, 'Missing action : \
                  domain|enterprise|schema|passwordneverexpires', Fore.WHITE)
        else:
            action = args[0]
            result_writer = None
            if action == 'domain':
                resultSet, session = \
                  driver.query(q_admins.Admins().get_domain_admins("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_domain_all.csv')
                session.close()
            elif action == "domain=enabled":
                resultSet, session = \
                  driver.query(q_admins.Admins().get_domain_admins("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_domain_enabled.csv')
                session.close()
            elif action == "schema":
                resultSet, session = \
                  driver.query(q_admins.Admins().get_schema_admins("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_schema_all.csv')
                session.close()
            elif action == "schema=enabled":
                resultSet, session = \
                  driver.query(q_admins.Admins().get_schema_admins("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_schema_enabled.csv')
                session.close()
            elif action == "enterprise":
                resultSet, session = \
                  driver.query(q_admins.Admins().get_enterprise_admins("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_enterprise_all.csv')
                session.close()
            elif action == "enterprise=enabled":
                resultSet, session = \
                  driver.query(q_admins.Admins().get_enterprise_admins("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_enterprise_enabled.csv')
                session.close()
            elif action == "accountOperators":
                resultSet, session = driver.query(q_admins.Admins().get_account_operators("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_accountOperators_all.csv')
                session.close()
            elif action == "accountOperators=enabled":
                resultSet, session = driver.query(q_admins.Admins().get_account_operators("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_accountOperators_enabled.csv')
                session.close()
            elif action == "administrators":
                resultSet, session = driver.query(q_admins.Admins().get_administrators("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_administrators_all.csv')
                session.close()
            elif action == "administrators=enabled":
                resultSet, session = driver.query(q_admins.Admins().get_administrators("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_administrators_enabled.csv')
                session.close()
            elif action == "backupOperators":
                resultSet, session = driver.query(q_admins.Admins().get_backup_operators("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_backupOperators_all.csv')
                session.close()
            elif action == "backupOperators=enabled":
                resultSet, session = driver.query(q_admins.Admins().get_backup_operators("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_backupOperators_enabled.csv')
                session.close()
            elif action == "printOperators":
                resultSet, session = driver.query(q_admins.Admins().get_print_operators("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_printOperators_all.csv')
                session.close()
            elif action == "printOperators=enabled":
                resultSet, session = driver.query(q_admins.Admins().get_print_operators("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_printOperators_enabled.csv')
                session.close()
            elif action == "replicators":
                resultSet, session = driver.query(q_admins.Admins().get_replicators("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_replicators_all.csv')
                session.close()
            elif action == "replicators=enabled":
                resultSet, session = driver.query(q_admins.Admins().get_replicators("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_replicators_enabled.csv')
                session.close()
            elif action == "serverOperators":
                resultSet, session = driver.query(q_admins.Admins().get_server_operators("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_serverOperators_all.csv')
                session.close()
            elif action == "serverOperators=enabled":
                resultSet, session = driver.query(q_admins.Admins().get_server_operators("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_serverOperators_enabled.csv')
                session.close()
            elif action == "adminSDHolder":
                resultSet, session = driver.query(q_admins.Admins().get_adminsdholder("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_adminSDHolder_all.csv')
                session.close()
            elif action == "adminSDHolder=enabled":
                resultSet, session = driver.query(q_admins.Admins().get_adminsdholder("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_adminSDHolder_enabled.csv')
                session.close()
            elif action == "passwordneverexpires":
                resultSet, session = driver.query(q_admins.Admins().get_password_never_expires("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_pwdnvrexp_all.csv')
                session.close()
            elif action == "passwordneverexpires=enabled":
                resultSet, session = driver.query(q_admins.Admins().get_password_never_expires("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Admin_pwdnvrexp_enabled.csv')
                session.close()
            else:
                print(Fore.RED, 'Unrecognized action. Expected: domain|enterprise|schema|passwordneverexpires', Fore.WHITE)
