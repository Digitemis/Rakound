class Search:
    def searchUser(self,filter,operator,term):
        if filter == 'all' and operator == 'like':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.name =~ '(?i).*"+term+".*' RETURN DISTINCT(u.name) as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'enabled' and operator == 'like':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.name =~ '(?i).*"+term+".*' AND u.enabled = True RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'all' and operator == 'is':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.name =~ '(?i)"+term+"@.*' RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'enabled' and operator == 'is':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.name =~ '(?i)"+term+"@.*' AND u.enabled = True RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"

    def searchComputer(self,operator,term):
        if operator == 'like':
            return "MATCH (c:Computer) WHERE c.name =~ '(?i).*"+term+".*' WITH COLLECT(c.name) AS computers MATCH (u:User)-[:AdminTo]->(c:Computer) WHERE c.name IN computers RETURN DISTINCT(c.name) as computers, c.operatingsystem as os, c.description as description, c.haslaps as LAPS, COLLECT(u.name) as localAdmins"
        elif operator == 'is':
            return "MATCH (c:Computer) WHERE c.name =~ '(?i)"+term+"..*' WITH COLLECT(c.name) AS computers MATCH (u:User)-[:AdminTo]->(c:Computer) WHERE c.name IN computers RETURN DISTINCT(c.name) as computers, c.operatingsystem as os, c.description as description, c.haslaps as LAPS, COLLECT(u.name) as localAdmins"
        
    def searchPassword(self,filter,operator,term):
        if filter == 'all' and operator == 'like':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.cracked_password =~ '(?i).*"+term+".*' RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'enabled' and operator == 'like':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.cracked_password =~ '(?i).*"+term+".*' AND u.enabled = True RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'all' and operator == 'is':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.cracked_password = '"+term+"' RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'enabled' and operator == 'is':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.cracked_password = '"+term+"' AND u.enabled = True RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'all' and operator == 'empty':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.cracked_password = '' RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'enabled' and operator == 'empty':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.cracked_password = '' AND u.enabled = True RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'all' and operator == 'lm':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.lm = True RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.lm as lm, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'enabled' and operator == 'lm':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE u.lm = True AND u.enabled = True RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.lm as lm, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'all' and operator == 'user_as_pass':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE split(u.name, '@')[0] = toupper(u.cracked_password) RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"
        elif filter == 'enabled' and operator == 'user_as_pass':
            return "MATCH (u:User)-[r:MemberOf]->(g:Group) WHERE g.objectid =~ '(?i)S-1-5-.*-518' OR g.objectid =~ '(?i)S-1-5-.*-512' OR g.objectid =~ '(?i)S-1-5-.*-519' WITH COLLECT(u.name) as admins MATCH (u:User) OPTIONAL MATCH p=(u:User)-[r:AdminTo]->(c:Computer) WITH u,c,admins WHERE split(u.name, '@')[0] = toupper(u.cracked_password) AND u.enabled = True RETURN u.name as account, case WHEN u.name IN admins then 'admin' else 'user' end as type, u.cracked_password as password, u.description as description, u.enabled as status, COLLECT(DISTINCT(c.name)) as localAdminOn"

    def searchDescription(self,operator,term):
        if operator == 'like':
            return "MATCH (b:Base) WHERE NOT last(labels(b)) = 'Group' AND NOT last(labels(b)) = 'OU' AND b.description =~ '(?i).*"+term+".*' RETURN b.name as name, b.description as description, last(labels(b)) as type, b.cracked_password as password"
        elif operator == 'is':
            return "MATCH (b:Base) WHERE NOT last(labels(b)) = 'Group' AND NOT last(labels(b)) = 'OU' AND b.description =~ '(?i)"+term+"' RETURN b.name as name, b.description as description, last(labels(b)) as type, b.cracked_password as password"
        elif operator == 'not_empty':
            return "MATCH (b:Base) WHERE NOT last(labels(b)) = 'Group' AND NOT last(labels(b)) = 'OU' AND NOT b.description IS NULL RETURN b.name as name, b.description as description, last(labels(b)) as type, b.cracked_password as password"