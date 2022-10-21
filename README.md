# netflix-movie-recommendation

Project for building recommendation system on [netflix data](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data).

### Problem Statement:

Building recommendation system on Netflix data.

### Data:

Data has been taken from [Kaggle](https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data). It contains 4 files:

1. combined_data_<1-4>.txt
2. movie_titles.csv
3. probe.txt
4. qualifying.txt

Data will be available in the data folder in below format:
```bash
data
├── README              ---> Details about the data
├── combined_data_1.txt ---> Training data 1 (MovieId:\n,CustomerID,Rating,Date)
├── combined_data_2.txt ---> Training data 2 (MovieId:\n,CustomerID,Rating,Date)
├── combined_data_3.txt ---> Training data 3 (MovieId:\n,CustomerID,Rating,Date)
├── combined_data_4.txt ---> Training data 4 (MovieId:\n,CustomerID,Rating,Date)
├── movie_titles.csv    ---> Other Training  (MovieID,YearOfRelease,Title)
├── probe.txt           ---> Validation data
└── qualifying.txt      ---> Testing data
```

### Data Preprocessing:

Data preprocessing is done in the following steps:

1. Data is loaded and merged from combined_data_1.txt to combined_data_4.txt and movie_titles.csv using `ml.data.load_data()` function.

