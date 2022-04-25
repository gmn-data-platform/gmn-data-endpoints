"""Datasette meteor map."""
from datasette import hookimpl


@hookimpl
def extra_js_urls(database, table, columns, view_name, datasette):
    """
    Add datasette-meteor-map.js file to page if the right meteor columns are on the
     page. More info:
     https://docs.datasette.io/en/stable/plugin_hooks.html#extra-js-urls-template-datab
     ase-table-columns-view-name-request-datasette
    :param database: The database name (gmn_data_store).
    :param table: The table name (meteor or meteor_summary).
    :param columns: The list of column names.
    :param view_name: The view name.
    :param datasette: The datasette object.
    :return: JS list.
    """
    if not has_columns(table, columns, view_name):
        return []
    return [
        {
            "url": datasette.urls.static_plugins(
                "datasette-meteor-map", "datasette-meteor-map.js"
            ),
            "module": True,
        }
    ]


def has_columns(table, columns, view_name) -> bool:
    """
    According to the table, columns and view_name does the page contain the right
     attributes to display the meteor map.
    :param table: The table name (meteor or meteor_summary).
    :param columns: The list of column names.
    :param view_name: The view name.
    :return: True if the page should display the meteor map.
    """
    if not columns:
        return False
    columns = [column.lower() for column in columns]
    return "latbeg_n_deg" in columns and \
           "lonbeg_e_deg" in columns and \
           "latend_n_deg" in columns and \
           "lonend_e_deg" in columns and \
           ("unique_trajectory_identifier" in columns or "id" in columns)
