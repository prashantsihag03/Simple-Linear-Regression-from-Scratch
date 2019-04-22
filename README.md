# Simple-Linear-Regression-from-Scratch
In this repository, I have created  Simple Linear Regression algorithm from scratch in a simplest way.

## DataSet ##
The data set used is completely fictional and consists only 4 attributes where first atribute is taken as independent variable and last attribute is target variable. 
Attributes are: EngineSize, Cylinders, Fuel Consumption, CO2Emission.

## Dependencies & Installation ##
* **Numpy**: NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.**Installation**: pip install numpy

* **Pandas**: Pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.
**Installation**: pip install pandas

## Working ##
The focus of this program is on simple linear regression which include only one dependent and one independent variable.
As we know that linear regression helps in predicting continuous values only, i have taken a fictional dataset of cars where we are taking engine size as independent variable and CO2 emission as target/dependent variable.

For better understanding of dataset, below provided scatterplot shows the linear relationship between these two variables.
![Image of bar graph](https://github.com/prashantsihag03/Simple-Linear-Regression-from-Scratch/blob/master/extra/graph.png)

With linear regression you can fit a line through the data.For instance, as the EngineSize increases, so do the emissions.A good model can be used to predict what the approximate emission of each car is.<br>
The form of the model would be: ***yhat = θ0 +θ1 x1*** <br>
In this equation, *yhat* is the dependent variable or the predicted value, and x1 is the independent variable; θ0 and θ1 are the parameters of the line that we must adjust. θ1 is known as the "slope" or "gradient" of the fitting line and θ0 is known as the "intercept." θ0 and θ1 are also called the coefficients of the linear equation. You can interpret this equation as yhat being a function of x1, or yhat being dependent of x1.

Linear regression estimates the coefficients of the line. This means we must calculate θ0 and θ1 to find the best line to ‘fit’ the data.
As mentioned before, θ0 and θ1, in the simple linear regression, are the coefficients of the fit line. We can use a simple equation to estimate these coefficients. That is, given that it’s a simple linear regression, with only 2 parameters, and knowing that θ0 and θ1 are the intercept and slope of the line, we can estimate them directly from our data. It requires that we calculate the mean of the independent and dependent or target columns, from the dataset.It can be shown that the intercept and slope can be calculated using these equations. We can start off by estimating the value for θ1.
This is how you can find the slope of a line: 

![Image of bar graph](https://github.com/prashantsihag03/Simple-Linear-Regression-from-Scratch/blob/master/extra/Equation.png)

And bias can be found by using the main equation of linear regresion which is : bias = mean value of y - (slope*\mean value of x).
finally, we are ready to predict.
