

import pandas as pd

INPUT_PATH = "ongevallen_2024.csv"
OUTPUT_PATH = "ongevallen_2024_amsterdam.csv"

# Op welke kolom en waarde we filteren.
FILTER_KOLOM = "gemeente"
FILTER_WAARDE = "Amsterdam"

# Kolommen die we houden.
KOLOMMEN = ["verkeersongeval_nummer", "jaar_ongeval", "verkeersongeval_afloop", "aantal_partijen",
            "partij_1_objecttype", "partij_1_objecttype_overig", "partij_2_objecttype",
            "partij_2_objecttype_overig", "maximum_snelheid", "wegvak_id", "junctie_id",
            "niveau_koppelen", "x_rd", "y_rd", "straatnaam", "woonplaats", "wegbeheerder",
            "bebouwde_kom", "wegsituatie", "weersgesteldheid", "wegdek", "lichtgesteldheid"]

# Kolommen met gehele getallen.
INT_KOLOMMEN = ["maximum_snelheid", "wegvak_id", "junctie_id"]

# Kolom waarvan we aan het eind de aantallen per waarde tonen.
TEL_KOLOM = "verkeersongeval_afloop"


# 1. Inlezen. low_memory=False voorkomt waarschuwingen over gemengde kolomtypes.
df = pd.read_csv(INPUT_PATH, low_memory=False)
print(f"Invoer: {len(df)} rijen, {df.shape[1]} kolommen")

# 2. Filteren. 
gefilterd = df[df[FILTER_KOLOM] == FILTER_WAARDE].copy()
print(f"Na filter {FILTER_KOLOM} = {FILTER_WAARDE}: {len(gefilterd)} rijen")

# 3. Coördinaten
if "shape" in gefilterd.columns:
    coords = gefilterd["shape"].str.extract(r"POINT \(([\d.]+) ([\d.]+)\)").astype(float).round(1)
    gefilterd["x_rd"] = coords[0]
    gefilterd["y_rd"] = coords[1]

# 4. Controleren of alle gewenste kolommen bestaan, zodat je een duidelijke foutmelding krijgt.
ontbrekend = [k for k in KOLOMMEN if k not in gefilterd.columns]
if ontbrekend:
    raise SystemExit(f"Deze kolommen staan niet in {INPUT_PATH}: {ontbrekend}")

gefilterd = gefilterd[KOLOMMEN]

# 5. Gehele getallen als Int64 opslaan (integer die lege waarden toestaat).
for kolom in INT_KOLOMMEN:
    gefilterd[kolom] = gefilterd[kolom].astype("Int64")

# 6. Opslaan.
gefilterd.to_csv(OUTPUT_PATH, index=False)
print(f"Opgeslagen: {OUTPUT_PATH} ({len(gefilterd)} rijen, {gefilterd.shape[1]} kolommen)")
print(gefilterd[TEL_KOLOM].value_counts())
