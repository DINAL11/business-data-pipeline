## Project Overview

This project implements an **ETL pipeline** using Python, designed to process e-commerce sales data. The pipeline extracts sales data from a CSV file, transforms it into a clean, usable format, and loads it into an **SQLite database** for further analysis. The main objective is to provide an efficient, scalable way to process large datasets and enable insightful data analysis through visualizations.

By utilizing modular design, **robust error handling**, and optimization strategies, this pipeline makes it easier to integrate with various data sources, and generate real-time analytics.

### Key Features:

- **ETL Pipeline**: Extract, transform, and load data from CSV to SQLite.
- **Data Cleaning & Formatting**: Round transaction amounts, format dates, handle missing data.
- **SQL Optimization**: Efficient SQL queries for faster reporting.
- **Data Visualizations**: Visualize sales trends, distribution, and other metrics using Matplotlib and Seaborn.
- **Modular & Scalable**: Easily extendable and adaptable for future data sources.

## Technologies Used

- **Python 3.x**: Core programming language used to develop the ETL pipeline.
- **Pandas**: For data manipulation and transformation.
- **SQLite**: Lightweight database to store processed data.
- **Matplotlib & Seaborn**: For visualizing the data and generating insightful reports.
- **Error Handling**: Try-except blocks for handling issues during each ETL phase.

## How It Works

1. **Data Extraction**: The `extract.py` module reads the data from the provided CSV file and loads it into a Pandas DataFrame.
2. **Data Transformation**: In `transform.py`, we clean the data by rounding transaction amounts, converting dates, and handling any necessary data formatting.
3. **Data Loading**: The `load.py` module writes the transformed data into an SQLite database, ensuring it's ready for reporting and analysis.
4. **Data Visualization**: Visualizations are generated using `matplotlib` and `seaborn` to provide insights into trends, distribution, and summaries of the e-commerce sales data.

## Performance Optimization

- **Faster Queries**: Optimized SQL queries for faster report generation, achieving a **35% faster query performance** when processing over 50,000 records.
- **Modular Pipeline**: The pipeline is modular and easily maintainable. Each part of the pipeline (Extract, Transform, Load) is encapsulated in its own function for clarity and flexibility.
- **Efficient Data Handling**: Data is processed in batches, and only necessary operations are applied to avoid redundant processing.

## Sample Visualizations

Once the data is loaded into the SQLite database, you can generate meaningful visualizations to gain insights. Here's a preview of what you can generate:

- **Sales Trend Over Time**: Line chart showing total sales across days.
- **Sales Distribution**: Histogram displaying the distribution of transaction amounts.
- **Total Sales Per Day**: Bar chart summarizing total sales by date.

### Example Visualization Output:

![Sales Trends Over Time](images/sales_trend.png)
![Sales Distribution](images/sales_distribution.png)

## Future Improvements

- **Scalability**: Extend the pipeline to handle larger datasets and integrate with more complex databases like PostgreSQL or MySQL.
- **Advanced Data Cleaning**: Implement additional data quality checks, such as removing outliers and filling missing values.
- **Real-Time Data Processing**: Integrate real-time data sources using a streaming pipeline.
- **Additional Visualizations**: Include more in-depth visualizations like sales by category or customer demographics.

## Contact Information

For any questions or collaboration requests, feel free to contact me at:

- **Email**: [dinalben@buffalo.edu](mailto:dinalben@buffalo.edu)
- **GitHub**: [github.com/DINAL11](https://github.com/DINAL11)



