from prettytable import PrettyTable
from colorama import Fore,Style

class Import:
    def importNTLM(self,importFile,driver):
        table = PrettyTable()
        try:
            file=open(importFile,"r")
        except Exception:
            print(Fore.RED,"Error : file note found.",Fore.WHITE)
            return
        domain = []
        resultSet,session = driver.query('MATCH (d:Domain) RETURN d.name as domain')
        for record in resultSet:
            domain.append(record["domain"])
        session.close()
        for line in file:
            imported = None
            username = None
            data = line.split(":")
            if len(data) > 1:
                user = data[0]
                if len(data) < 8:
                    lm_hash = data[2]
                    ntlm_hash = data[2]+":"+data[3]
                else:
                    lm_hash = data[3]
                    ntlm_hash = data[3]+":"+data[4]
                if not len(lm_hash) == 32:
                    print(Fore.RED,"Error : invalid format. NTLM hash is not recognized.",Fore.WHITE)
                    break
                if "\\" in user:
                    userdata = user.split("\\")
                    if "$" not in user:
                        loop = 0
                        while loop < len(domain): 
                            username = userdata[1]+"@"+domain[loop]
                            if "aad3b435b51404eeaad3b435b51404ee" not in lm_hash:
                                resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.lm = True, u.ntlm = "'+ntlm_hash+'" RETURN u.name as name')
                            else:
                                resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.lm = False, u.ntlm = "'+ntlm_hash+'" RETURN u.name as name')
                            for record in resultSet:
                                imported = True
                            loop = loop + 1 if not imported else len(domain)
                            session.close()
                        if not imported:
                            print(Fore.RED,"Error : "+userdata[1].upper()+" not found in BloodHound with all detected domains.",Fore.WHITE)
                    else:
                        loop = 0
                        while loop < len(domain):
                            username = userdata[1]+"@"+domain[loop]
                            if "aad3b435b51404eeaad3b435b51404ee" not in lm_hash:
                                resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.lm = True, u.ntlm = "'+ntlm_hash+'" RETURN u.name as name')
                            else:
                                resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.lm = False, u.ntlm = "'+ntlm_hash+'" RETURN u.name as name')
                            for record in resultSet:
                                imported = True
                            loop = loop + 1 if not imported else len(domain)
                            session.close()
                        if not imported:
                            loop = 0
                            while loop < len(domain):
                                if userdata[1].endswith('$'):
                                    computer = userdata[1][:-1]+"."+domain[loop]
                                else:
                                    computer = userdata[1]+"."+domain[loop]
                                if "aad3b435b51404eeaad3b435b51404ee" not in lm_hash:
                                    resultSet,session = driver.query('MATCH (c:Computer) where c.name = "'+computer.upper()+'" SET c.lm = True, c.ntlm = "'+ntlm_hash+'" RETURN c.name as name')
                                else:
                                    resultSet,session = driver.query('MATCH (c:Computer) where c.name = "'+computer.upper()+'" SET c.lm = False, c.ntlm = "'+ntlm_hash+'" RETURN c.name as name')
                                for record in resultSet:
                                    imported = True
                                loop = loop + 1 if not imported else len(domain)
                                session.close()
                            if not imported:
                                print(Fore.RED,"Error : "+userdata[1].upper()+" not found in BloodHound users or computers with all detected domains.",Fore.WHITE)
                else:
                    if "$" not in user:
                        loop = 0
                        while loop < len(domain):
                            username = user+"@"+domain[loop]
                            if "aad3b435b51404eeaad3b435b51404ee" not in lm_hash:
                                resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.lm = True, u.ntlm = "'+ntlm_hash+'" RETURN u.name as name')
                            else:
                                resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.lm = False, u.ntlm = "'+ntlm_hash+'" RETURN u.name as name')
                            for record in resultSet:
                                imported = True
                            loop = loop + 1 if not imported else len(domain)
                            session.close()
                        if not imported:
                            print(Fore.RED,"Error : "+user.upper()+" not found in BloodHound users with all detected domains.",Fore.WHITE)
                    else:
                        loop = 0
                        while loop < len(domain):
                            username = user+"@"+domain[loop]
                            if "aad3b435b51404eeaad3b435b51404ee" not in lm_hash:
                                resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.lm = True, u.ntlm = "'+ntlm_hash+'" RETURN u.name as name')
                            else:
                                resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.lm = False, u.ntlm = "'+ntlm_hash+'" RETURN u.name as name')
                            for record in resultSet:
                                imported = True
                            loop = loop + 1 if not imported else len(domain)
                            session.close()
                        if not imported:
                            loop = 0
                            while loop < len(domain):
                                if user.endswith('$'):
                                    computer = user[:-1]+"."+domain[loop]
                                else:
                                    computer = user+"."+domain[loop]
                                if "aad3b435b51404eeaad3b435b51404ee" not in lm_hash:
                                    resultSet,session = driver.query('MATCH (c:Computer) where c.name = "'+computer.upper()+'" SET c.lm = True, c.ntlm = "'+ntlm_hash+'" RETURN c.name as name')
                                else:
                                    resultSet,session = driver.query('MATCH (c:Computer) where c.name = "'+computer.upper()+'" SET c.lm = False, c.ntlm = "'+ntlm_hash+'" RETURN c.name as name')
                                for record in resultSet:
                                    imported = True
                                loop = loop + 1 if not imported else len(domain)
                                session.close()
                            if not imported:
                                print(Fore.RED,"Error : "+user.upper()+" not found in BloodHound users or computers with all detected domains.",Fore.WHITE)
        file.close()

    def importPassword(self,importFile,driver):
        table = PrettyTable()
        try:
            file=open(importFile,"r")
        except Exception:
            print("cannot found file")
            return
        domain = []
        resultSet,session = driver.query('MATCH (d:Domain) RETURN d.name as domain')
        for record in resultSet:
            domain.append(record["domain"])
        session.close()
        for line in file:
            imported = None
            username = None
            data = line.split(":")
            if len(data) > 1:
                if len(data) < 8:
                    print(Fore.RED,"Error : invalid file format. Provide 'john --show' file format",Fore.WHITE)
                    break
                elif len(data) > 8:
                    pwd = ":".join(data[1:-6]).translate(str.maketrans({'\\': r'\\', '"': r'\"'}))
                else:
                    pwd = data[1].translate(str.maketrans({'\\': r'\\', '"': r'\"'}))
                user = data[0]
                if "\\" in user:
                    userdata = user.split("\\")
                    if "$" not in user:
                        loop = 0
                        while loop < len(domain):
                            username = userdata[1]+"@"+domain[loop]
                            resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.cracked_password = "'+pwd+'", u.owned = True RETURN u.name as name')
                            for record in resultSet:
                                imported = True
                            loop = loop + 1 if not imported else len(domain)
                            session.close()
                        if not imported:
                            print(Fore.RED,"Error : "+userdata[1].upper()+" not found in BloodHound users or computers with all detected domains.",Fore.WHITE)
                    else:
                        loop = 0
                        while loop < len(domain):
                            username = userdata[1]+"@"+domain[loop]
                            resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.cracked_password = "'+pwd+'", u.owned = True RETURN u.name as name')
                            for record in resultSet:
                                imported = True
                            loop = loop + 1 if not imported else len(domain)
                            session.close()
                        if not imported:
                            loop = 0
                            while loop < len(domain):
                                if userdata[1].endswith('$'):
                                    computer = userdata[1][:-1]+"."+domain[loop]
                                else:
                                    computer = userdata[1]+"."+domain[loop]
                                resultSet,session = driver.query('MATCH (c:Computer) where c.name = "'+computer.upper()+'" SET c.cracked_password = "'+pwd+'", c.owned = True RETURN c.name as name')
                                for record in resultSet:
                                    imported = True
                                loop = loop + 1 if not imported else len(domain)
                                session.close()
                            if not imported:
                                print(Fore.RED,"Error : "+userdata[1].upper()+" not found in BloodHound users or computers with all detected domains.",Fore.WHITE)
                else:
                    loop = 0
                    while loop < len(domain):
                        username = user+"@"+domain[loop]
                        resultSet,session = driver.query('MATCH (u:User) where u.name = "'+username.upper()+'" SET u.cracked_password = "'+pwd+'", u.owned = True RETURN u.name as name')
                        for record in resultSet:
                            imported = True
                        loop = loop + 1 if not imported else len(domain)
                        session.close()
                    if not imported:
                        loop = 0
                        while loop < len(domain):
                            if user.endswith('$'):
                                computer = user[:-1]+"."+domain[loop]
                            else:
                                computer = user+"."+domain[loop]
                            resultSet,session = driver.query('MATCH (c:Computer) where c.name = "'+computer.upper()+'" SET c.cracked_password = "'+pwd+'", c.owned = True RETURN c.name as name')
                            for record in resultSet:
                                imported = True
                            loop = loop + 1 if not imported else len(domain)
                            session.close()
                        if not imported:
                            print(Fore.RED,"Error : "+user.upper()+" not found in BloodHound users or computers with all detected domains.",Fore.WHITE)
        file.close()
