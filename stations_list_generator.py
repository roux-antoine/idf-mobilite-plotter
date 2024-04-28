import pandas as pd

allowed_values = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "3B",
    "7B",
]

columns_to_check = ["route_long_name", "stop_name"]

############

df = pd.read_csv("idf-mobilite-files/arrets-lignes.csv")

df_ratp_only = df[df["OperatorName"] == "RATP"]

df_subset_lines = df_ratp_only[df_ratp_only["route_long_name"].isin(allowed_values)]

# sometimes there are multiple entries for a same station for a given line, removing them
df_filtered = df_subset_lines.drop_duplicates(subset=columns_to_check, keep="first")

all_stations = list(
    df_filtered.drop_duplicates(subset=["stop_name"], keep="first")["stop_name"]
)

print(all_stations)
print(len(all_stations))
