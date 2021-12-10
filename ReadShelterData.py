#Title: Rescuing Rescues
#Name: Serrin Doscher
#Email: serrin.doscher53@myhunter.cuny.edu
#Resources: CSCI39542, w3schools, stackoverflow, codepen, matplotlib.org, HTML and CSS tutorials on YouTube
#URL: https://serrin-sage.github.io/DataScienceProject/


#importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#create dataframe from read csv
shelter_data_avg = pd.read_csv('shelter_data_avg.csv')
shelter_df = pd.DataFrame(shelter_data_avg)

#create area graph based on the given Dataframe
#Data is set within function and can not be changed by user
def createAreaGraph(df):
    shelter_df = pd.DataFrame(df)
    fig = plt.figure(figsize=(12,8))

    sns.set_theme()

    colors = sns.color_palette("Set1")
    date_axis = shelter_df['year']
    adoption = shelter_df['adoptions']
    stray = shelter_df['stray']
    euth = shelter_df['euthanasia']

    plt.stackplot(date_axis, euth, stray, adoption, labels=['Euthanasia','Strays','Adoptions'], colors=colors, alpha=0.6)
    plt.legend(loc='upper right')

    plt.xticks(date_axis)

    plt.title('Outcome of Shelter Animals 2016-2020', fontweight='bold', fontsize=20)
    plt.xlabel('Year', fontweight='bold', fontsize=15)
    plt.ylabel('Intake', fontweight='bold', fontsize=15)

    return fig

#create a line graph based on the given Dataframe
#Data is set within function and can not be changed by user
def createLineGraph(df):
    shelter_df = pd.DataFrame(df)
    fig = plt.figure(figsize=(12,8))

    sns.set_style('darkgrid')
    date_axis = shelter_df['year']
    g_intake = shelter_df['gross_intake']
    live = shelter_df['live_outcome']
    other = shelter_df['other_outcome']

    plt.plot(date_axis, g_intake, label="Gross Intake")
    plt.plot(date_axis, live, label="Live Outcome")
    plt.plot(date_axis, other, label="Other Outcome")

    plt.xticks(date_axis)

    plt.title('Average Intake NY 2016-2020', fontweight='bold', fontsize=20)
    plt.xlabel('Year', fontweight='bold', fontsize=15)
    plt.ylabel('Intake', fontweight='bold', fontsize=15)
    plt.legend(loc='upper right')
    return fig

#create a pie chart based on the given Dataframe and year
#Data is influenced by users input
def createPieChart(df, year, title, cat, dog):
    if year == '2016':
        pos = 0
    elif year == '2017':
        pos = 1
    elif year == '2018':
        pos = 2
    elif year == '2019':
        pos = 3
    elif year == '2020':
        pos = 4
    shelter_df = pd.DataFrame(df)

    fig = plt.figure(figsize=(12,8))

    cat_data = shelter_df._get_value(pos, cat)
    dog_data = shelter_df._get_value(pos, dog)

    labels = [f'Cats: {cat_data}', f'Dogs: {dog_data}']
    colors = ['sandybrown','skyblue']
    animal_data = np.array([cat_data, dog_data])

    plt.pie(animal_data, labels=labels, colors=colors, autopct='%.1f%%')
    plt.title(f"Cat and Dog Distribution for {title} in " + year, fontweight='bold')
    return fig

#create a bar graph based on the given Dataframe and the data type
#Data is influenced by users input
def createBarGraph(df, main_col, title, cat, dog):
    sheler_df = pd.DataFrame(df)

    bar_width = 0.25
    fig = plt.subplots(figsize = (12,8))

    cat_data = sheler_df[cat]
    dog_data = sheler_df[dog]
    total = sheler_df[main_col]

    bar1 = np.arange(len(total))
    bar2 = [x + bar_width for x in bar1]
    bar3 = [x + bar_width for x in bar2]

    plt.bar(bar1, total, color='lightcoral', width=bar_width, edgecolor='grey', label=title)
    plt.bar(bar2, cat_data, color='sandybrown', width=bar_width, edgecolor='grey', label=f'Cat {title}')
    plt.bar(bar3, dog_data, color='skyblue', width=bar_width, edgecolor='grey', label=f'Dog {title}')

    plt.xlabel('Year', fontweight='bold', fontsize=15)
    plt.ylabel(title , fontweight='bold', fontsize=15)
    plt.xticks([r + bar_width for r in range(len(total))], shelter_df['year'])
    plt.title(f'Distribution for {title} 2016-2020', fontweight='bold', fontsize=15)
    plt.legend(loc='upper right')

    return fig

#Asks the user for input: Which graph type to generate and with what data
while(True):
    graph_type = str(input("Enter preferred graph type to view data (Line, Area, Pie, Bar) : "))

    if graph_type == 'Line':
        createLineGraph(shelter_df)
        break

    elif graph_type == 'Area':
        createAreaGraph(shelter_df)
        break

    elif graph_type == 'Pie':
        while(True):
            data_type = str(input("Enter preferred data (gross_intake, live_outcome, adoptions, stray, or euthanasia) : "))
            while (True):
                year = str(input("Enter preferred year (2016, 2017, 2018, 2019, or 2020) : "))
                if year == '2016':
                    break
                elif year == '2017':
                    break
                elif year == '2018':
                    break
                elif year == '2019':
                    break
                elif year == '2020':
                    break
                else:
                    print("Invlaid input, please try again")
                    continue
            if data_type == 'gross_intake':
                title = 'Gross Intake'
                cat = 'cat_intake'
                dog = 'dog_intake'
                break
            elif data_type == 'live_outcome':
                title = 'Live Outcome'
                cat = 'cat_outcome'
                dog = 'dog_outcome'
                break
            elif data_type == 'adoptions':
                title = 'Adoptions'
                cat = 'cat_adopt'
                dog = 'dog_adopt'
                break
            elif data_type == 'stray':
                title = 'Stray Population'
                cat = 'cat_stray'
                dog = 'dog_stray'
                break
            elif data_type == 'euthanasia':
                title = 'Euthanized in Shelter'
                cat = 'cat_euth'
                dog = 'dog_euth'
                break
            else:
                print("Invlaid input, please try again")
                continue
        createPieChart(shelter_df, year, title, cat, dog)
        break


    elif graph_type == 'Bar':
        while(True):
            data_type = str(input("Enter preferred data (gross_intake, live_outcome, adoptions, stray, or euthanasia) : "))
            if data_type == 'gross_intake':
                cat = 'cat_intake'
                dog = 'dog_intake'
                title = 'Gross Intake'
                break
            elif data_type == 'live_outcome':
                cat = 'cat_outcome'
                dog = 'dog_outcome'
                title = 'Live Outcome'
                break
            elif data_type == 'adoptions':
                cat = 'cat_adopt'
                dog = 'dog_adopt'
                title = 'Adoptions'
                break
            elif data_type == 'stray':
                cat = 'cat_stray'
                dog = 'dog_stray'
                title = 'Stray Population'
                break
            elif data_type == 'euthanasia':
                cat = 'cat_euth'
                dog = 'dog_euth'
                title = 'Euthanasia Count'
                break
            else:
                print("Invlaid input, please try again")
                continue
        createBarGraph(shelter_df, data_type, title, cat, dog)
        break
    else:
        print("Invlaid input, please try again")
        continue

plt.show()
