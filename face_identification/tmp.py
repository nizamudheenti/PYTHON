def read_data():
    import pandas as pd
    data=pd.read_csv('name.csv',index_col='no')
    length=(len(data))
    face_id = input('\n enter name end press <return> ==>  ')
    data.loc[length+1]=[face_id]
    data.to_csv('name.csv')
    return length+1