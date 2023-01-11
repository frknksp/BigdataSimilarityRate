# CSV Cleaner and Similarity Rate Generator


This script is used for cleaning a CSV file, it reads a CSV file specified by the path in the pd.read_csv() function, filters out some rows by selecting certain columns, removes punctuation and stop words from certain columns. The user can also choose the number of threads for parallel processing, choose a specific column for which the similarity rate will be calculated, and set the desired similarity ratio for comparison.
## Input
- CSV file, you need to give the csv file path to the pd.read_csv function in cleardataframe.py
- The dataset I used: https://www.kaggle.com/datasets/selener/consumer-complaint-database


## Sample Output
![alt text](https://github.com/frknksp/BigdataSimilarityRate/blob/master/ui.png?raw=true)
