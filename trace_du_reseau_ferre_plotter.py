import matplotlib.pyplot as plt
import json


with open("idf-mobilite-files/traces-du-reseau-ferre-idf.json") as file:

    foo = json.load(file)

    res_coms = set()
    for elem in foo:
        res_coms.add(elem["res_com"])

    for elem in foo:
        # if "TER" in elem["res_com"] or "TRAIN" in elem["res_com"]:
        #     continue
        # if "METRO" not in elem["res_com"]:
        #     continue
        xs = [a[0] for a in elem["geo_shape"]["geometry"]["coordinates"]]
        ys = [a[1] for a in elem["geo_shape"]["geometry"]["coordinates"]]
        if elem["colourweb_hexa"]:
            color = f"#{elem['colourweb_hexa']}"
        else:
            color = "black"
        plt.plot(xs, ys, color=color)

    plt.axis("equal")
    plt.show()

    print(res_coms)
