import solid2
import igraph as ig
import numpy as np
import plotly.graph_objs as go


metro_line_1_stations = [
    "La Défense (Grande Arche)",
    "Esplanade de la Défense",
    "Pont de Neuilly",
    "Les Sablons",
    "Porte Maillot",
    "Argentine",
    "Charles de Gaulle - Etoile",
    "George V",
    "Franklin D. Roosevelt",
    "Champs-Élysées - Clemenceau",
    "Concorde",
    "Tuileries",
    "Palais Royal - Musée du Louvre",
    "Louvre - Rivoli",
    "Châtelet",
    "Hôtel de Ville",
    "Saint-Paul (Le Marais)",
    "Bastille",
    "Gare de Lyon",
    "Reuilly - Diderot",
    "Nation",
    "Porte de Vincennes",
    "Saint-Mandé",
    "Bérault",
    "Château de Vincennes",
]

metro_line_2_stations = [
    "Porte Dauphine",
    "Victor Hugo",
    "Charles de Gaulle - Etoile",
    "Ternes",
    "Courcelles",
    "Monceau",
    "Villiers",
    "Rome",
    "Place de Clichy",
    "Blanche",
    "Pigalle",
    "Anvers",
    "Barbès - Rochechouart",
    "La Chapelle",
    "Stalingrad",
    "Jaurès",
    "Colonel Fabien",
    "Belleville",
    "Couronnes",
    "Ménilmontant",
    "Père Lachaise",
    "Philippe Auguste",
    "Alexandre Dumas",
    "Avron",
    "Nation",
]

metro_line_3_stations = [
    "Pont de Levallois - Bécon",
    "Anatole France",
    "Louise Michel",
    "Porte de Champerret",
    "Pereire",
    "Wagram",
    "Malesherbes",
    "Villiers",
    "Europe",
    "Saint-Lazare",
    "Havre-Caumartin",
    "Opéra",
    "Quatre Septembre",
    "Bourse",
    "Sentier",
    "Réaumur - Sébastopol",
    "Arts et Métiers",
    "Temple",
    "République",
    "Parmentier",
    "Rue Saint-Maur",
    "Père Lachaise",
    "Gambetta",
    "Porte de Bagnolet",
    "Gallieni",
]

metro_line_3bis_stations = [
    "Porte des Lilas",
    "Saint-Fargeau",
    "Pelleport",
    "Gambetta",
]

metro_line_4_stations = [
    "Porte de Clignancourt",
    "Simplon",
    "Marcadet - Poissonniers",
    "Château Rouge",
    "Barbès - Rochechouart",
    "Gare du Nord",
    "Gare de l'Est",
    "Château d'Eau",
    "Strasbourg - Saint-Denis",
    "Réaumur - Sébastopol",
    "Etienne Marcel",
    "Les Halles",
    "Châtelet",
    "Cité",
    "Saint-Michel",
    "Odéon",
    "Saint-Germain-des-Prés",
    "Saint-Sulpice",
    "Saint-Placide",
    "Montparnasse Bienvenue",
    "Vavin",
    "Raspail",
    "Denfert-Rochereau",
    "Mouton-Duvernet",
    "Alésia",
    "Porte d'Orléans",
    "Mairie de Montrouge",
    "Barbara",
    "Bagneux - Lucie Aubrac",
]

metro_line_5_stations = [
    "Bobigny Pablo Picasso",
    "Bobigny-Pantin - Raymond Queneau",
    "Église de Pantin",
    "Hoche",
    "Porte de Pantin",
    "Ourcq",
    "Laumière",
    "Jaurès",
    "Stalingrad",
    "Gare du Nord",
    "Gare de l'Est",
    "Jacques Bonsergent",
    "République",
    "Oberkampf",
    "Richard-Lenoir",
    "Bréguet-Sabin",
    "Bastille",
    "Quai de la Rapée",
    "Gare d'Austerlitz",
    "Saint-Marcel",
    "Campo-Formio",
    "Place d'Italie",
]

