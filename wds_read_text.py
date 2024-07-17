import pandas as pd
import os
# Chemin du fichier texte


directory_path = 'data/'



fields_positions = [17,19, 26, 33, 35, 44, 46, 53, 55, 61, 62, 67, 69, 75, 76, 81, 90, 91, 97, 98, 101, 110, 113, 116, 117]
fields_format = ['f','a','f','f','a','f','a','f','a','f','a', 'f','a','f','a','f','a','a','f','a','f','a','a','a','a']
fields_names = [ 'date', 'tflag', 'theta', 'terr', 'rflag', 'rho', 'reflag', 'rerr', 'mflag1', 'mag1', 'm1eflag', 'm1err', 'mflag2', 'mag2', 'm2eflag', 'm2err','filter', 'fflag', 'tel', 'teflag','nn','ref','tech','codes', 'de']
 
# Read one block of measures
def wds_read_one_block(data_lines):
    first_row = data_lines[0].strip().split(maxsplit=2)[:2]  # Keep only two first columns
    remaining_data = []
    i=0
    # Browse line until empty lines (except for space)
    for line in data_lines[1:]:
        i+=1
        if len(line.strip())==0:
            break # Get out if empty line

        last_position=7 # fist position
        current_line=[]

        # Check each columns to find data
        for index, pos in enumerate(fields_positions):
            value=line[last_position-1:pos].strip()
            last_position=pos+1
            # Convert to float if needed
            if fields_names[index]=='mag1' or fields_names[index]=='mag2' :
                    print(value)
            if fields_format[index]=='f':
                value=float(value) if value!='.' and len(value)>0 else 0.0

            current_line.append(value)
        
        remaining_data.append(current_line)
    
    # Create dataframe
    data_df = pd.DataFrame(remaining_data, columns=fields_names)
    name=''.join(first_row)
    return name, data_df,i


# Read on txt file
def wds_read_one_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    # find line index of "MEASURES:"
    start_index = None
    for i, line in enumerate(lines):
        if line.strip() == 'MEASURES:':
            start_index = i + 2
            break

    # No Measures found
    if start_index is None:
        raise ValueError("La ligne 'MEASURES:' n'a pas été trouvée dans le fichier.")

    # Get lines after "MEASURES:"
    data_lines = lines[start_index:]
    results={}

    # Process Data until delimiter
    while data_lines[0][0:5]!='-----':
        name, data, i = wds_read_one_block(data_lines)
        data_lines=data_lines[i+1:]
        results[name]=data
    return results
 

def wds_read_files(directory_path):   
    results={}
    wds_indexes={}
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            print(f"Reading {directory_path+'/'+filename}")
            data = wds_read_one_file(directory_path+'/'+filename)
            results.update(data)
            wds_index=filename.split('.')[0]
            for k in data.keys():
                wds_indexes[k]=wds_index
    return results,wds_indexes




