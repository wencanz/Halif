import os

def rename(directory='./'):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        print(filename)
        if '.DS_Store' in filename:
            continue
        if filename.endswith('.PNG'):
            old_path = os.path.join(directory, filename)
            new_filename = filename[:-4] + '.png'
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
    return        

if __name__ == "__main__":
    # for folder in os.listdir('Configural'):
    #    rename('./Configural/'+folder)
    
    # print('Current path:', os.getcwd())
    # print(os.listdir('./Configural'))
    target_face = '158_03_01_051_14'
    for folder in os.listdir(f"./Configural/{target_face}"):
        if '.DS_Store' in folder: continue
        rename(f'./Configural/{target_face}/'+folder)