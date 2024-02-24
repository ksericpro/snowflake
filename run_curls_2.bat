@echo Started: %date% %time%
curl localhost:8000/getTenantMix
curl localhost:8000/getWale
curl localhost:8000/getRentalReversion
curl localhost:8000/getTop10Tenants
curl localhost:8000/getTotalNLA
curl localhost:8000/getLeaseExpiry
curl localhost:8000/getPortfolioCommitedOccupancy
curl localhost:8000/getAveEffectiveGrossRent
@echo Ended: %date% %time%