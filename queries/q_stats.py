class Stats:
    def analyzeUserPasswords(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND NOT u.name IN admins return DISTINCT(u.name) as account, u.cracked_password as password"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.enabled = True AND u.cracked_password IS NOT NULL AND NOT u.name IN admins return DISTINCT(u.name) as account, u.cracked_password as password"

    def analyzeUserPasswords10(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND NOT u.name IN admins return DISTINCT(u.cracked_password) as password,COUNT(u.cracked_password) as total ORDER BY total DESC LIMIT 10"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.enabled = True AND u.cracked_password IS NOT NULL AND NOT u.name IN admins return DISTINCT(u.cracked_password) as password,COUNT(u.cracked_password) as total ORDER BY total DESC LIMIT 10"

    def analyzeUserPasswordsType(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.lm = TRUE AND NOT u.name IN admins WITH count(u.name) as lm, admins MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND NOT u.name IN admins WITH lm, count(u.cracked_password) as cracked, admins MATCH (u:User) WHERE NOT u.name IN admins RETURN COUNT(u.name) as users, lm, cracked"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.lm = TRUE AND NOT u.name IN admins AND u.enabled = True WITH count(u.name) as lm, admins MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND NOT u.name IN admins AND u.enabled = True WITH lm, count(u.cracked_password) as cracked, admins MATCH (u:User) WHERE NOT u.name IN admins AND u.enabled = True RETURN COUNT(u.name) as users, lm, cracked"

    def analyzeAdminPasswords(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND u.name IN admins return DISTINCT(u.name) as account, u.cracked_password as password"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.enabled = True AND u.cracked_password IS NOT NULL AND u.name IN admins return DISTINCT(u.name) as account, u.cracked_password as password"

    def analyzeAdminPasswordsData(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND u.name IN admins return u.name as account, u.enabled as enabled, u.cracked_password as password ORDER BY u.name"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.enabled = True AND u.cracked_password IS NOT NULL AND u.name IN admins return u.name as account, u.enabled as enabled, u.cracked_password as password ORDER BY u.name"

    def analyzeAdminPasswordsType(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.lm = TRUE AND u.name IN admins WITH count(u.name) as lm, admins MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND u.name IN admins WITH lm, count(u.cracked_password) as cracked, admins MATCH (u:User) WHERE u.name IN admins RETURN COUNT(u.name) as users, lm, cracked"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(518|512|519|544)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.lm = TRUE AND u.name IN admins AND u.enabled = True WITH count(u.name) as lm, admins MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND u.name IN admins AND u.enabled = True WITH lm, count(u.cracked_password) as cracked, admins MATCH (u:User) WHERE u.name IN admins AND u.enabled = True RETURN COUNT(u.name) as users, lm, cracked"

    def analyzeAllPasswords(self,filter):
        if filter == 'all':
            return "MATCH (u:User) WHERE u.cracked_password IS NOT NULL return DISTINCT(u.name) as account, u.cracked_password as password"
        elif filter == 'enabled':
            return "MATCH (u:User) WHERE u.enabled = True AND u.cracked_password IS NOT NULL return DISTINCT(u.name) as account, u.cracked_password as password"

    def analyzeAllPasswordsType(self,filter):
        if filter == 'all':
            return "MATCH (u:User) WHERE u.lm = TRUE WITH count(u.name) as lm MATCH (u:User) WHERE u.cracked_password IS NOT NULL WITH lm, count(u.cracked_password) as cracked MATCH (u:User) RETURN COUNT(u.name) as users, lm, cracked"
        elif filter == 'enabled':
            return "MATCH (u:User) WHERE u.lm = TRUE AND u.enabled = True WITH count(u.name) as lm MATCH (u:User) WHERE u.cracked_password IS NOT NULL AND u.enabled = True WITH lm, count(u.cracked_password) as cracked MATCH (u:User) WHERE u.enabled = True RETURN COUNT(u.name) as users, lm, cracked"

    def analyzeComputerPasswords(self):
        return "MATCH (c:Computer) WHERE c.cracked_password IS NOT NULL RETURN DISTINCT(c.name) as computer, c.cracked_password as password"
