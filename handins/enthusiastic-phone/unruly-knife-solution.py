import pandas as pd
import numpy as np
import matplotlib.pyplot as pp

global DATA



def get_data(url=None, file_name='C:/datamatiker/python/exercises/handins/enthusiastic-phone/dataset/database.csv'):
    if url:
        webget.download(url, file_path)
    global DATA
    DATA = pd.read_csv(file_path, low_memory=False)
    print(DATA.columns, "\n")

def common_perpetrators_and_victims():
    cols = ['Victim Ethnicity', 'Perpetrator Ethnicity']
    df = [DATA[cols]]
    print("Victim Ethnicities:\n {0}\n\n".format(DATA['Victim Ethnicity'].value_counts()))
    print("Perpetrator Ethnicities:\n {0}\n\n".format(DATA['Perpetrator Ethnicity'].value_counts()))

def preferred_weapons_by_gender():
    cols = ['Perpetrator Sex', 'Weapon']
    df = DATA[cols]
    masks = {}
    masks['Female'] = (df['Perpetrator Sex']=='Male')
    masks['Male'] = (df['Perpetrator Sex']=='Female')
    masks['Unknown'] = (df['Perpetrator Sex']=='Unknown')
    for k, v in masks.items():
        print("{0} genders preferred weapons:\n{1}\n\n".format(k, df[v]['Weapon'].value_counts()))

def youngest_and_oldest_victim():
    df = DATA['Victim Age']
    print("youngest victim was {0} years old".format(df.min()))
    print("oldest victim was {0} years old".format(df.max()))
    print("victim average age is {0} years".format(df.mean()))

def male_to_female_ratio():
    df = DATA['Perpetrator Sex'] # reduce the size of the dataframe we're working on
    male_count = df.where(df=='Male').count()
    female_count = df.where(df=='Female').count()
    print("male to female ratio is: {0}".format(male_count/female_count))

def top_states(count=10):
    df = DATA['State']
    dframe = df.value_counts()[0:count]
    states_dict = dict(dframe.value_counts())

# plot setup
    index = 1
    bar_width = 0.3
    pp.figure(figsize=(12, 8))
    ax = dframe.plot(kind='bar')
    ax.set_title('top {0} murder states'.format(count))
    ax.set_xlabel('murders')
    ax.set_ylabel('state')
    # ax.set_xticklabels()
    rects = ax.patches
    labels = states_dict.keys()
    for rect, label in zip(rects, labels): # add labels to the columns
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')
    pp.show()

def wait():
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass

get_data()
wait()
common_perpetrators_and_victims()
wait()
preferred_weapons_by_gender()
wait()
youngest_and_oldest_victim()
wait()
male_to_female_ratio()
wait()
top_states()
