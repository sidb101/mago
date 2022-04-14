import pandas as pd

fnames = [('Common Words I', 51), ('Common Words II', 51), ('Common Words III', 51), ('Common Words IV', 51), ('Common Words V', 51), ('Common Words VI', 51), \
    ('Basic I', 50), ('Basic II', 50), ('Basic III', 50), ('Basic IV', 50), ('Basic V', 50), ('Basic VI', 50), ('Basic VII', 51), ('Advanced I', 50), ('Advanced II', 51), \
    ('Advanced III', 50), ('Advanced IV', 51), ('Advanced V', 50), ('Advanced VI', 50), ('Advanced VII', 50)]

df = pd.DataFrame({'deck':[], 'word':[], 'meaning':[], 'example':[]})

for fname in fnames:
    dft = pd.read_csv(fname[0]+'.csv')
    dft = dft[['deck', 'word', 'meaning', 'example']]
    # ['deck', 'word', 'meaning', 'example']
    print(dft.columns)
    df = df.append(dft)

df.to_csv('AllDecks.csv', index=False)