metro_line_6_stations = [
    "Charles de Gaulle - Etoile",
    "Kléber",
    "Boissière",
    "Trocadéro",
    "Passy",
    "Bir-Hakeim",
    "Dupleix",
    "La Motte-Picquet - Grenelle",
    "Cambronne",
    "Sèvres-Lecourbe",
    "Pasteur",
    "Montparnasse Bienvenue",
    "Edgar Quinet",
    "Raspail",
    "Denfert-Rochereau",
    "Saint-Jacques",
    "Glacière",
    "Corvisart",
    "Place d'Italie",
    "Nationale",
    "Chevaleret",
    "Quai de la Gare",
    "Bercy",
    "Dugommier",
    "Daumesnil",
    "Bel-Air",
    "Picpus",
    "Nation",
]

metro_line_7_stations = [
    "La Courneuve - 8 Mai 1945",
    "Fort d'Aubervilliers",
    "Aubervilliers-Pantin Quatre Chemins",
    "Porte de la Villette",
    "Corentin Cariou",
    "Crimée",
    "Riquet",
    "Stalingrad",
    "Louis Blanc",
    "Château Landon",
    "Gare de l'Est",
    "Poissonnière",
    "Cadet",
    "Le Peletier",
    "Chaussée d'Antin - La Fay_edgestte",
    "Opéra",
    "Pyramides",
    "Palais Royal - Musée du Louvre",
    "Pont Neuf",
    "Châtelet",
    "Pont Marie (Cité des Arts)",
    "Sully - Morland",
    "Jussieu",
    "Place Monge",
    "Censier - Daubenton",
    "Les Gobelins",
    "Place d'Italie",
    "Tolbiac",
    "Maison Blanche",
    "Porte d'Italie",
    "Porte de Choisy",
    "Porte d'Ivry",
    "Pierre et Marie Curie",
    "Mairie d'Ivry",
]

metro_line_7_branch_stations = [
    "Maison Blanche",
    "Le Kremlin-Bicêtre",
    "Villejuif Léo Lagrange",
    "Villejuif Paul Vaillant-Couturier",
    "Villejuif - Louis Aragon",
]


metro_line_7bis_stations = [
    "Louis Blanc",
    "Jaurès",
    "Bolivar",
    "Buttes Chaumont",
    "Botzaris",
    "Place des Fêtes",
    "Pré-Saint-Gervais",
    "Danube",
    "Botzaris",
]

metro_line_8_stations = [
    "Balard",
    "Lourmel",
    "Boucicaut",
    "Félix Faure",
    "Commerce",
    "La Motte-Picquet - Grenelle",
    "École Militaire",
    "La Tour-Maubourg",
    "Invalides",
    "Concorde",
    "Madeleine",
    "Opéra",
    "Richelieu - Drouot",
    "Grands Boulevards",
    "Bonne Nouvelle",
    "Strasbourg - Saint-Denis",
    "République",
    "Filles du Calvaire",
    "Saint-Sébastien - Froissart",
    "Chemin Vert",
    "Bastille",
    "Ledru-Rollin",
    "Faidherbe - Chaligny",
    "Reuilly - Diderot",
    "Montgallet",
    "Daumesnil",
    "Michel Bizot",
    "Porte Dorée",
    "Porte de Charenton",
    "Liberté",
    "Charenton - Écoles",
    "Ecole Vétérinaire de Maisons-Alfort",
    "Maisons-Alfort - Stade",
    "Maisons-Alfort - Les Juilliottes",
    "Créteil - L'Échat",
    "Créteil - Université",
    "Créteil - Préfecture",
    "Pointe du Lac",
]

