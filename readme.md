# Reference
- [Snowflake] (https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-install) 

- [Snowflake API] (https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api)

- [Querying] (https://hex.tech/blog/connecting-snowflake-python/)

- [Querying by Chunk] (https://docs.snowflake.com/developer-guide/python-connector/python-connector-pandas#installation)

# Install
- pip install snowflake-connector-python --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org

- pip install pandas --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org

- pip install "snowflake-connector-python[pandas]" --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org

- pip install fastapi --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org

- pip install "uvicorn[standard]" --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org

# run
- uvicorn main:app --reload

- curl localhost:8000/
- curl localhost:8000/ping
- curl localhost:8000/getTotalNLA
- curl localhost:8000/getLeaseExpiry
- curl localhost:8000/getPortfolioCommitedOccupancy
- curl localhost:8000/getAveEffectiveGrossRent
- curl localhost:8000/getTenantMix
- curl localhost:8000/getWale
- curl localhost:8000/getRentalReversion
- curl localhost:8000/getTop10Tenants