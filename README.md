# Housing Affordability Analysis – Maricopa County (2020–2024)

Final Capstone Project for Data Analytics Course
## Overview

This project analyzes housing affordability across ZIP codes in Maricopa County, Arizona by examining the relationship between median household income and median home value.

The goal of this analysis is to determine:

- Whether higher income leads to higher home values
- How affordability varies across different geographic areas
- Which ZIP codes show the greatest affordability challenges

The project combines data analysis, visualization, and dashboard design to provide insights that can support decision-making for policymakers, businesses, and communities.

## Technologies Used
- Python (pandas, matplotlib) – Data cleaning and analysis  
- Microsoft Power BI – Interactive dashboard  
- PolicyMap / U.S. Census ACS Data – Data source  
- GitHub – Version control  

## How to Reproduce the Analysis
1. Download the Data

Use the dataset provided in the /data folder:

maricopa_housing_data_raw.csv
2. Run the Python Script

Navigate to the /python folder and run:

python capstone_data_cleaning_modeling.py

This script will:

Clean and format the dataset
Handle missing values
Create a price-to-income ratio
Export a cleaned dataset
Generate supporting visualizations

Output files will include:

maricopa_housing_data_cleaned.csv
Python-generated charts (PNG files)
3. Open the Power BI Dashboard
Open the file in /powerbi:
DariusJohnson_Final_Capstone_PowerBI.pbix
Click Refresh to load the dataset
Interact with the dashboard:
Use slicers to filter by ZIP code
Hover over visuals for detailed tooltips
Observe cross-filtering between visuals
4. Review the Final Report

See the /report folder for the full written analysis:

Housing_Affordability_Report.docx

This document includes:

Hypotheses and statistical reasoning
Data analysis and visual interpretation
Dashboard explanation
Real-world implications

## File Structure

DariusJohnson-Capstone/

├── data/
│   ├── maricopa_housing_data_raw.csv
│   └── maricopa_housing_data_cleaned.csv
│
├── python/
│   └── capstone_data_cleaning_modeling.py
│
├── powerbi/
│   └── DariusJohnson_Final_Capstone_PowerBI.pbix
│
├── images/
│   ├── scatter_plot.png
│   ├── bar_chart.png
│   ├── map.png
│   └── dashboard.png
│
├── report/
│   └── Housing_Affordability_Report.docx
│
└── README.md

## Key Findings
There is a strong positive relationship between income and home value
Housing prices vary significantly across ZIP codes
Higher-income areas tend to have lower affordability (higher price-to-income ratios)
Geographic location plays a major role in housing costs
Conclusion

This project demonstrates how data analytics and visualization tools can be used to better understand housing affordability challenges. The findings highlight the importance of considering both income and location when evaluating housing markets.

Future improvements could include adding additional variables such as:

Employment rates
Population growth
Housing supply

to create a more advanced predictive model.
