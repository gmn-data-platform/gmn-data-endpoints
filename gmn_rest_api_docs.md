# GMN REST API Docs

**Note that the GMN REST API is not deployed in the GMN server yet. Links here may be broken.**

The GMN REST API can be used to access current [Global Meteor Network](https://globalmeteornetwork.org/) data. 
Global meteor data is generated using a network of low-light cameras pointed towards the night sky. Meteor properties (radiants, orbits, magnitudes and masses) are produced by the GMN and are available through this REST API.
To take a look at the available data with an easy-to-use web interface visit the [GMN Data Portal]().

The GMN REST API uses [Datasette](https://datasette.io/) to access and query data in the GMN Data Store (the internal GMN database). The GMN Data Store database schema can be found [here](https://github.com/gmn-data-platform/gmn-data-store/blob/main/database_schema.md). Datasette provides [documentation](https://docs.datasette.io/en/stable/json_api.html) on how to query data using its JSON API.

**Example 1 (accessing the meteor_summary table):**
```sh
GET /gmn_data_store/meteor_summary.json

{
  "database": "gmn_data_store",
  "table": "meteor_summary",
  "is_view": true,
  "human_description_en": "",
  "rows": [
    ["20220304220741_yrPTs", 2459643.422013203, "2022-03-04 22:07:41.940752", ...]
    ["20220401012310_f5I2M", 2459670.5577639486, "2022-04-01 01:23:10.805157", ...],
    ...
  ],
  ...
  "columns": ["unique_trajectory_identifier", "beginning_julian_date", "beginning_utc_time", ...],
  ...
}
```
Note that data is [paginated](https://docs.datasette.io/en/stable/json_api.html#pagination) by 100 rows.

**Example 2 (querying using the `_where` argument):**
```sh
GET /gmn_data_store/iau_shower.json?_shape=array&_where=code="SIA"

[
  {
    "id": 3,
    "code": "SIA",
    "name": "Southern iota Aquariids",
    "created_at": "2022-04-10 21:33:51.876187",
    "updated_at": "2022-04-10 21:33:51.876190"
  }
]
```
The `_where` argument takes an SQL SELECT statement. The `_shape` has also been specified to be just the array of data (not including metadata).

**Example 3 (querying using pure SQL):**
```sh
# SQL: select station_id, COUNT(station_id) from participating_station GROUP BY station_id;
GET /gmn_data_store.csv?sql=select+station_id%2C+COUNT%28station_id%29+from+participating_station+GROUP+BY+station_id%3B

station_id,COUNT(station_id)
1,63
2,22
3,1679
```

The SQL SELECT statement has been run against the GMN Data Store Database. Note that CSV format has also been chosen.

A Python package, [gmn-python-api](https://gmn-python-api.readthedocs.io/en/latest/), has also been developed to allow you to access and query data using functions that abstract the GMN REST API. Refer to the [REST API section](https://gmn-python-api.readthedocs.io/en/latest/rest_api.html) in the GMN Python API docs for more info. SQL select queries can be tested on the GMN Data Portal interface and then used with the GMN Python API to perform the same queries.

**References**:
- GMN Data Store database schema: https://gmn-python-api.readthedocs.io/en/latest/data_schemas.html
- Global Meteor Network - https://globalmeteornetwork.org/
- GMN REST API source code - https://github.com/gmn-data-platform/gmn-data-endpoints
- GMN Data Platform code repository - https://github.com/gmn-data-platform
