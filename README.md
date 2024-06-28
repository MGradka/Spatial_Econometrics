# Spatial_Econometrics

## Configuration before running

Before running the scraping program, make sure to follow these steps:

1. Download the Firefox WebDriver (geckodriver) to your local machine. You can download it from [here](https://github.com/mozilla/geckodriver/releases).

2. Create a configuration file named `config.ini` in the project folder.

3. Inside the `config.ini` file, add the following lines:

```ini
[WebDriver]
geckodriver_path = /Path/to/geckodriver


## Description of the project

1. Webscrapping of data from OLX [code for webscrapping](scrapper_olx.py)
2. Cleaning and preparation of the data [code for preparation](Data_preparation.ipynb)
3. Manual adjustments of the [data](Data_cleaned.xlsx)
4. Analysis of the data [code for analysis](spatial_analysis.ipynb)