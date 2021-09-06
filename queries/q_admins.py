class Admins:
    def get_domain_admins(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-512' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-512' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_enterprise_admins(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-519' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-519' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_schema_admins(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-518' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-518' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_account_operators(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-548' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-548' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_administrators(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-544' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-544' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_backup_operators(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-551' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-551' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_print_operators(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-550' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-550' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_replicators(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-552' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-552' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_server_operators(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-549' \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-549' \
                    AND u.enabled = True \
                    RETURN \
                      u.name as account, \
                      u.enabled as status"

    def get_adminsdholder(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ \
                      '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' \
                    RETURN \
                      DISTINCT(g.name) as group, \
                      COLLECT(DISTINCT(u.name)+'('+\
                        CASE u.enabled WHEN True \
                        THEN 'Enabled' \
                        ELSE 'Disabled' \
                        END+')') as account"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ \
                    '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' \
                    AND u.enabled = True \
                    RETURN \
                      DISTINCT(g.name) as group, \
                      COLLECT(DISTINCT(u.name)+'('+\
                        CASE u.enabled WHEN True \
                        THEN 'Enabled' \
                        ELSE 'Disabled' \
                        END+')') as account"

    def get_password_never_expires(self, filter):
        if filter == 'all':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' \
                    WITH COLLECT(u.name) as admins \
                    MATCH (u:User) \
                    WHERE u.name IN admins \
                    AND u.pwdneverexpires = True \
                    RETURN \
                      DISTINCT(u.name) as account, \
                      u.enabled as status, \
                      u.pwdneverexpires as pwdneverexpires"
        elif filter == 'enabled':
            return "MATCH p=(u:User)-[r:MemberOf]->(g:Group) \
                    WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' \
                    WITH COLLECT(u.name) as admins \
                    MATCH (u:User) \
                    WHERE u.name IN admins \
                    AND u.pwdneverexpires = True \
                    AND u.enabled = True \
                    RETURN \
                      DISTINCT(u.name) as account, \
                      u.enabled as status, \
                      u.pwdneverexpires as pwdneverexpires"