metro_line_9_stations = [
    "Pont de Sèvres",
    "Billancourt",
    "Marcel Sembat",
    "Porte de Saint-Cloud",
    "Ex_edgeslmans",
    "Michel-Ange - Molitor",
    "Michel-Ange - Auteuil",
    "Jasmin",
    "Ranelagh",
    "La Muette",
    "Rue de la Pompe",
    "Trocadéro",
    "Iéna",
    "Alma - Marceau",
    "Franklin D. Roosevelt",
    "Saint-Philippe du Roule",
    "Miromesnil",
    "Saint-Augustin",
    "Havre-Caumartin",
    "Chaussée d'Antin - La Fay_edgestte",
    "Richelieu - Drouot",
    "Grands Boulevards",
    "Bonne Nouvelle",
    "Strasbourg - Saint-Denis",
    "République",
    "Oberkampf",
    "Saint-Ambroise",
    "Voltaire",
    "Charonne",
    "Rue des Boulets",
    "Nation",
    "Buz_edgesnval",
    "Maraîchers",
    "Porte de Montreuil",
    "Robespierre",
    "Croix de Chavaux",
    "Mairie de Montreuil",
]

metro_line_10_stations = [
    "Boulogne Pont de Saint-Cloud",
    "Boulogne Jean Jaurès",
    "Michel-Ange - Molitor",
    "Chardon Lagache",
    "Mirabeau",
    "Javel - André Citroën",
    "Charles Michels",
    "Avenue Émile Zola",
    "La Motte-Picquet - Grenelle",
    "Ségur",
    "Duroc",
    "Vaneau",
    "Sèvres - Babylone",
    "Mabillon",
    "Odéon",
    "Cluny - La Sorbonne",
    "Maubert - Mutualité",
    "Cardinal Lemoine",
    "Jussieu",
    "Gare d'Austerlitz",
]

metro_line_10_loop_stations = [
    "Javel - André Citroën",
    "Église d'Auteuil",
    "Michel-Ange - Auteuil",
    "Porte d'Auteuil",
    "Boulogne Jean Jaurès",
]

metro_line_11_stations = [
    "Châtelet",
    "Hôtel de Ville",
    "Rambuteau",
    "Arts et Métiers",
    "République",
    "Goncourt",
    "Belleville",
    "Pyrénées",
    "Jourdain",
    "Place des Fêtes",
    "Télégraphe",
    "Porte des Lilas",
    "Mairie des Lilas",
]

metro_line_12_stations = [
    "Mairie d'Aubervilliers",
    "Aimé Césaire",
    "Front Populaire",
    "Porte de la Chapelle",
    "Marx Dormoy",
    "Marcadet - Poissonniers",
    "Jules Joffrin",
    "Lamarck - Caulaincourt",
    "Abbesses",
    "Pigalle",
    "Saint-Georges",
    "Notre-Dame-de-Lorette",
    "Trinité - d'Estienne d'Orves",
    "Saint-Lazare",
    "Madeleine",
    "Concorde",
    "Assemblée Nationale",
    "Solférino",
    "Rue du Bac",
    "Sèvres - Babylone",
    "Rennes",
    "Notre-Dame des Champs",
    "Montparnasse Bienvenue",
    "Falguière",
    "Pasteur",
    "Volontaires",
    "Vaugirard",
    "Convention",
    "Porte de Versailles",
    "Corentin Celton",
    "Mairie d'Issy",
]

metro_line_13_stations = [
    "Saint-Denis - Université",
    "Basilique de Saint-Denis",
    "Saint-Denis - Porte de Paris",
    "Carrefour Pley_edgesl",
    "Mairie de Saint-Ouen",
    "Garibaldi",
    "Porte de Saint-Ouen",
    "Guy Môquet",
    "La Fourche",
    "Place de Clichy",
    "Liège",
    "Saint-Lazare",
    "Miromesnil",
    "Champs-Élysées - Clemenceau",
    "Invalides",
    "Varenne",
    "Saint-François-Xavier",
    "Duroc",
    "Montparnasse Bienvenue",
    "Gaîté",
    "Pernety",
    "Plaisance",
    "Porte de Vanves",
    "Malakoff - Plateau de Vanves",
    "Malakoff - Rue Etienne Dolet",
    "Châtillon-Montrouge",
]

