import numpy as np
import pandas as pd

def load_data(file, dependent_var, independent_var):
    data = pd.read_csv(file, header=None)
    data.head()
    data.decsribe()
    x_test = np.array(data.iloc[: ,dependent_var])
    y_test = np.array(data.iloc[: ,independent_var])
    return x_test, y_test

def mean(train_list):
    xsum = 0.0
    mean = 0.0
    summation = 0.0
    for i in range(0,len(train_list)):
        summation = summation + train_list[i]
    mean = summation/len(train_list)
    return mean

def slope(xtrain, ytrain, xmean, ymean):
    numerator = 0.0
    denomenator = 0.0
    xval = 0.0
    yval = 0.0
    for i in range(0, len(xtrain)):
        xval = xtrain[i]-xmean
        yval = ytrain[i]-ymean
        val = xval*yval
        numerator = numerator + val
        denomenator = denomenator + xval ** 2
    
    slope = numerator / denomenator
    return slope

def bias(slope, xmean, ymean):
    bi = ymean - slope*xmean
    return bi

def predict(slope, bias, x):
    y = bias + slope*x
    return y

def main(file, predict_val):
    #loading data
    xtrain, ytrain = load_data(file, 0, 3)
    print("X train : ",xtrain)
    print("Y train : ",ytrain)

    #finding mean 
    xmean = mean(xtrain)
    ymean = mean(ytrain)
    print("xmean: ",xmean)
    print("ymean: ", ymean)

    #finding slope
    theta1 = slope(xtrain, ytrain, xmean, ymean)
    print("Slope: ",theta1)

    #finding bias
    theta = bias(theta1, xmean, ymean)
    print("Bias: ",theta)

    #predicting
    prediction = predict(theta1, theta, predict_val)
    print("Predicted value of CO2 Emission: ",prediction)
    
#loading dataset
file = "F:/Prashant/DS/5. Machine Learning/Projects/Simple_Linear_Regression_Scratch/car.csv"
value = float(input("Enter value for Engine Size: "))
main(file, value)
        
