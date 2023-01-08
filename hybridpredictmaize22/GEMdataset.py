# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_gemDataset.ipynb.

# %% auto 0
__all__ = ['collect_snps', 'WT', 'YT', 'ST', 'GEM', 'GemDataset']

# %% ../nbs/02_gemDataset.ipynb 3
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

from sklearn.preprocessing import StandardScaler
from pathlib import Path


# %% ../nbs/02_gemDataset.ipynb 4
def collect_snps(method):
    """
    Input
        method: a Path(PosixPath) to directory containing npy arrays for each chr
    Output
        tuple(hybrid ids, snp matrix)
    """
    for c,chr in enumerate(method.iterdir()):
        if c == 0:
            strains,snp_data = np.load(chr,allow_pickle=True)
        else:
            strains, snps = np.load(chr, allow_pickle=True)
            snp_data = np.vstack((snp_data,snps))

    return strains,snp_data

# %% ../nbs/02_gemDataset.ipynb 5
class WT():
    """
    A class which will hold the weather data for the entire dataset for training purposes
    
    init
        weather_data -> pandas table
        testYear -> e.g. 2019. this will set all data from a given year as the Test Set
    """
    def __init__(self, weather_data, testYear):
        
        self.Te = weather_data.iloc[([str(testYear) in x for x in weather_data['Year']]),:].reset_index()
        self.Tr = weather_data.iloc[([str(testYear) not in x for x in weather_data['Year']]),:].reset_index()
            
        self.setup_scaler()
        self.scale_data(self.Tr)
        self.scale_data(self.Te)
            
    def setup_scaler(self):
        ss = StandardScaler()
        ss.fit(self.Tr.select_dtypes('float'))
        self.scaler = ss
            
    def scale_data(self, df):
        fd = df.select_dtypes('float')
        fs = self.scaler.transform(fd)
        df[fd.columns] = fs

# %% ../nbs/02_gemDataset.ipynb 6
class YT():
    """
    A class which will hold the yield data for the entire dataset for training purposes
    
    init
        yield_data -> pandas table
        testYear -> e.g. 2019. this will set all data from a given year as the Test Set
    """
    def __init__(self, yield_data, testYear):

        self.Te = yield_data.iloc[([str(testYear) in x for x in yield_data['Env']]),:].reset_index()
        self.Tr = yield_data.iloc[([str(testYear) not in x for x in yield_data['Env']]),:].reset_index()

        self.setup_scaler()
        self.scale_data(self.Tr)
        self.scale_data(self.Te)

    def setup_scaler(self):
        ss = StandardScaler()
        ss.fit(np.array(self.Tr['Yield_Mg_ha']).reshape(-1,1))
        self.scaler = ss

    def scale_data(self,df):
        ya = np.array(df['Yield_Mg_ha']).reshape(-1,1)
        ys = self.scaler.transform(ya)
        df['scaled_yield'] = ys

    def plot_yields(self):

        plt.hist(self.Tr['scaled_yield'],density=True, label='Train',alpha=.5,bins=50)
        plt.hist(self.Te['scaled_yield'],density=True, label='Test',alpha=.5,bins=50)
        plt.legend()
        plt.show()

# %% ../nbs/02_gemDataset.ipynb 7
class ST():
    """
    A class which will hold the secondary trait data for the entire dataset for pre-training purposes
    
    init
        yield_data -> pandas table
        testYear -> e.g. 2019. this will set all data from a given year as the Test Set
    """
    def __init__(self, yield_data, testYear):

        self.Te = yield_data.iloc[([str(testYear) in x for x in yield_data['Env']]),:].reset_index()
        self.Tr = yield_data.iloc[([str(testYear) not in x for x in yield_data['Env']]),:].reset_index()

        self.secondary_traits = [
                'Stand_Count_plants',
                'Pollen_DAP_days',
                'Silk_DAP_days',
                'Plant_Height_cm',
                'Ear_Height_cm',
                #'Root_Lodging_plants',
                #'Stalk_Lodging_plants',
                'Twt_kg_m3',
                'Yield_Mg_ha',
                #'Date_Harvested'
                ]
        
        self.setup_scaler()
        self.scale_data(self.Tr)
        self.scale_data(self.Te)

    def setup_scaler(self):
        ss = StandardScaler()
        ss.fit(np.array(self.Tr[self.secondary_traits]))
        self.scaler = ss

    def scale_data(self,df):
        scaled_secondary = self.scaler.transform(np.array(df[self.secondary_traits]))
        for c,i in enumerate(self.secondary_traits):
            #print(i)
            df[i] = scaled_secondary[:,c]
    
    def plot_yields(self):
        for i in self.secondary_traits:
            plt.hist(self.Tr[i],density=True, label='Train',alpha=.5,bins=50)
            plt.hist(self.Te[i],density=True, label='Test',alpha=.5,bins=50)
            plt.legend()
            plt.title(i)
            plt.show()

# %% ../nbs/02_gemDataset.ipynb 8
class GEM():
    """
    init
        split -> the year that will be designated as the test split
    """
    def __init__(self, split):
        self.split = str(split)
        self.Y = None
        self.W = None
        self.SNP = None

# %% ../nbs/02_gemDataset.ipynb 9
class GemDataset():
    """
    Pytorch Dataset which can be used with dataloaders for simple batching during training loops
    """
    def __init__(self,W,Y,G, def_device='cpu'):
        self.W = W
        self.SNP = G
        self.Y = Y
        self.device = def_device
        
    def __len__(self): return self.Y.shape[0]

    def __getitem__(self,idx):
        #keys to access SNPs and Weather
        hybrid = self.Y.iloc[idx,:]['Hybrid']
        env = self.Y.iloc[idx,:]['Env']

        #values for the model training
        target = self.Y.iloc[idx,:]['scaled_yield']
        genotype = self.SNP[1][:, np.where(self.SNP[0]==hybrid)[0][0]]
        weather = np.array(self.W.loc[self.W['Env'] == env].select_dtypes('float'))
        #convert to tensors
        target = torch.tensor(target, dtype=torch.float32)
        genotype = torch.tensor(genotype, dtype=torch.float32)
        weather = torch.tensor(weather,dtype=torch.float32)

        return target.to(self.device), genotype.to(self.device), weather.to(self.device)
