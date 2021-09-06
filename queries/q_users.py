class Users:
    def getLocalAdmins(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' WITH COLLECT(u.name) as admins MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WHERE NOT u.name IN admins RETURN DISTINCT(u.name) as account, u.enabled as status, COLLECT(DISTINCT(c.name)) as computer, COUNT(DISTINCT(c.name)) as total ORDER BY total DESC"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' WITH COLLECT(u.name) as admins MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WHERE NOT u.name IN admins AND u.enabled = True RETURN DISTINCT(u.name) as account, u.enabled as status, COLLECT(DISTINCT(c.name)) as computer, COUNT(DISTINCT(c.name)) as total ORDER BY total DESC"

    def getLocalAdminsDC(self,filter):
        if filter == 'all':
            return "MATCH (c:Computer)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-516' WITH COLLECT(c.name) as computers MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' WITH COLLECT(u.name) as admins,computers MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WHERE NOT u.name IN admins AND c.name IN computers RETURN DISTINCT(u.name) as account, u.enabled as status, COLLECT(DISTINCT(c.name)) as computer, COUNT(DISTINCT(c.name)) as total ORDER BY total DESC"
        elif filter == 'enabled':
            return "MATCH (c:Computer)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-516' WITH COLLECT(c.name) as computers MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' WITH COLLECT(u.name) as admins,computers MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WHERE NOT u.name IN admins AND c.name IN computers AND u.enabled RETURN DISTINCT(u.name) as account, u.enabled as status, COLLECT(DISTINCT(c.name)) as computer, COUNT(DISTINCT(c.name)) as total ORDER BY total DESC"

    def getPasswordNeverExpires(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.pwdneverexpires = True AND NOT u.name IN admins RETURN DISTINCT u.name as account,u.enabled as status, u.pwdneverexpires as pwdneverexpires"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' WITH COLLECT(u.name) as admins MATCH (u:User) WHERE u.pwdneverexpires = True AND u.enabled = True AND NOT u.name IN admins RETURN DISTINCT u.name as account,u.enabled as status, u.pwdneverexpires as pwdneverexpires"

    def canReadLapsPassword(self,filter):
        if filter == 'all':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' WITH COLLECT(u.name) as admins MATCH p=(u:User)-[:AllExtendedRights|ReadLAPSPassword]->(c:Computer) WHERE NOT u.name IN admins RETURN DISTINCT(u.name) as account, u.enabled as status, COLLECT(DISTINCT(c.name)) as computer, COUNT(DISTINCT(c.name)) as total ORDER BY total DESC"
        elif filter == 'enabled':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i).*S-1-5-.*-(544|512|519|518|548|549|550|551|552)' WITH COLLECT(u.name) as admins MATCH p=(u:User)-[:AllExtendedRights|ReadLAPSPassword]->(c:Computer) WHERE NOT u.name IN admins AND u.enabled = True RETURN DISTINCT(u.name) as account, u.enabled as status, COLLECT(DISTINCT(c.name)) as computer, COUNT(DISTINCT(c.name)) as total ORDER BY total DESC"