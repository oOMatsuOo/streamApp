def list_movies(path):
    all_movies = []
    for (repertoire, sous_repertoires, fichiers) in os.walk(path):
        for files in fichiers:
            all_movies.append(files)

    return all_movies


def list_series(path):
    all_series = []
    for serie in os.listdir(path):
        all_series.append(serie)
    
    return all_series
