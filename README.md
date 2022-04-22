# GMN Data Endpoints
Global Meteor Network data portal and REST API. 

This project provides user-facing interfaces for accessing data in the [GMN Data Store](https://github.com/gmn-data-platform/gmn-data-store). The GMN REST API can query data stored in the GMN Data Store SQLite database (readonly restricted). And the GMN Data Portal is a web interface to view and query the data. The GMN Data Store database is accessed using the gmn-data-store python package and the gmn_data_store volume is mounted using Docker volumes (more info on the GMN Data Store repo).

The GMN REST API and GMN Data Portal are provided by [Datasette](https://datasette.io/). Datasette plugins have been set up to alter the interface and data access methods. The index page has also been overridden. As well as interface changes, a [meteor map](https://github.com/gmn-data-platform/gmn-data-endpoints/tree/2fd5a17a683840fe1cce60932e3af70d9ba74928/services/gmn_data_portal/datasette-meteor-map) plugin has also been written to visualise meteors on an interactive map using [Leaflet](https://leafletjs.com/). 

These services can be started up using the [Makefile](https://github.com/gmn-data-platform/gmn-data-endpoints/blob/2fd5a17a683840fe1cce60932e3af70d9ba74928/Makefile).

See the [GMN REST API Docs](https://github.com/gmn-data-platform/gmn-data-endpoints/blob/main/gmn_rest_api_docs.md) for more info about querying data using the GMN REST API.

IPython data analysis notebooks for the `gmn-python-api` are also provided here.

More info: https://github.com/gmn-data-platform/gmn-data-platform

## Requirements
| Prerequisite                                                      | Description                                             |
|-------------------------------------------------------------------|---------------------------------------------------------|
| [Docker](https://www.docker.com/)                                 | Container management tool                               |
| [Docker Compose v2](https://docs.docker.com/compose/cli-command/) | A tool for defining multi-container apps                |
| [GNU Make 4.1+](https://www.gnu.org/software/make/)               | A tool which allows an easy way to run project commands |

## Usage
```sh
make run_all_services
```

Note that the `gmn_data_store` volume should be created beforehand (see the [init task](https://github.com/gmn-data-platform/gmn-data-store/blob/7a6f0038c6926703ab130b46b72fa9aede07ac0e/Makefile) in the GMN Data Store Makefile).

See the Makefile for more provided tasks.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide](https://github.com/gmn-data-platform/gmn-data-endpoints/blob/main/CONTRIBUTING.rst).

## License

Distributed under the terms of the [MIT license](https://opensource.org/licenses/MIT), GMN Data Platform Monitoring is free and open source software.

## Issues

If you encounter any problems, please [file an issue](https://github.com/gmn-data-platform/gmn-data-endpoints/issues) along with a detailed description.
