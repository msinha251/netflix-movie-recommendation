import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def load_data(data_path, n_rows=100):
    '''
    This function loads the data from the file path then merge the combined_data_<> files with movie_titles and then returns a dataframe.

    Input:
        data_path: 
            path of the data folder containing the combined_data_<> files and movie_titles.csv
        n_rows: 
            number of rows to load from the combined_data_<> files, since the files are too large to load all at once.

    Returns:
        dataframes:
            combined_data: merged dataframe of all the combined_data_<> files with movie_titles
            movie_titles: movie_titles dataframe
    '''
    # load movie_titles:
    logging.info('Loading movie_titles...')
    movie_titles = pd.read_csv(f'{data_path}movie_titles.csv', encoding='ISO-8859-1', header=None, names=['MovieID','YearOfRelease','Title'], error_bad_lines=False, warn_bad_lines=False)
    
    # generate list of combined_data file paths:
    logging.info('Generating list of combined_data file paths...')
    combined_data_file_paths = [os.path.join(data_path, files) for files in os.listdir(data_path) if files.startswith('combined_data')]

    # Create movie_ratings dataframe:
    logging.info('Creating movie_ratings dataframe...')
    movie_ratings = pd.DataFrame(columns=['MovieID','CustID','Rating','Date'])

    # Load combined_data files and append to movie_ratings dataframe:
    for file in combined_data_file_paths:
        logging.info(f'Loading only {n_rows} rows from {file}')
        with open(combined_data_file_paths[0], 'r') as f:
            data = f.readlines()
            data = [i.strip() for i in data[:n_rows]]
        for line in data:
            if ':' in line:
                movie_id = line.replace(':', '')
            else:
                movie_ratings = movie_ratings.append({'MovieID': movie_id, 'CustID': line.split(',')[0], 'Rating': line.split(',')[1], 'Date': line.split(',')[2]}, ignore_index=True)

    # convert data types
    logging.info('Converting data types...')
    movie_ratings['MovieID'] = movie_ratings['MovieID'].astype(int)
    movie_ratings['CustID'] = movie_ratings['CustID'].astype(int)
    movie_ratings['Rating'] = movie_ratings['Rating'].astype(int)
    movie_ratings['Date'] = pd.to_datetime(movie_ratings['Date'])

    # merge movie_ratings with movie_titles:
    logging.info('Merging movie_ratings with movie_titles...')
    movie_ratings = pd.merge(movie_ratings, movie_titles, on='MovieID', how='left')

    logging.info('Done!')
    return (movie_ratings, movie_titles)

if __name__ == '__main__':
    data_path = '../data/'
    n_rows = 100
    load_data(data_path, n_rows)