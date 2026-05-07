# fall-2025-climate-and-road-maintenance
Team project: fall-2025-climate-and-road-maintenance


# Overview:

The goal of this project is to analyze the impact of weather events on future road work needed in New York City. Can we predict the amount of time/scale of road work needed based on weather data from the preceding year?

Weather-proofing roads and scheduling infrastructural maintenance are important factors in reducing future costs of repairs. We will quantify the amount of road work attributable to weather impact. Following this we will try to analyze actionable steps that the city can take to reduce future road work costs. Some possible avenues for this are the following:

* Does timely plowing after snowstorms reduce future road work?
* Does maintaining drainage impact necessary roadwork?


## The data:

Data is being taken from the following sources:

- NYC/NYS Data portals
	- [511 incidents](https://data.ny.gov/Transportation/511-NY-Events-Beginning-2010/ah74-pg4w/about_data)
	- [311 calls](https://data.cityofnewyork.us/Social-Services/DEP/gd7c-erma/explore/query/)
	- [Traffic volume counts](https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt/about_data)
- [Open-Meteo historical weather data](https://open-meteo.com/en/docs/historical-weather-api)

## Key Performance Indicators

- Prediction Error (e.g. RMSE) 


# Getting Started:

If you are using conda, in the terminal run

`conda env create -f environment.yml`

If you are using venv run

`pip install -r requirements.txt`.