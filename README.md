# Custom Dataset Analyzer

This Python program helps you analyze any CSV dataset by:
- Detecting missing values
- Computing averages for numerical columns
- Displaying correlations between numerical columns
- Generating histograms, box plots, scatter plots, and heatmaps for data visualization

## Requirements:
- Python 3.x
- Pandas
- Matplotlib
- Seaborn

## Installation:
1. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn

---

### How to Use the Program:

1. **Choose Your CSV File**:
   - Place your dataset CSV file inside the `input_data/` folder. The CSV file should have columns with meaningful headers (e.g., age, height, weight, etc.).
   
2. **Run the Program**:
   - Run the program using `python analyzer.py` by navigating into the custom_dataset_analyzer folder and opening terminal.
   
3. **Input the File Path**:
   - When prompted, enter the full path to the CSV file (e.g., `input_data/my_dataset.csv`).
   
4. **View the Analysis**:
   - The program will display missing values, averages, and correlations in the terminal.
   
5. **Generate Plots**:
   - When prompted to generate visualizations, type "yes". The program will generate histograms, box plots, scatter plots, and a correlation heatmap.
   
6. **Check the Output Folder**:
   - After execution, the generated plots will be saved in the `output/` folder.

---

### Analysis Breakdown:
- **Histograms** will show the distribution of each numeric column, helping you understand how values are spread across the dataset.
- **Scatter plots** will show the relationship between pairs of numeric columns, helping to identify any correlations or trends.
- **Box plots** will help identify outliers and provide insight into the spread of the data in each column.
- **Heatmap** will show a visual representation of the correlations between numeric columns, making it easier to spot any strong relationships.


