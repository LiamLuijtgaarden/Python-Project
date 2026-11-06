# Speed Limits and Road Safety: Assessing the Effects of Amsterdam's 30 km/h Policy

On 8 December 2023, Amsterdam lowered the speed limit from 50 km/h to 30 km/h on a large number of roads. This project investigates to what extent that change has been associated with changes in traffic safety, using all registered accidents from 2016 to 2025.

The report is in `Final report.ipynb`. It answers four subquestions:

1. Is there a greater effect on the roads that changed from 50 to 30 km/h than on the roads without a change?
2. Has the severity of the traffic accidents in Amsterdam changed?
3. How does a possible change compare to the nationwide trend?
4. How does the actual number of accidents compare to the trend predicted without the change?

## Running the pipeline

### Setup

The notebooks were run with Python 3.14. Install the packages with:

```
pip install pandas numpy matplotlib scipy statsmodels geopandas shapely pyproj jupyter
```

Run all notebooks from the project root.

### Reproducing the analysis

The processed data is included in `data/`, so the analysis notebooks can be run directly, in any order:

| Notebook | Subquestion | Figures saved to |
| -------- | ----------- | ---------------- |
| `Subquestion 1.ipynb` | Effect on the changed roads | `Visualisations and Graphs/RQ1/` |
| `Subquestion 2.ipynb` | Accident severity | `Visualisations and Graphs/RQ2/` |
| `Subquestion 3.ipynb` | Nationwide comparison | Shown in the notebook, not saved automatically. Exported figures are in `Visualisations and Graphs/RQ3/` |
| `Subquestion 4.ipynb` | Predicted trend | `Visualisations and Graphs/RQ4/` |

### Rebuilding the data from scratch

This is only needed to recreate the files in `data/`.

1. Download the BRON accident data (see Data sources) and place `ongevallen.txt` in the project root.
2. Run `data 2016-2025 filteren.ipynb`. It filters the data to 2016-2025 and writes `ongevallen_gefilterd_landelijk.csv` and `ongevallen_gefilterd_amsterdam.csv` to the project root. Move both files to `data/`.
3. Run `wegvakken.ipynb`. It links every accident to a road group and writes `data/crashes_amsterdam_classified.csv`. Missing NWB versions are downloaded automatically and then saved in `data/nwb_archive/`.

`data/amsterdam_dertig.json` (Amsterdam's 30 km/h map) and `data/bevolking_nederland_steden.csv` (population numbers) are available to download using the links below.

## Data sources

- [BRON](https://data.overheid.nl/dataset/9841-verkeersongevallen---bestand-geregistreerde-ongevallen-nederland): registered traffic accidents (Rijkswaterstaat)
- [NWB](https://data.overheid.nl/dataset/14767-nwb---wegen): national road network (Rijkswaterstaat)
- [30 km/u in de stad](https://maps.amsterdam.nl/30km/): road segments with their old and new speed limit (Gemeente Amsterdam)
- [Regionale kerncijfers Nederland](https://opendata.cbs.nl/#/CBS/nl/dataset/70072ned/table): population numbers (Statistics Netherlands)

## Authors

Project Group 18

- Jaden Accord
- Nienke van Slooten
- Jelle Kock
- Liam van de Luijtgaarden
