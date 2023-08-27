# cas-data-exploration
Preliminary exploration of the public Crash Analysis System (CAS) data for New Zealand

The dataset is not included in this repository, but it is public and can be downloaded from [here](https://opendata-nzta.opendata.arcgis.com/datasets/crash-analysis-system-cas-data-1/explore?location=-20.304565%2C0.000000%2C2.92).

All the exploratory analysis is inside a Jupyter notebook [assignment.ipynb](./assignment.ipynb) with some custom Python functions stored in [cas_functions.py](./cas_functions.py). The analysis relies on Pandas and GeoPandas libraries, as well as other more standard packages (see [requirements.txt](./requirements.txt)).

The analysis also makes use of NZ population data from Stats NZ and a map of NZ regions, both of which are included in `.csv` and `.geojson` files, respectively. 