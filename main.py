import pandas as pd
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


# data sets:
def readData():
    climate_data = pd.read_csv("Data/Climate_data_by_census_tract.csv")
    print(climate_data.head())


def main():
    readData()




main()

