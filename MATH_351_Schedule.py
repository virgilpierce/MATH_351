#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pa
import datetime as dt
pa.set_option('max_colwidth', 200)


# In[2]:


first_day = dt.date(2020, 1, 11)


# In[3]:


holidays = [dt.date(2020, 1, 18) ]
spring_break_start = dt.date(2020, 3, 13)
spring_break_end = dt.date(2020, 3, 21)
spring_break_delta = spring_break_end - spring_break_start
holidays += [ spring_break_start + dt.timedelta(i) for i in range(spring_break_delta.days+1)]


# In[4]:


last_day = dt.date(2020, 4, 30)


# In[5]:


final_exam = dt.date(2020, 5, 7)


# In[6]:


semester_length = last_day - first_day
semester_length


# In[18]:


class_days = []
for i in range((semester_length.days //7 + 1)):
    class_days += [first_day + dt.timedelta(1) + dt.timedelta(i*7), first_day + dt.timedelta(1) + dt.timedelta(i*7+2)]
    # shift first day by 1 for TR class
class_days += [final_exam]


# In[19]:


schedule = pa.DataFrame(class_days, columns = ['Day'])
weekday_dict = {5:'Monday', 6:'Tuesday', 0:'Wednesday', 1:'Thursday', 2:'Friday', 3:'Saturday', 4:'Sunday'}
for i in range(schedule.shape[0]):
    schedule.loc[i,'Week_Day'] = schedule.loc[i, 'Day'].weekday()
schedule.Week_Day = schedule.Week_Day.map(weekday_dict)


# In[21]:


for holiday in holidays:
    schedule.loc[schedule.Day==holiday, 'Title'] = 'No Class - University Holiday'


# In[22]:


def add_day(title='', description='', notes=''):
    global schedule
    global day
    
    while schedule.loc[day, 'Day'] in holidays:
        day += 1
    if day >= schedule.shape[0]:
        print('Error to many days')
        return 'ERROR'
    else:
        schedule.loc[day, 'Title'] = title
        schedule.loc[day, 'Description'] = description
        schedule.loc[day, 'Notes'] = notes
        
        day += 1
    


# In[33]:


day = 0

# Discrete

add_day('Discrete Random Variables', 
        'Discrete random variables and their probability distributions, simmulating discrete random variables')

add_day('Expected Value of Discrete Random Variable', 'Computing the expected value of a discrete random variable')

add_day('Binomial and Geometric Probability Distributions')

add_day('Poisson Probability Distribution')


# Continuous

add_day('Continuous Random Variables', 
        'probability density, cummulative distribution function, expected values, uniform distribution, and simmulating a continuous random variable')

add_day('Normal Probability Distribution')

add_day('Gamma and Beta Probability Distributions')

add_day('Other expected values and momemnt')

# Multivariate

add_day('Multivariate Probability Distributions', 'marginal and conditional probability distributions')

add_day('Independent Random Variables')

add_day('Expected Value of Multivariate Random Variables and some Special Theorems')

add_day('Sampling depedent random variables', 
        'Sampling dependent random variables is much harder than sampling single or independent random variables')

add_day('The Covariance of Two Random Variables')

add_day('Expected values and variance of linear functions of random variables')

add_day('The multinomial probability distribution')

add_day('Conditional Expectations')

# Functions of multivariate random variables

add_day('Finding the Probability Distribution of a Function of Random Variables')

add_day('Order Statistics')

# Sampling Distributions

add_day('Sampling Distributions Related to the Normal Distribution')

add_day('The Central Limit Theorem')

add_day('Normal Approximation to the Binomial Distribution')

# Estimation

add_day('Point Estimators')

add_day('Confidence Intervals')

add_day('Sample Size Concerns')

add_day('Methods of Estimation')

# Hypothesis Testing

add_day('Common Large Sample Tests')

add_day('Type II Error Probabilities')

add_day('Hypothesis Testing and Confidence Intervals')

add_day('More Hypothesis Testing')

add_day('Considerations in Experimental Designs')

add_day('Alternative Approaches', 
        'In our last class we will take a look ahead to the methods of Data Science and resampling for hypothesis testing and confidence intervals')

schedule


# In[ ]:




