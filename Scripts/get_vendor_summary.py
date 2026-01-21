import pandas as pd
import numpy as np
from sqlalchemy import create_engine


# DATABASE CONNECTION (MySQL)

engine = create_engine(
    "mysql+mysqlconnector://root:Shubham%40123@localhost:3306/inventory"
)

# INGEST DATAFRAME INTO MYSQL
def ingest_db(df, table_name, engine):
    """
    Ingest dataframe into MySQL table
    """
    df.to_sql(
        table_name,
        con=engine,
        if_exists='replace',
        index=False,
        chunksize=5000
    )

# CREATE VENDOR SUMMARY
def create_vendor_summary(engine):
    """
    Merge purchase, sales, and freight data
    to create vendor-level summary
    """
    query = """
    WITH FreightSummary AS (
        SELECT
            VendorNumber,
            SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),

    PurchaseSummary AS (
        SELECT
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price AS ActualPrice,
            pp.Volume,
            SUM(p.Quantity) AS TotalPurchaseQuantity,
            SUM(p.Dollars) AS TotalPurchaseDollars
        FROM purchases p
        JOIN purchase_prices pp
            ON p.Brand = pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY
            p.VendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price,
            pp.Volume
    ),

    SalesSummary AS (
        SELECT
            VendorNo,
            Brand,
            SUM(SalesQuantity) AS TotalSalesQuantity,
            SUM(SalesDollars) AS TotalSalesDollars,
            SUM(SalesPrice) AS TotalSalesPrice,
            SUM(ExciseTax) AS TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
        AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalPurchaseDollars DESC
    """

    return pd.read_sql_query(query, engine)

# CLEAN & FEATURE ENGINEERING
def clean_data(df):
    """
    Clean data and create analytical metrics
    """

    # Type fixes
    df['Volume'] = df['Volume'].astype(float)

    # Handle missing values
    df.fillna(0, inplace=True)

    # Clean text
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # Metrics
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']

    df['ProfitMargin'] = np.where(
        df['TotalSalesDollars'] > 0,
        (df['GrossProfit'] / df['TotalSalesDollars']) * 100,
        0
    )

    df['StockTurnover'] = np.where(
        df['TotalPurchaseQuantity'] > 0,
        df['TotalSalesQuantity'] / df['TotalPurchaseQuantity'],
        0
    )

    df['SalesToPurchaseRatio'] = np.where(
        df['TotalPurchaseDollars'] > 0,
        df['TotalSalesDollars'] / df['TotalPurchaseDollars'],
        0
    )

    return df

# MAIN EXECUTION
if __name__ == "__main__":
    summary_df = create_vendor_summary(engine)
    clean_df = clean_data(summary_df)
    ingest_db(clean_df, "vendor_sales_summary", engine)
