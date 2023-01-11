# CSV Cleaner and Similarity Rate Generator


This script is used for cleaning a CSV file, it reads a CSV file specified by the path in the pd.read_csv() function, filters out some rows by selecting certain columns, removes punctuation and stop words from certain columns, and lastly it adds an additional column containing similarity rate between elements of selected columns. The user can also choose the number of threads for parallel processing, choose a specific column for which the similarity rate will be calculated, and set the desired similarity ratio for comparison.
## Input
- CSV file, specified in the path in the pd.read_csv() function
## Output
- CSV file, containing cleaned columns and similarity rate column.