metro_line_13_branch_stations = [
    "Asnières - Gennevilliers Les Courtilles",
    "Les Agnettes",
    "Gabriel Péri",
    "Mairie de Clichy",
    "Porte de Clichy",
    "Brochant",
    "La Fourche",
]


metro_line_14_stations = [
    "Mairie de Saint-Ouen",
    "Saint-Ouen",
    "Porte de Clichy",
    "Pont Cardinet",
    "Saint-Lazare",
    "Madeleine",
    "Pyramides",
    "Châtelet",
    "Gare de Lyon",
    "Bercy",
    "Cour Saint-Emilion",
    "Bibliothèque François Mitterrand",
    "Olympiades",
]

master_list = [
    {
        "name": "1",
        "color": "#ffbe00",
        "stations": metro_line_1_stations,
    },
    {
        "name": "2",
        "color": "#0055c8",
        "stations": metro_line_2_stations,
    },
    {
        "name": "3",
        "color": "#6e6e00",
        "stations": metro_line_3_stations,
    },
    {
        "name": "3bis",
        "color": "#6ec4e8",
        "stations": metro_line_3bis_stations,
    },
    {
        "name": "4",
        "color": "#a0006e",
        "stations": metro_line_4_stations,
    },
    {
        "name": "5",
        "color": "#ff7e2e",
        "stations": metro_line_5_stations,
    },
    {
        "name": "6",
        "color": "#6eca97",
        "stations": metro_line_6_stations,
    },
    {
        "name": "7",
        "color": "#f49fb3",
        "stations": metro_line_7_stations,
    },
    {
        "name": "7",
        "color": "#f49fb3",
        "stations": metro_line_7_branch_stations,
    },
    {
        "name": "7bis",
        "color": "#6eca97",
        "stations": metro_line_7bis_stations,
    },
    {
        "name": "8",
        "color": "#d282be",
        "stations": metro_line_8_stations,
    },
    {
        "name": "9",
        "color": "#b6bd00",
        "stations": metro_line_9_stations,
    },
    {
        "name": "10",
        "color": "#c9910d",
        "stations": metro_line_10_stations,
    },
    {
        "name": "10",
        "color": "#c9910d",
        "stations": metro_line_10_loop_stations,
    },
    {
        "name": "11",
        "color": "#704b1c",
        "stations": metro_line_11_stations,
    },
    {
        "name": "12",
        "color": "#007852",
        "stations": metro_line_12_stations,
    },
    {
        "name": "13",
        "color": "#6ec4e8",
        "stations": metro_line_13_stations,
    },
    {
        "name": "13",
        "color": "#6ec4e8",
        "stations": metro_line_13_branch_stations,
    },
    {
        "name": "14",
        "color": "#62259d",
        "stations": metro_line_14_stations,
    },
]


def return_angles_rotation_2_points(P, Q):
    # with logic from https://stackoverflow.com/questions/50869080/openscad-how-to-draw-a-cylinder-from-vector-to-vector
    # and from https://stackoverflow.com/questions/15022630/how-to-calculate-the-angle-from-rotation-matrix

    P = np.array(P)
    Q = np.array(Q)

    v = Q - P
    c = v / np.linalg.norm(v)
    u = np.cross([0, 0, 1], c)  # this fails if c is vertical
    a = u / np.linalg.norm(u)
    b = np.cross(c, a)

    tx = np.arctan2(b[2], c[2]) * 180 / np.pi
    ty = np.arctan2(-a[2], np.sqrt(b[2] ** 2 + c[2] ** 2)) * 180 / np.pi
    tz = np.arctan2(a[1], a[0]) * 180 / np.pi

    return tx, ty, tz


