class Help:
    def db(self):
        print('Description :\n\tInteract with Neo4j database')
        print('Usage :\n\tdb <option>')
        print('Options :')
        print('\tconnect : connect to configured database')
        print('\tdisconnect : disconnected from database')
        print('\tstatus : print connection status')

    def config(self):
        print('Description :\n\tManage database configuration')
        print('Usage :\n\tconfig <option>')
        print('Options :')
        print('\tcreate : create configuration file')
        print('\tupdate <all|uri|user|password>')
        print('\t\tall : update all configuration file')
        print('\t\turi : update database URI')
        print('\t\tuser : update database user')
        print('\t\tpassword : update database password')
        print('\tdelete : reset configuration file to defaults')
        print('\tverify : verify configuration')

    def admin(self):
        print('Description :\n\tQuery data on administrators')
        print('Usage :\n\tadmin <option> [export]')
        print('Options :')
        print('\tdomain[=enabled] : list all domain admins group members or only enabled')
        print('\tenterprise[=enabled] : list all enterprise admins group members or only enabled')
        print('\tschema[=enabled] : list all schema admins group members or only enabled')
        print('\taccountOperators[=enabled] : list all account operators group members or only enabled')
        print('\tadministrators[=enabled] : list all administrators group members or only enabled')
        print('\tbackupOperators[=enabled] : list all backup operators group members or only enabled')
        print('\tprintOperators[=enabled] : list all print operators group members or only enabled')
        print('\treplicators[=enabled] : list all replicators group members or only enabled')
        print('\tserverOperators[=enabled] : list all server operators group members or only enabled')
        print('\tadminSDHolder[=enabled] : list all above')
        print('\tpasswordneverexpires[=enabled] : list all admins whose password never expires or only enabled')

    def computer(self):
        print('Description :\n\tQuery data on computers')
        print('Usage :\n\tcomputer <option> [export]')
        print('Options :')
        print('\tlaps : get computers on which LAPS is installed')
        print('\tobsolete : retrieve all obsolete OS (can provide false positive with reality)')

    def password(self):
        print('Description :\n\tQuery data on passwords')
        print('Usage :\n\tpassword <option> [export]')
        print('Options :')
        print('\tcomment[=enabled] : print users comments containing possible passwords')
        print('\tchangeddate[=enabled] [days] : show users whose passwords are older than given days (90 by default)')
        print('\tuserpassword[=enabled] : detect if any password is stored in userpassword attribute')

    def user(self):
        print('Description :\n\tQuery data on users')
        print('Usage :\n\tuser <option> [export]')
        print('Options :')
        print('\tlocaladmin[=enabled] : list all unprivileged users (or only enabled) and computers they are admin on')
        print('\tlocaladminDC[=enabled] : list all unprivileged users (or only enabled) admins on DC')
        print('\tpasswordneverexpires[=enabled] : list all unprivileged users whose password never expires (or only enabled)')
        print('\treadlaps[=enabled] : list all unprivileged users who can read laps passwords (or only enabled)')

    def importFile(self):
        print('Description :\n\tImport NTLM hashes or cracked passwords into neo4j')
        print('Usage :\n\timport <option> <file>')
        print('Options :')
        print('\tntlm : create LM flag and import NTLM hash in neo4j')
        print('\tcracked : import cracked password into neo4j and set user as owned')
        print('File format :')
        print('\tntlm : secretsdump or JTR "show" format')
        print('\tcracked : JTR "show" format')

    def stats(self):
        print('Description :\n\tProvides statistics on passwords. This only works after importing NTLM and cracked passwords (see help import)')
        print('Usage :\n\tstats <option> <attributes>')
        print('Options :')
        print('\tpassword[=enabled] : output passwords statistics')
        print('Attributes :')
        print('\tuser : only unprivileged users')
        print('\tadmin : only privileged users')
        print('\tall : all users')

    def search(self):
        print('Description :\n\tRetrieve data on users, computers or passwords (only works after importing NTLM and cracked passwords (see help import))')
        print('Usage :\n\tsearch <option> <filter> [term] [export]')
        print('Options :')
        print('\tpassword[=enabled] : search for passwords')
        print('\tuser[=enabled] : search for users')
        print('\tcomputer[=enabled] : search for computers')
        print('Filters :')
        print('\tis : search for specific term (case sensitive)')
        print('\tlike : search by partial term (case insensitive)')
        print('\tempty : search for empty passwords')
        print('\tlm : retrieve nodes with LM storage')
        print('Term : quotes and space are taken as part of term, do not provide it as delimiter')

