# Data Engineering | ETL Project: Medallion Architecture with SSIS and Python (SAAQIS Data)

## Project Overview
This project demonstrates an ETL pipeline using SSIS and Python, leveraging data from the **South African Air Quality Information System (SAAQIS)**. The pipeline follows the **Medallion Architecture** to process and refine data, ultimately loading it into a data warehouse for analytics purposes.

---

## Architecture Workflow
![image](https://github.com/user-attachments/assets/c518d358-6676-4bae-b19e-a547f65de0f1)

1. **Data Extraction**:
   - Python script fetches air quality data from the SAAQIS API and saves it as raw JSON in the staging area.
   
2. **Bronze Layer**:
   - Raw JSON is flattened and loaded into a csv file.

3. **Silver Layer**:
   - Irrelevant columns are removed.
   - Data transformations are applied, including dropping columns, handling null values, extracting station names and locations from station_names column.

4. **Gold Layer**:
   - Data is further refined, structured, and loaded into a data warehouse, ready for analytics.

---

## Tools and Technologies
- **ETL Tool**: SSIS
- **Scripting Language**: Python
- **Database**: MSSQL
- **Data Source**: SAAQIS API
- **Architecture**: Medallion (Bronze, Silver, Gold)

---

## Project Workflow

### 1. Data Extraction
- **Data Source**: [SAAQIS API](https://saaqis.environment.gov.za/)
- **Python Script**: `python_scripts/api_data_extraction.py`
  - Fetches air quality data from SAAQIS.
  - Saves the raw data as JSON in the staging area.

### 2. Data Transformation and Loading
- **SSIS ELT control flow**:
- ![image](https://github.com/user-attachments/assets/3d782cc1-8cd0-460b-95f1-8b8d5e10be20)



### 3. Data Storage
- **Database**: MSSQL
  - **Staging Table**: Holds raw JSON data.
  - **Bronze Table**: Flattened raw data.
  - **Silver Table**: Cleaned and transformed data.
  - **Gold Table**: Final refined dataset ready for analytics.

---

## How to Run the Project

### Prerequisites
1. Python installed with libraries (`requests`, `pandas`, `aiohttp`,`reques`, `asyncio`, `aiohttp`, `json`,`csv`).
2. SSIS installed and configured.
3. MSSQL database,
4. Access to the [SAAQIS API](https://saaqis.environment.gov.za/).

