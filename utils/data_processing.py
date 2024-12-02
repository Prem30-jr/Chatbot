import pandas as pd

def load_and_preprocess_data(file_path):
    """
    Loads and preprocesses the dataset from the given file path.

    Steps:
    - Converts 'Date' column to datetime format.
    - Fills missing values with sensible defaults.
    - Strips whitespace and ensures consistent text formatting.
    - Adds derived columns such as 'Profit' if applicable.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Cleaned and preprocessed DataFrame.
    """
    
    data = pd.read_csv(file_path)

    
    if "Date" in data.columns:
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    
    
    data.fillna({
        "Sales": 0,               
        "Profit": 0,             
        "Discount": 0,            
        "Customer_Rating": data["Customer_Rating"].mean() if "Customer_Rating" in data.columns else 0
    }, inplace=True)

    
    data.dropna(subset=["Date"], inplace=True)

    
    if "Region" in data.columns:
        data["Region"] = data["Region"].str.strip().str.title()
    if "Product_Category" in data.columns:
        data["Product_Category"] = data["Product_Category"].str.strip().str.title()

    
    if "Sales" in data.columns and "Cost" in data.columns and "Profit" not in data.columns:
        data["Profit"] = data["Sales"] - data["Cost"]

    return data


def summarize_dataset(data):
    """
    Provides basic summary statistics and insights for the dataset.
    
    Args:
        data (pd.DataFrame): The preprocessed dataset.
    
    Returns:
        dict: A summary dictionary containing key statistics.
    """
    summary = {
        "Total Sales": data["Sales"].sum() if "Sales" in data.columns else None,
        "Average Sales": data["Sales"].mean() if "Sales" in data.columns else None,
        "Top Region": data.groupby("Region")["Sales"].sum().idxmax() if "Region" in data.columns else None,
        "Top Product": data.groupby("Product")["Sales"].sum().idxmax() if "Product" in data.columns else None
    }
    return summary



if __name__ == "__main__":
    file_path = "datasets/sales_data.csv"
    processed_data = load_and_preprocess_data(file_path)
    print("Data Preprocessing Complete!")
    print("Sample of Cleaned Data:")
    print(processed_data.head())

    
    summary = summarize_dataset(processed_data)
    print("\nDataset Summary:")
    print(summary)
