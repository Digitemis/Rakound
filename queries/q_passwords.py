class Passwords:
    def getUserPassword(self,filter):
        if filter == 'all':
            return "MATCH (b:Base) WHERE b.userpassword is not null RETURN b.name as account, b.userpassword as userpassword, b.enabled as status, last(labels(b)) as type"
        elif filter == 'enabled':
            return "MATCH (b:Base) WHERE b.userpassword is not null and b.enabled = True RETURN b.name as account, b.userpassword as userpassword, b.enabled as status, last(labels(b)) as type"

    def getPasswordInComment(self,filter):
        if filter == 'all':
            return "MATCH (b:Base) WHERE b.description =~ '(?i).*(pass|pw|mdp|code).*' RETURN b.name as account, b.description as description, b.enabled as status, last(labels(b)) as type"
        elif filter == 'enabled':
            return "MATCH (b:Base) WHERE b.description =~ '(?i).*(pass|pw|mdp|code).*' and b.enabled = true RETURN b.name as account, b.description as description, b.enabled as status, last(labels(b)) as type"

    def getOldPasswords(self,filter,days=90):
        if filter == 'all':
            return "MATCH (u:User) WHERE u.pwdlastset < (datetime().epochseconds - ("+str(days)+" * 86400)) and NOT u.pwdlastset IN [-1.0, 0.0] RETURN u.name as account, u.enabled as status, datetime({epochSeconds: toInteger(u.pwdlastset)}) as pwdlastset order by u.pwdlastset"
        elif filter == "enabled":
            return "MATCH (u:User) WHERE u.enabled = true AND u.pwdlastset < (datetime().epochseconds - ("+str(days)+" * 86400)) and NOT u.pwdlastset IN [-1.0, 0.0] RETURN u.name as account, u.enabled as status, datetime({epochSeconds: toInteger(u.pwdlastset)}) as pwdlastset order by u.pwdlastset"
