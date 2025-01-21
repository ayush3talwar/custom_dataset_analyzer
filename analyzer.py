import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, analyze_data, plot_histogram, plot_scatter, plot_boxplot, plot_heatmap

def main():
    # Ask for file path
    file_path = input("Enter the path of the CSV file (e.g., 'input_data/my_dataset.csv'): ")

    # Load the dataset
    df = load_data(file_path)

    # Analyze the dataset
    analyze_data(df)

    # Ask if the user wants to generate visualizations
    plot_choice = input("Do you want to generate histograms, box plots, scatter plots, and heatmaps? (yes/no): ")
    if plot_choice.lower() == 'yes':
        generate_plots(df)

def generate_plots(df):
    # Generate histogram for all numerical columns
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        plot_histogram(df, column)

    # Generate scatter plots (for first two numeric columns)
    if len(df.select_dtypes(include=['float64', 'int64']).columns) >= 2:
        plot_scatter(df, df.select_dtypes(include=['float64', 'int64']).columns[0], df.select_dtypes(include=['float64', 'int64']).columns[1])

    # Generate box plots for all numerical columns
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        plot_boxplot(df, column)

    # Generate heatmap for correlation matrix
    plot_heatmap(df)

if __name__ == '__main__':
    main()
