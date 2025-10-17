# Part 2 of dugga -- Data handling and plotting
# Use provided dugga env to run this script
# Import necessary libraries:
import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Avoid hard coding paths by letting the user define the path to the input file
input_file = sys.argv[1] # should be 'brca_head500_genes.csv'

# Task 2.1 Read the file brca_head500_genes.csv into a dataframe using pandas, using ',' as separator
df = pd.read_csv(input_file, sep=',')
print(df.head()) # print the first few rows to verify

# Task 2.2 Create a function that plots a histogram of the column fpkm_log2 from the dataframe you created from the csv file
# task 2.2.1 Define the function
def plot_histogram(df):
    plt.hist(df['fpkm_log2'], bins=30, color='magenta', edgecolor='white', alpha=0.7)
    plt.xlabel('Expression')
    plt.ylabel('Number of genes')
    plt.title('Distribution of gene expression')
    plt.savefig('fpkm_distribution.png')
    plt.close()
# Task 2.2.2 call the function to create and save the histogram
plot_histogram(df)




