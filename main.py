from typing import Union
from fastapi import FastAPI
import config
import snowflakemgr
import logmgr
import pandas as pd
import eventmgr

app = FastAPI()

_logger = logmgr.getLogger("api_")
_logger.info("Started")

_eventmgr = eventmgr.EventMgr("data/main-16022024.csv")

mgr = snowflakemgr.SnowflakeMgr(_logger, _eventmgr, config.USER, config.PASSWORD, config.HOST, config.WAREHOUSE_PROD, config.DATABASE, config.SCHEMA, config.ROLE)
mgr.connect()

@app.get("/")
def read_root():
    return {"message": "Welcome to greatest API in the world"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/getTotalNLA")
def getTotalNLA():
    df = mgr.getTotalNLA()
    result = df.to_json(orient="split")
    return result

@app.get("/getLeaseExpiry")
def getLeaseExpiry():
    df = mgr.getLeaseExpiry()
    result = df.to_json(orient="split")
    return result

@app.get("/getPortfolioCommitedOccupancy")
def getPortfolioCommitedOccupancy():
    df = mgr.getPortfolioCommitedOccupancy()
    result = df.to_json(orient="split")
    return result

@app.get("/getAveEffectiveGrossRent")
def getAveEffectiveGrossRent():
    df = mgr.getAveEffectiveGrossRent()
    result = df.to_json(orient="split")
    return result

@app.get("/getTenantMix")
def getTenantMix():
    df = mgr.getTenantMix()
    result = df.to_json(orient="split")
    return result

@app.get("/getWale")
def getWale():
    df = mgr.getWale()
    result = df.to_json(orient="split")
    return result

@app.get("/getRentalReversion")
def getRentalReversion():
    df = mgr.getRentalReversion()
    result = df.to_json(orient="split")
    return result

@app.get("/getTop10Tenants")
def getTop10Tenants():
    df = mgr.getTop10Tenants()
    result = df.to_json(orient="split")
    return result

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}