from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials
from cognite_data_reader import CogniteDataReader

TENANT_ID = "48d5043c-cf70-4c49-881c-c638f5796997"
CLIENT_ID = "1b90ede3-271e-401b-81a0-a4d52bea3273"
CLIENT_SECRET = "secret-change-me"
CDF_CLUSTER = "api"
COGNITE_PROJECT = "publicdata"

base_url = f"https://{CDF_CLUSTER}.cognitedata.com"

creds = OAuthClientCredentials(
    token_url=f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scopes=[f"{base_url}/.default"]
)

cnf = ClientConfig(
    client_name="aalkhodiry-client",
    project=COGNITE_PROJECT,
    credentials=creds,
    base_url=base_url
)

client = CogniteClient(cnf)

# Need this to get the external IDs of all time series

# all_timeseries = client.time_series.list(limit=-1).to_pandas()
# all_timeseries = all_timeseries[['external_id', 'name', 'asset_id', 'created_time', 'last_updated_time', 'metadata']]
# all_timeseries.to_csv('all_timeseries.csv', index=False)
# print("All timeseries data saved to 'all_timeseries.csv'")
# print(len(all_timeseries))
# print(all_timeseries.head(10).T)

cdr = CogniteDataReader(client)

# after getting the external ID, use this to get the time series data
print(cdr.get_time_series_by_external_id(external_id="pi:160182"))