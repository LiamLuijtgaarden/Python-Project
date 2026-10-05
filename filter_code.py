
Invoer:  ongevallen_2024.csv               (landelijk, ~126.000 ongevallen, 39 kolommen)
Uitvoer: ongevallen_2024_amsterdam.csv     (gemeente Amsterdam, ~6.200 ongevallen, 22 kolommen)

import pandas as pd

INPUT_PATH = "ongevallen_2024.csv"
OUTPUT_PATH = "ongevallen_2024_amsterdam.csv"

# Kolommen die we houden.
KOLOMMEN = ["verkeersongeval_nummer","jaar_ongeval","verkeersongeval_afloop","aantal_partijen","partij_1_objecttype",
            "partij_1_objecttype_overig", "partij_2_objecttype","partij_2_objecttype_overig","maximum_snelheid","wegvak_id","junctie_id",
            "niveau_koppelen", "x_rd", "y_rd","straatnaam","woonplaats", "wegbeheerder","bebouwde_kom",
            "wegsituatie","weersgesteldheid","wegdek","lichtgesteldheid"]

# 1. Inlezen. low_memory=False voorkomt waarschuwingen over gemengde kolomtypes.
df = pd.read_csv(INPUT_PATH, low_memory=False)
print(f"Landelijk: {len(df)} ongevallen, {df.shape[1]} kolommen")

# 2. Alleen ongevallen in de gemeente Amsterdam houden.
#    .copy() zodat we daarna veilig nieuwe kolommen kunnen toevoegen.
ams = df[df["gemeente"] == "Amsterdam"].copy()
print(f"Amsterdam: {len(ams)} ongevallen")

# 3. Coördinaten
coords = ams["shape"].str.extract(r"POINT \(([\d.]+) ([\d.]+)\)").astype(float).round(1)
ams["x_rd"] = coords[0]
ams["y_rd"] = coords[1]

# 4. De juiste kolommen selecteren
ams = ams[KOLOMMEN]

# 5. De kolommen overzetten naar een type dat missende waarden aankan
for kolom in ["maximum_snelheid", "wegvak_id", "junctie_id"]:
    ams[kolom] = ams[kolom].astype("Int64") #Integer die lege waarden toestaat

# 6. Opslaan.
ams.to_csv(OUTPUT_PATH, index=False)
print(f"Opgeslagen: {OUTPUT_PATH} ({len(ams)} rijen, {ams.shape[1]} kolommen)")
print(ams["verkeersongeval_afloop"].value_counts())