def generate_scad_file():

    SCALE = 11
    BALL_RADOUS = 2.5
    CYLINDER_RADIUS = 1.75

    solid2.set_global_fs(0.1)
    d = solid2.sphere(r=0)

    for elem in all_stations_with_duplicates:

        id = all_stations_name_number_mapping[elem]
        d += solid2.translate([layout[id][0], layout[id][1], layout[id][2]])(
            solid2.sphere(r=BALL_RADOUS / SCALE)
        )

    for line in master_list:
        for i in range(len(line["stations"]) - 1):
            station_1_id = all_stations_name_number_mapping[line["stations"][i]]
            station_2_id = all_stations_name_number_mapping[line["stations"][i + 1]]

            P = [
                layout[station_1_id][0],
                layout[station_1_id][1],
                layout[station_1_id][2],
            ]
            Q = [
                layout[station_2_id][0],
                layout[station_2_id][1],
                layout[station_2_id][2],
            ]
            tx, ty, tz = return_angles_rotation_2_points(P, Q)
            length = np.linalg.norm(np.array(P) - np.array(Q))
            d += solid2.translate(P)(
                solid2.rotate([tx, ty, tz])(
                    solid2.cylinder(r=CYLINDER_RADIUS / SCALE, h=length)
                )
            )

    d = solid2.scale(SCALE)(d)

    solid2.scad_render_to_file(d, "scad/paris_metro_3d.scad")


all_stations_with_duplicates = []
for elem in master_list:
    all_stations_with_duplicates.extend(elem["stations"])
all_stations_set = set(all_stations_with_duplicates)

all_stations_name_number_mapping = {
    station_name: i for i, station_name in enumerate(all_stations_set)
}

edges = []

for line in master_list:
    for i in range(len(line["stations"]) - 1):
        station_1_name = line["stations"][i]
        station_2_name = line["stations"][i + 1]
        edge = [
            all_stations_name_number_mapping[station_1_name],
            all_stations_name_number_mapping[station_2_name],
        ]
        edges.append(edge)


G = ig.Graph(edges, directed=False)

layout = G.layout("kk", dim=3)
# layout = G.layout("drl", dim=3)
# layout = G.layout("fruchterman_reingold", dim=3)
# layout = G.layout("grid_3d", dim=3)


# Build the model is plotly
traces = []

for line in master_list:
    x_edges = []
    y_edges = []
    z_edges = []
    for i in range(len(line["stations"]) - 1):
        station_1_id = all_stations_name_number_mapping[line["stations"][i]]
        station_2_id = all_stations_name_number_mapping[line["stations"][i + 1]]

        x_edges += [layout[station_1_id][0], layout[station_2_id][0]]
        y_edges += [layout[station_1_id][1], layout[station_2_id][1]]
        z_edges += [layout[station_1_id][2], layout[station_2_id][2]]

    trace = go.Scatter3d(
        x=x_edges,
        y=y_edges,
        z=z_edges,
        mode="lines",
        line=dict(color=line["color"], width=15),
        name=line["name"],
        hoverinfo="none",
    )
    traces.append(trace)

x_nodes = [layout[k][0] for k in range(len(all_stations_set))]
y_nodes = [layout[k][1] for k in range(len(all_stations_set))]
z_nodes = [layout[k][2] for k in range(len(all_stations_set))]

trace_2 = go.Scatter3d(
    x=x_nodes,
    y=y_nodes,
    z=z_nodes,
    mode="markers",
    name="stations",
    marker=dict(
        symbol="circle",
        size=10,
        color="gray",
    ),
    text=list(all_stations_set),
    hoverinfo="text",
)

traces.append(trace_2)

fig = go.Figure(data=traces)

fig.update_layout(title="3D Representation of the Paris metro network")

fig.show()

generate_scad_file()
