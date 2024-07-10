import pandas as pd


def gaia_read_excel_file(file_path):
    df = pd.read_excel(file_path)
    # Supprimer les lignes complètement vides
    df.dropna(how='all', inplace=True)


    # Supprimer les espaces dans les textes de la colonne 'Name'
    df['Name'] = df['Name'].str.replace(r'\s+', '', regex=True)

    # Remplir les champs vides dans la colonne 'Name' avec la valeur de la ligne précédente
    df['Name'] = df['Name'].ffill()

    # Définir les colonnes à vérifier pour les valeurs non-nulles
    columns_to_check = df.columns.difference(['Name', '#source_id'])

    # Supprimer les lignes où seules les colonnes 'Name' et '#source_id' sont remplies
    df = df[~df[columns_to_check].isnull().all(axis=1)]
    return df