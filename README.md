# Data Pipeline Sales

This project demonstrates a simple ETL pipeline using Python and Pandas.

The pipeline extracts raw sales data from a CSV file, transforms and cleans the data, and loads the cleaned result into a new CSV file ready for analysis.

---

# Technologies Used

- Python
- Pandas

---

# ETL Process

## Extract
- Load raw sales data from CSV

## Transform
- Remove duplicate rows
- Drop rows with missing critical values
- Standardize product, category, and region text
- Convert columns to the correct data types
- Create a new revenue column

## Load
- Save cleaned data into a new CSV file

---

# Project Structure

```bash
data-pipeline-sales
│
├── data
│   └── raw_sales.csv
├── pipeline
│   └── etl_pipeline.py
├── output
│   └── clean_sales.csv
├── README.md
└── requirements.txt
---

# How to Run

```bash
python pipeline/etl_pipeline.py
## Author

Lucas Abreu Godoi  
Software Engineering Student  
GitHub: https://github.com/lucasagodoi
LinkedIn: https://linkedin.com/in/lucasgodoi
## Author

Lucas Abreu Godoi  
GitHub: https://github.com/lucasagodoi  
LinkedIn: https://www.linkedin.com/in/lucasgodoi/
