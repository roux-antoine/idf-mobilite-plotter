import matplotlib.pyplot as plt

import json

color_mapping = {
    "1": "#ffbe00",
    "2": "#0055c8",
    "3": "#6e6e00",
    "3B": "#6ec4e8",
    "4": "#a0006e",
    "5": "#ff7e2e",
    "6": "#6eca97",
    "7": "#f49fb3",
    "7B": "#6eca97",
    "8": "#d282be",
    "9": "#b6bd00",
    "10": "#c9910d",
    "11": "#704b1c",
    "12": "#007852",
    "13": "#6ec4e8",
    "14": "#62259d",
}

with open(
    "idf-mobilite-files/traces-des-lignes-de-transport-en-commun-idfm.json"
) as file:

    routes = json.load(file)

    color_counter = 0
    for route in routes:

        if route["route_type"] != "Subway":
            continue
        color_counter += 1
        if "shape" in route and "geometry" in route["shape"]:
            coordinates = route["shape"]["geometry"]["coordinates"]
            for coordinate in coordinates:
                for i in range(len(coordinate) - 1):
                    plt.plot(
                        [coordinate[i][0], coordinate[i + 1][0]],
                        [coordinate[i][1], coordinate[i + 1][1]],
                        color=color_mapping[route["route_long_name"]],
                    )

    plt.show()
