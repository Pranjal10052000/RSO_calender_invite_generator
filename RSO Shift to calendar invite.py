#!/usr/bin/env python
# coding: utf-8

# In[36]:


def RSO_cal():
    path = str(input("enter the csv file name"))
    cal_file_name = str(input("enter calender file name"))
    
    df = pd.read_csv(path)
    
    #csv cleaning
    df['TeamWork'][3]= 'Date'
    df.drop(columns=df.columns[0], axis=1,  inplace=True)
    new_header = df.iloc[3] #grab the first row for the header
    df = df[4:] #take the data less the header row
    df.columns = new_header
    df.drop(df.tail(2).index, inplace=True)
    
    #creating calender
    calendar = Calendar()

    for index, row in df.iterrows():
        event = Event()

        start_time = datetime.strptime(row['Date'] + ' ' + row['Start'], '%a, %m/%d/%Y %I:%M %p')
        end_time = datetime.strptime(row['Date'] + ' ' + row['End'], '%a, %m/%d/%Y %I:%M %p')

        if end_time < start_time:  # Handle shifts that end on the next day
            end_time += timedelta(days=1)

        event.name = "Shift at " + row['Station']
        event.begin = start_time
        event.end = end_time

        calendar.events.add(event)

    # Save the calendar to an .ics file
    with open(cal_file_name , 'w') as invite_file:
        invite_file.writelines(calendar)

    print("Apple Calendar invite files generated successfully!")


# In[37]:


RSO_cal()


# In[ ]:




