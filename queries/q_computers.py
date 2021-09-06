class Computers:
    def getObsolete(self):
        return "MATCH (c:Computer) WHERE c.operatingsystem =~ '(?i).*(2000|2003|2008|xp|vista|7|me).*' RETURN DISTINCT(c.operatingsystem) as os,COLLECT(DISTINCT(c.name)) as name, COUNT(c.name) as total ORDER BY total DESC"

    def getLAPS(self):
        return "MATCH (c:Computer) WHERE c.haslaps = True RETURN c.name as name, c.haslaps as laps"
