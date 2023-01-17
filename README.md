hybridpredictmaize22
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

Repo for analysis of GEM prediction for maize yield

## How to use

A demo of the library specifically for this dataset

``` python
Yield, Genotype, Weather = prep_gem_data(trait_csv='./data/Training_Data/1_Training_Trait_Data_2014_2021.csv',
                weather_csv = './data/Training_Data/4_Training_Weather_Data_2014_2021.csv',
                snp_folder = './data/snpCompress/PCS_10/'
               )
```

    136012 plots with 26 features
    77431 daily weather measurements with 18 features
    4928 hybrids

``` python
Yield
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Env</th>
      <th>Year</th>
      <th>Field_Location</th>
      <th>Experiment</th>
      <th>Replicate</th>
      <th>Block</th>
      <th>Plot</th>
      <th>Range</th>
      <th>Pass</th>
      <th>...</th>
      <th>Stand_Count_plants</th>
      <th>Pollen_DAP_days</th>
      <th>Silk_DAP_days</th>
      <th>Plant_Height_cm</th>
      <th>Ear_Height_cm</th>
      <th>Root_Lodging_plants</th>
      <th>Stalk_Lodging_plants</th>
      <th>Yield_Mg_ha</th>
      <th>Grain_Moisture</th>
      <th>Twt_kg_m3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>DEH1_2014</td>
      <td>2014</td>
      <td>DEH1</td>
      <td>G2F_2014_15</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>56.0</td>
      <td>63.0</td>
      <td>67.0</td>
      <td>213.00</td>
      <td>79.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.721725</td>
      <td>20.8</td>
      <td>706.664693</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>DEH1_2014</td>
      <td>2014</td>
      <td>DEH1</td>
      <td>G2F_2014_15</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>...</td>
      <td>54.0</td>
      <td>61.0</td>
      <td>63.0</td>
      <td>286.00</td>
      <td>172.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>11.338246</td>
      <td>25.8</td>
      <td>693.792841</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>DEH1_2014</td>
      <td>2014</td>
      <td>DEH1</td>
      <td>G2F_2014_15</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>...</td>
      <td>60.0</td>
      <td>63.0</td>
      <td>65.0</td>
      <td>239.00</td>
      <td>92.00</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>6.540810</td>
      <td>20.8</td>
      <td>698.941582</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>DEH1_2014</td>
      <td>2014</td>
      <td>DEH1</td>
      <td>G2F_2014_15</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>...</td>
      <td>59.0</td>
      <td>61.0</td>
      <td>63.0</td>
      <td>242.00</td>
      <td>118.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.366857</td>
      <td>23.7</td>
      <td>711.813434</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>DEH1_2014</td>
      <td>2014</td>
      <td>DEH1</td>
      <td>G2F_2014_15</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>...</td>
      <td>58.0</td>
      <td>63.0</td>
      <td>65.0</td>
      <td>211.00</td>
      <td>92.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>10.908814</td>
      <td>19.4</td>
      <td>743.993065</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>129303</th>
      <td>136007</td>
      <td>WIH3_2021</td>
      <td>2021</td>
      <td>WIH3</td>
      <td>G2F_2020_21_PHP02</td>
      <td>2</td>
      <td>25</td>
      <td>496</td>
      <td>19.0</td>
      <td>9.0</td>
      <td>...</td>
      <td>80.0</td>
      <td>75.0</td>
      <td>76.0</td>
      <td>251.67</td>
      <td>123.33</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.972527</td>
      <td>16.9</td>
      <td>698.941582</td>
    </tr>
    <tr>
      <th>129304</th>
      <td>136008</td>
      <td>WIH3_2021</td>
      <td>2021</td>
      <td>WIH3</td>
      <td>G2F_2020_21_PHP02</td>
      <td>2</td>
      <td>25</td>
      <td>497</td>
      <td>19.0</td>
      <td>8.0</td>
      <td>...</td>
      <td>65.0</td>
      <td>81.0</td>
      <td>90.0</td>
      <td>303.33</td>
      <td>148.33</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>9.160941</td>
      <td>23.7</td>
      <td>709.239064</td>
    </tr>
    <tr>
      <th>129305</th>
      <td>136009</td>
      <td>WIH3_2021</td>
      <td>2021</td>
      <td>WIH3</td>
      <td>G2F_2020_21_PHP02</td>
      <td>2</td>
      <td>25</td>
      <td>498</td>
      <td>19.0</td>
      <td>7.0</td>
      <td>...</td>
      <td>69.0</td>
      <td>76.0</td>
      <td>79.0</td>
      <td>301.67</td>
      <td>150.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.256348</td>
      <td>19.5</td>
      <td>732.408398</td>
    </tr>
    <tr>
      <th>129306</th>
      <td>136010</td>
      <td>WIH3_2021</td>
      <td>2021</td>
      <td>WIH3</td>
      <td>G2F_2020_21_PHP02</td>
      <td>2</td>
      <td>25</td>
      <td>499</td>
      <td>19.0</td>
      <td>6.0</td>
      <td>...</td>
      <td>81.0</td>
      <td>78.0</td>
      <td>79.0</td>
      <td>293.33</td>
      <td>165.00</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>11.504058</td>
      <td>19.1</td>
      <td>692.505656</td>
    </tr>
    <tr>
      <th>129307</th>
      <td>136011</td>
      <td>WIH3_2021</td>
      <td>2021</td>
      <td>WIH3</td>
      <td>G2F_2020_21_PHP02</td>
      <td>2</td>
      <td>25</td>
      <td>500</td>
      <td>19.0</td>
      <td>5.0</td>
      <td>...</td>
      <td>81.0</td>
      <td>76.0</td>
      <td>77.0</td>
      <td>291.67</td>
      <td>165.00</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>11.618923</td>
      <td>19.5</td>
      <td>696.367212</td>
    </tr>
  </tbody>
</table>
<p>129308 rows × 27 columns</p>
</div>

``` python
Genotype
```

    (array(['2369/DK3IIH6', '2369/PHN82', '2369/PHZ51', ...,
            'Z038E0057/DK3IIH6', 'Z038E0057/LH162', 'Z038E0057/PHZ51'],
           dtype=object),
     array([[-0.00898487, -0.00889737, -0.00985531, ..., -0.00912366,
             -0.00703719, -0.00999637],
            [ 0.00958669,  0.01123948, -0.02311905, ...,  0.00941995,
             -0.00142499, -0.02322749],
            [ 0.01249667,  0.00819269, -0.0079599 , ...,  0.01258645,
              0.00026784, -0.00785536],
            ...,
            [-0.01473902, -0.0097304 , -0.00344457, ..., -0.01584803,
             -0.00909118, -0.00434402],
            [ 0.00850316,  0.0033058 ,  0.00246347, ...,  0.00928889,
             -0.00240442,  0.00304883],
            [-0.00583694, -0.00337831, -0.00102845, ..., -0.00549591,
             -0.00374846, -0.000797  ]]))

``` python
Weather
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Env</th>
      <th>Date</th>
      <th>QV2M</th>
      <th>T2MDEW</th>
      <th>PS</th>
      <th>RH2M</th>
      <th>WS2M</th>
      <th>GWETTOP</th>
      <th>ALLSKY_SFC_SW_DWN</th>
      <th>ALLSKY_SFC_PAR_TOT</th>
      <th>T2M_MAX</th>
      <th>T2M_MIN</th>
      <th>T2MWET</th>
      <th>GWETROOT</th>
      <th>T2M</th>
      <th>GWETPROF</th>
      <th>ALLSKY_SFC_SW_DNI</th>
      <th>PRECTOTCORR</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>ARH1_2016</td>
      <td>20160101</td>
      <td>3.54</td>
      <td>-0.78</td>
      <td>102.34</td>
      <td>77.00</td>
      <td>2.15</td>
      <td>0.84</td>
      <td>8.21</td>
      <td>41.96</td>
      <td>7.80</td>
      <td>-0.70</td>
      <td>1.15</td>
      <td>0.83</td>
      <td>3.08</td>
      <td>0.80</td>
      <td>5.96</td>
      <td>0.00</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>ARH1_2016</td>
      <td>20160102</td>
      <td>3.23</td>
      <td>-1.91</td>
      <td>102.04</td>
      <td>74.62</td>
      <td>1.49</td>
      <td>0.84</td>
      <td>11.28</td>
      <td>55.13</td>
      <td>10.15</td>
      <td>-3.10</td>
      <td>0.42</td>
      <td>0.83</td>
      <td>2.74</td>
      <td>0.80</td>
      <td>16.13</td>
      <td>0.00</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>ARH1_2016</td>
      <td>20160103</td>
      <td>4.09</td>
      <td>1.05</td>
      <td>101.59</td>
      <td>80.69</td>
      <td>1.95</td>
      <td>0.84</td>
      <td>9.78</td>
      <td>49.21</td>
      <td>12.39</td>
      <td>-1.29</td>
      <td>2.72</td>
      <td>0.83</td>
      <td>4.38</td>
      <td>0.80</td>
      <td>18.36</td>
      <td>0.00</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>ARH1_2016</td>
      <td>20160104</td>
      <td>2.87</td>
      <td>-3.49</td>
      <td>102.24</td>
      <td>79.88</td>
      <td>3.45</td>
      <td>0.84</td>
      <td>7.35</td>
      <td>35.66</td>
      <td>4.56</td>
      <td>-4.00</td>
      <td>-1.79</td>
      <td>0.83</td>
      <td>-0.09</td>
      <td>0.80</td>
      <td>10.87</td>
      <td>0.00</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>ARH1_2016</td>
      <td>20160105</td>
      <td>2.81</td>
      <td>-3.64</td>
      <td>102.37</td>
      <td>78.81</td>
      <td>1.95</td>
      <td>0.84</td>
      <td>13.00</td>
      <td>62.04</td>
      <td>6.94</td>
      <td>-4.59</td>
      <td>-1.74</td>
      <td>0.82</td>
      <td>0.16</td>
      <td>0.80</td>
      <td>27.02</td>
      <td>0.00</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>63595</th>
      <td>77361</td>
      <td>TXH4_2019</td>
      <td>20191023</td>
      <td>4.03</td>
      <td>-0.77</td>
      <td>90.26</td>
      <td>34.19</td>
      <td>2.94</td>
      <td>0.33</td>
      <td>18.76</td>
      <td>94.70</td>
      <td>26.10</td>
      <td>7.84</td>
      <td>7.62</td>
      <td>0.35</td>
      <td>16.00</td>
      <td>0.38</td>
      <td>33.63</td>
      <td>0.00</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>63596</th>
      <td>77362</td>
      <td>TXH4_2019</td>
      <td>20191024</td>
      <td>4.09</td>
      <td>-0.46</td>
      <td>90.98</td>
      <td>64.88</td>
      <td>6.20</td>
      <td>0.34</td>
      <td>3.61</td>
      <td>20.41</td>
      <td>11.37</td>
      <td>0.13</td>
      <td>2.63</td>
      <td>0.35</td>
      <td>5.73</td>
      <td>0.38</td>
      <td>2.57</td>
      <td>0.30</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>63597</th>
      <td>77363</td>
      <td>TXH4_2019</td>
      <td>20191025</td>
      <td>2.56</td>
      <td>-6.35</td>
      <td>91.14</td>
      <td>46.31</td>
      <td>3.95</td>
      <td>0.34</td>
      <td>19.07</td>
      <td>93.01</td>
      <td>13.57</td>
      <td>-0.67</td>
      <td>-0.52</td>
      <td>0.36</td>
      <td>5.31</td>
      <td>0.38</td>
      <td>35.17</td>
      <td>0.00</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>63598</th>
      <td>77364</td>
      <td>TXH4_2019</td>
      <td>20191026</td>
      <td>2.81</td>
      <td>-5.44</td>
      <td>90.00</td>
      <td>33.81</td>
      <td>3.30</td>
      <td>0.34</td>
      <td>18.52</td>
      <td>91.70</td>
      <td>24.73</td>
      <td>0.55</td>
      <td>3.09</td>
      <td>0.35</td>
      <td>11.62</td>
      <td>0.38</td>
      <td>34.00</td>
      <td>0.25</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>63599</th>
      <td>77365</td>
      <td>TXH4_2019</td>
      <td>20191027</td>
      <td>4.09</td>
      <td>-0.48</td>
      <td>90.14</td>
      <td>49.19</td>
      <td>3.41</td>
      <td>0.34</td>
      <td>18.39</td>
      <td>91.51</td>
      <td>17.08</td>
      <td>3.90</td>
      <td>4.76</td>
      <td>0.35</td>
      <td>9.99</td>
      <td>0.38</td>
      <td>34.26</td>
      <td>0.00</td>
      <td>2019</td>
    </tr>
  </tbody>
</table>
<p>63600 rows × 20 columns</p>
</div>

``` python
#Create a GEM dataset
test_split = 2019
gem = GemDataset(
W=WT(Weather,testYear=test_split),
Y=YT(Yield,testYear=test_split),
G=Genotype,)
```

``` python
gem.Y.plot_yields()
```

![](index_files/figure-commonmark/cell-7-output-1.png)

``` python
#example of how to unscale a value
gem.Y.scaler.inverse_transform(np.array(1.4).reshape(-1,1))
```

    array([[13.27959341]])

``` python
tr_ds = GemDataset(gem.W.Tr, gem.Y.Tr, gem.SNP)
te_ds = GemDataset(gem.W.Te, gem.Y.Te, gem.SNP)

tr_dl = DataLoader(tr_ds, batch_size=4)
te_dl = DataLoader(te_ds, batch_size=4)
dls = DataLoaders(tr_dl,te_dl)
```
