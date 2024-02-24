import argparse
import config
import snowflakemgr
import logmgr
import eventmgr

def getMenu(mgr):
    while True:
        print("Menu:")
        print("1. getTotalNLA")
        print("2. getLeaseExpiry")
        print("3. getPortfolioCommitedOccupancy")
        print("4. getAveEffectiveGrossRent")
        print("5. getTenantMix")
        print("6. getWale")
        print("7. getRentalReversion")
        print("8. getTop10Tenants")
        print("9. Run All")
        print("q. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            mgr.getTotalNLA()
        elif choice == '2':
            mgr.getLeaseExpiry()
        elif choice == '3':
            mgr.getPortfolioCommitedOccupancy()
        elif choice == '4':
            mgr.getAveEffectiveGrossRent()
        elif choice == '5':
            mgr.getTenantMix()
        elif choice == '6':
            mgr.getWale()
        elif choice == '7':
            mgr.getRentalReversion()
        elif choice == '8':
            mgr.getTop10Tenants()
        elif choice == '9':
            mgr.getTotalNLA()
            mgr.getLeaseExpiry()
            mgr.getPortfolioCommitedOccupancy()
            mgr.getAveEffectiveGrossRent()
            mgr.getTenantMix()
            mgr.getWale()
            mgr.getRentalReversion()
            mgr.getTop10Tenants()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option ")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--menu", default="0")

    args = parser.parse_args()
    menu = args.menu
    print("menu="+menu)

    _logger = logmgr.getLogger("snowflake_")
    _logger.info("Started")

    _eventmgr = eventmgr.EventMgr("data/run_queries.csv")

    mgr = snowflakemgr.SnowflakeMgr(_logger, _eventmgr, config.USER, config.PASSWORD, config.HOST, config.WAREHOUSE_PROD, config.DATABASE, config.SCHEMA, config.ROLE)
    mgr.connect()

    if menu=="1":
        getMenu(mgr)
    else:
        mgr.getTotalNLA()
        mgr.getLeaseExpiry()
        mgr.getPortfolioCommitedOccupancy()
        mgr.getAveEffectiveGrossRent()
        mgr.getTenantMix()
        mgr.getWale()
        mgr.getRentalReversion()
        mgr.getTop10Tenants()
    mgr.close() 

if __name__ == "__main__":
    main()