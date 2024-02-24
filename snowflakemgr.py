import snowflake.connector
import pandas as pd
from time import perf_counter as pc
import datetime

class SnowflakeMgr:
    def __init__(self, logger, eventmgr, user, password, host, warehouse, database, schema, role):
        self.logger = logger
        self.eventmgr = eventmgr
        self.user = user
        self.password = password
        self.host = host 
        self.warehouse = warehouse
        self.database = database
        self.schema = schema
        self.role = role
        self.connected = False

    def connect(self):
        self.logger.info("\n[connect]")
        #connection
        self.ctx = snowflake.connector.connect(
            user=self.user,
            password=self.password,
            account=self.host,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema,
            role=self.role
            )
        self.connected = True

    def baseQuery(self, name, sql):
        self.logger.info("\n-[{}]-".format(name))   
        try:
            #create cursor
            cs = self.ctx.cursor()
            t0 = pc()
            tm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")
            cs.execute(sql)
            df = cs.fetch_pandas_all()
            self.logger.info("top 5 rows\n{}".format(df.head()))
            self.logger.info("shape={}".format(df.shape))
            duration = pc() - t0
            self.logger.info("duration={}s".format(duration))
            if self.eventmgr != None:
                self.eventmgr.writeCustom([tm, name, duration])
            return df
        except Exception as err:
            self.logger.error("Unexpected Error=>", err)
            raise

    def getTotalNLA(self):
        sql = 'SELECT * FROM "View_LmsMobileAppGetTotalNLA"'
        return self.baseQuery("gettotalnla", sql)

    def getLeaseExpiry(self):
        sql = 'SELECT "Lease Expiry Category", sum("Expiring Occupied Usage") as "Expiring Occupied Usage", "Total Occupied NLA By Project"  from "View_LmsMobileAppGetLeaseExpiry"' + \
              ' where "Project Name" in (\'All Assets\',\'Central Mall Conservation Unit\',\'Central Mall Office Tower\',\'City House\',\'Fortune Centre\',\'Golden Mile Complex\',\'Katong Shopping Centre\',\'King''s Centre\',\'Republic Plaza\',\'Sunshine Plaza\',\'Tampines Concourse\',\'The Arcade\',\'Waterfront Plaza\')'+ \
              ' GROUP BY "Lease Expiry Category", "Total Occupied NLA By Project"' + \
              ' ORDER BY "Lease Expiry Category" asc'
        return self.baseQuery("getLeaseExpiry", sql)

    def getPortfolioCommitedOccupancy(self):
        sql = 'SELECT "Calculated Date", "Project Name", "Assets Classification", "Usage" ,"Total Occupied By Building", "Space Type NLA" FROM "View_LmsMobileAppGetPortfolioCommittedOccupancy"' + \
              ' where "Calculated Date" >= \'2023-01-01\' and "Calculated Date" <= \'2024-01-31\''
        return self.baseQuery("getPortfolioCommitedOccupancy", sql)

    def getAveEffectiveGrossRent(self):
        sql = 'SELECT "Project Name", "Assets Classification", "Usage", "EGR", "Total Lease NLA"  FROM "View_LmsMobileAppGetAveEffectiveGrossRent"'
        return self.baseQuery("getAveEffectiveGrossRent", sql)

    def getTenantMix(self):
        sql = 'SELECT  "Assets Classification" ,ROUND(SUM("Gross Rent Per Month"),2) AS "Gross Rent Per Month", "Trade Type" from "View_LmsMobileAppGetTenantMixPieChart"' +\
              ' where "Gross Rent Per Month" <> 0' + \
              ' AND "Project Name" IN (\'All Assets\',\'Central Mall Conservation Unit\',\'Central Mall Office Tower\',\'City House\',\'Fortune Centre\',\'Golden Mile Complex\',\'Katong Shopping Centre\',\'King''s Centre\',\'Republic Plaza\',\'Sunshine Plaza\',\'Tampines Concourse\',\'The Arcade\',\'Waterfront Plaza\')' +\
              ' GROUP BY "Assets Classification", "Trade Type"'+\
              ' ORDER BY "Gross Rent Per Month" DESC'
        return self.baseQuery("getTenantMix", sql)

    def getWale(self):
        sql = 'SELECT "Project Name" ,"NLA X Remaining Year", "Asset Total Occupied NLA" FROM "View_LmsMobileAppGetWALE"' +\
              ' where "Project Name" in (\'All Assets\',\'Central Mall Conservation Unit\',\'Central Mall Office Tower\',\'City House\',\'Fortune Centre\',\'Golden Mile Complex\',\'Katong Shopping Centre\',\'King''s Centre\',\'Republic Plaza\',\'Sunshine Plaza\',\'Tampines Concourse\',\'The Arcade\',\'Waterfront Plaza\')'
        return self.baseQuery("getWale", sql)
    
    def getRentalReversion(self):
        sql = 'SELECT "Project Name", "Assets Classification","Usage", "Total EGR Reversion By Usage","Total Previous Revision By Usage", "Total Occupied NLA" FROM "View_LmsMobileAppGetRentalReversion"'
        return self.baseQuery("getRentalReversion", sql)
    
    def getTop10Tenants(self):
        sql = 'SELECT "Project Name", "Assets Classification", "Usage" ,initcap("Tenant Name", \'\') as "Tenant Name", \"NLA\", "Gross Rent Per Month", "Building NLA", "Building Gross Rent Per Month" from "View_LmsMobileAppGetTopTenTenants"'
        return self.baseQuery("getTop10Tenants", sql)

    def close(self):
        print("\n[close]")
        if self.ctx!=None:
            self.ctx.close()