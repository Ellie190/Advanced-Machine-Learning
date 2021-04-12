# Import library
import numpy as np
import matplotlib.pyplot as plt

# Regression Class
class LinearRegression():
    """ 
    A Simple Linear Regression Model Class:
    Class Attributes:
    x: Independent Variable Input
    y: Dependent Variable Input
    Class Functions:
    designMatrix(): Outputs X n*2 matrix of ones and independent variable inputs
    learnParameter(): Outputs b_0 and b_1 and regression equation
    fitPlot(): Outputs the line of best fit plot 
    Pred(): Takes input and outputs predicted value 
    
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def designMatrix(self):
        global X, Y
        mat_len = len(self.x)
        X = np.matrix([np.ones(mat_len), self.x]).T;
        Y = np.matrix(self.y).T
        return X
    
    def learnParameter(self):
        global x_var, y_var, l_par
        l_par = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
        print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(l_par[0], l_par[1]))
        print("Equation: y_bar = {} + {}x".format(l_par[0], l_par[1]))
    
    def fitPlot(self):
        y_pred = l_par[0] + l_par[1] * self.x
        plt.plot(np.array(self.x), np.array(y_pred).flatten(), color='b');
        plt.scatter(self.x, self.y, color='r');
    
    def Pred(self, val):
        return np.array(l_par[0] + l_par[1] * val).flatten() 
    
# Regression Class Use Case Example
x = [29, 9, 10, 38, 16, 26, 50, 10, 30, 33, 43, 2, 39, 15, 44, 29, 41, 15, 24, 50] # Study hours
y = [65, 7, 8, 76, 23, 56, 100, 3, 74, 48, 73, 0, 62, 37, 74, 40, 90, 42, 58, 100] # Test results

# Create Class object r1
r1 = LinearRegression(x, y)

# Access design Matrix
r1.designMatrix()

# Access Learning parameters
r1.learnParameter()

# Access model fit plot
r1.fitPlot()

# Make predictions
r1.Pred([2,50,30])


