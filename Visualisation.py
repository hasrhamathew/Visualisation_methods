# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:56:11 2022

@author: harsha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def ageDependency():
    """ This function reads data from age.csv and plots
    'Age Dependency Ratio vs Countries' with X axix as country and Y axis, Ratio.
    Visualisation method used: Bar Graph"""
    
    #Reading data from a csv file
    age_depend = pd.read_csv("age.csv")
    plt.figure(figsize=(13,14)) 
    plt.xlabel("Country")
    plt.ylabel("Ratio")
    plt.title("Age Dependency Ratio vs Countries(2021)",size=20)
    plt.bar(age_depend["Country Name"], age_depend["2021"])
    plt.xticks(rotation=90)
    plt.savefig('age_visualisation.png')
    plt.show()

def landArea():
    """ This function reads data from land.xlsx and plots
    'Distribution of Total Land Area'.
    Visualisation method used: Pie Chart"""
    
    #Reading data from an excel file
    land_area = pd.read_excel("land.xlsx")
    plt.figure()
    arr = np.array(land_area["Percentage of total land"])
    plt.pie(arr, labels = land_area["Continent or Region"], autopct='%.0f%%')
    plt.title("Distribution of Total Land Area",size=15)
    plt.savefig('land_visualisation.png')
    plt.show()

def unemploymentUk():
    """ This function reads data from unemployment.xlsx and plots
    'Unemployment Rate in the UK(1992-2021)' with X axix Year and Y axis, Unemployment Rate.
    Visualisation method used: Line Plot"""
    
    #Reading data from an excel file
    uk_unemployment = pd.read_excel("unemployment.xlsx")   
    plt.figure()
    plt.plot(uk_unemployment["Year"],uk_unemployment["Unemployment Rate in the UK"],label = 'Unemployment Rate in the UK')
    plt.plot(uk_unemployment["Year"],uk_unemployment["Unemployment Rate in India"],label = 'Unemployment Rate in India')
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate")
    plt.legend()
    plt.xlim(1992) 
    plt.title("Unemployment Rate in the UK vs India(1992-2021)", size=13)
    plt.savefig('unemployment _visualisation.png')
    plt.show()

#Calling the ageDependency function
ageDependency()
#Calling the landArea function 
landArea() 
#Calling the unemploymentUk function
unemploymentUk()

