"""Add a link to the Google Colab Data Analysis Environment."""
from datasette import hookimpl


@hookimpl
def extra_body_script(database, table, columns, view_name, datasette) -> str:
    """
    Add JavaScript to every Datasette page that adds a Google Colab link to the nav bar.
    :param database: The database name (gmn_data_store).
    :param table: The table name (meteor or meteor_summary).
    :param columns: The list of column names.
    :param view_name: The view name.
    :param datasette: The datasette object.
    :return: A JS string to add to the page.
    """
    return """
    var nav = document.getElementsByTagName("nav")[0];
    var p = document.createElement("p");
    p.style.float = "right";
    var link = document.createElement("a");
    link.setAttribute("href", "https://colab.research.google.com/github/gmn-data-platform/gmn-data-endpoints/blob/dc25444cb98693081443bb31e8f6b2abbed3fde2/gmn_data_analysis_template.ipynb");
    link.setAttribute("target", "_blank");
    link.innerHTML = "Google Colab data analysis template &raquo;";
    link.style.color = "black";
    p.appendChild(link);
    nav.appendChild(p);
    """
