import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
# Load CSV data into a Pandas DataFrame
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print("Error: The file was not found.")
        exit()

# Analyze missing values, averages, and correlations
def analyze_data(df):
    # Missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    # Averages for numeric columns (filter only numeric columns)
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    print("\nAverages for numeric columns:")
    print(df[numeric_cols].mean())

    # Correlations
    print("\nCorrelation between numeric columns:")
    print(df[numeric_cols].corr())


def plot_histogram(df, column):
    # Sanitize the column name to make it a valid file name
    sanitized_column = column.replace("/", "_").replace(" ", "_").replace(":", "_")
    
    # Ensure the output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    # Plotting the histogram
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f"Histogram for {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    
    # Save the plot with the sanitized column name
    plt.savefig(f"output/{sanitized_column}_histogram.png")
    plt.show()

# Generate scatter plot between two columns
def plot_scatter(df, column_x, column_y):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=column_x, y=column_y)
    plt.title(f"Scatter Plot between {column_x} and {column_y}")
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.savefig(f"output/{column_x}_{column_y}_scatter.png")
    plt.show()

def plot_boxplot(df, column):
    # Sanitize the column name to make it a valid file name
    sanitized_column = column.replace("/", "_").replace(" ", "_").replace(":", "_")
    
    # Ensure the output directory exists
    if not os.path.exists('output'):
        os.makedirs('output')

    # Plotting the box plot
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot for {column}")
    plt.xlabel(column)
    
    # Save the plot with the sanitized column name
    plt.savefig(f"output/{sanitized_column}_boxplot.png")
    plt.show()

# Generate heatmap for correlation matrix

def plot_heatmap(df):
    # Filter out non-numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Calculate the correlation matrix for numeric columns only
    correlation_matrix = df[numeric_cols].corr()
    
    # Plotting the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()
