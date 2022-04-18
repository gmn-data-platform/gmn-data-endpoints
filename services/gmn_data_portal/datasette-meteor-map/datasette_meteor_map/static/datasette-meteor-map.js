document.addEventListener("DOMContentLoaded", () => {
        // Only execute on table, query and row pages
        if (document.querySelector("body.table,body.row,body.query")) {
            // Create meteor trail svg
            document.body.appendChild(document.createElement("div")).innerHTML = `
             <svg xmlns="http://www.w3.org/2000/svg">
                <defs>
                  <linearGradient id="TrailGradient">
                    <stop offset="5%" stop-color="#000000" />
                    <stop offset="95%" stop-color="#725a00" />
                  </linearGradient>
                </defs>
              </svg>`

            function isValidLatitude(latitude) {
                latitude = parseFloat(latitude);
                if (isNaN(latitude)) {
                    return false;
                }
                return latitude >= -90 && latitude <= 90;
            }

            function isValidLongitude(longitude) {
                longitude = parseFloat(longitude);
                if (isNaN(longitude)) {
                    return false;
                }
                return longitude >= -180 && longitude <= 180;
            }

            // Get lat and long columns
            let columns = Array.prototype.map.call(
                document.querySelectorAll("table.rows-and-columns th"),
                (th) => (th.getAttribute("data-column") || th.textContent).trim()
            );
            let latbeg_n_degColumn = null;
            let lonbeg_e_degColumn = null;
            let latend_n_degColumn = null;
            let lonend_e_degColumn = null;
            columns.forEach((col) => {
                if (
                    col.toLowerCase() === "latbeg_n_deg".toLowerCase()
                ) {
                    latbeg_n_degColumn = col;
                }
                if (
                    col.toLowerCase() === "lonbeg_e_deg".toLowerCase()
                ) {
                    lonbeg_e_degColumn = col;
                }
                if (
                    col.toLowerCase() === "latend_n_deg".toLowerCase()
                ) {
                    latend_n_degColumn = col;
                }
                if (
                    col.toLowerCase() === "lonend_e_deg".toLowerCase()
                ) {
                    lonend_e_degColumn = col;
                }
            });

            // Does it have Latitude and Longitude columns?
            if (latbeg_n_degColumn && lonbeg_e_degColumn && latbeg_n_degColumn && lonbeg_e_degColumn) {
                let path = location.pathname + ".json" + location.search;
                if (path.indexOf("?") > -1) {
                    path += "&_size=max&_labels=on&_shape=objects";
                } else {
                    path += "?_size=max&_labels=on&_shape=objects";
                }
                // Load json data into leaflet
                fetch(path)
                    .then((response) => response.json())
                    .then((data) => {
                        let link = document.createElement('link');
                        link.rel = 'stylesheet';
                        link.href = datasette.leaflet.CSS_URL;
                        document.head.appendChild(link);
                        import(datasette.leaflet.JAVASCRIPT_URL)
                            .then((leaflet) => {
                                let div = document.createElement('div');
                                div.style.width = "100%";
                                div.style.height = "350px";
                                div.style.marginBottom = "20px";

                                let table =
                                    document.querySelector(".table-wrapper") ||
                                    document.querySelector("table.rows-and-columns");
                                table.parentNode.insertBefore(div, table);

                                let tiles = leaflet.tileLayer(
                                    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                                    {
                                        "maxZoom": 19,
                                        "detectRetina": true,
                                        "attribution": "&copy; <a href=\"https://www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors"
                                    }
                                );
                                let map = leaflet.map(div, {
                                    center: leaflet.latLng(0, 0),
                                    zoom: 2,
                                    layers: [tiles]
                                });

                                let lines = [];
                                console.log(data.rows);
                                data.rows.forEach((row) => {
                                    let latbeg_n_deg = row.latbeg_n_deg;
                                    let lonbeg_e_deg = row.lonbeg_e_deg;
                                    let latend_n_deg = row.latend_n_deg;
                                    let lonend_e_deg = row.lonend_e_deg;
                                    if (isValidLatitude(latbeg_n_deg) && isValidLongitude(lonbeg_e_deg) && isValidLatitude(latend_n_deg) && isValidLongitude(lonend_e_deg)) {
                                        let line = leaflet.polyline([
                                            [latbeg_n_deg, lonbeg_e_deg],
                                            [latend_n_deg, lonend_e_deg]
                                        ], {
                                            className: 'trail',
                                            color: "black", // note that the color is inverted for the dark theme by default
                                            weight: 1.5,
                                            opacity: 1,
                                            smoothFactor: 1,
                                        });

                                        line.on('mouseover', function () {
                                            this.mySavedWeight = this.options.weight;
                                            this.setStyle({
                                                weight: 8
                                            });
                                        });

                                        line.on('mouseout', function () {
                                            this.setStyle({
                                                weight: this.mySavedWeight
                                            });
                                        });

                                        line.on("click", function (e) {
                                            let lat = (latbeg_n_deg + latend_n_deg) / 2;
                                            let lon = (lonbeg_e_deg + lonend_e_deg) / 2;
                                            let popup = leaflet.popup()
                                                .setLatLng(leaflet.latLng(lat, lon))
                                                .setContent(
                                                    "<div class='popover-content'>" +
                                                    "<div class='popover-header'>" +
                                                    "<h3 class='popover-title'>" +
                                                    "Meteor" +
                                                    "</h3>" +
                                                    "</div>" +
                                                    "<div class='popover-body'>" +
                                                    "<br>" +
                                                    "id: <a href='http://0.0.0.0:8001/gmn_data_store/meteor/" + (row.unique_trajectory_identifier || row.id) + "'>" + (row.unique_trajectory_identifier || row.id) + "</a>" +
                                                    "</br>" +
                                                    "latbeg_n_deg: " + row.latbeg_n_deg +
                                                    "</br>" +
                                                    "lonbeg_e_deg: " + row.lonbeg_e_deg +
                                                    "</br>" +
                                                    "latend_n_deg: " + row.latend_n_deg +
                                                    "</br>" +
                                                    "lonend_e_deg: " + row.lonend_e_deg +
                                                    "</p>" +
                                                    "</div>" +
                                                    "</div>"
                                                );
                                            map.openPopup(popup);
                                        });
                                        map.addLayer(line);
                                        lines.push(line)
                                    }
                                });

                                // Zoom in to fit points nicely on the screen
                                if (lines.length > 0) {
                                    map.fitBounds(
                                        leaflet.featureGroup(lines).getBounds()
                                    );

                                }
                            });
                    })
                ;
            }
        }
    }
)
;
