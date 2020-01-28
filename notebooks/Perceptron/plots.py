# display functions

import numpy as np 
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from ipywidgets import widgets, interact, interactive, fixed, interact_manual
from IPython.display import display
import sklearn.model_selection as ms 
import sklearn.linear_model as lm 
import sklearn.metrics as metrics
import sklearn.datasets as dts

def decision_boundary(inputs): 

    y_test = inputs["y_test"]
    x_test = inputs["x_test"]
    slope = inputs["slope"]
    intercept = inputs["intercept"]
    y_pred = inputs["ypred"]

    # isolating data points based on class 
    blue_x = x_test[np.where(y_test ==1)[0]]
    orange_x = x_test[np.where(y_test ==0)[0]]


    # scatter plot with decision boundary
    x_values = np.linspace(-5,5,1000)
    desc_boundary = slope*x_values+ intercept


    # correctly classified points
    class1_correct = np.intersect1d(np.where(y_pred==1), np.where(y_test==1))
    class2_correct = np.intersect1d(np.where(y_pred==0), np.where(y_test==0))
    correct_combined = np.append(class1_correct, class2_correct)

    # finding misclassified points 
    misclassified = np.setdiff1d(np.arange(0,x_test.shape[0]), correct_combined)


    # the main figure object 
    fig = make_subplots(rows=1, cols=2)




    # adding blue class points in right plot
    test_class1 = go.Scatter(
                        x = blue_x[:,0],
                        y = blue_x[:,1],
                        mode="markers",
                        marker=dict(color="blue"),
                        name="test class 1", 
                        
                    )


    # adding orange class points in left plot
    test_class2 = go.Scatter(
                        x = orange_x[:,0],
                        y = orange_x[:,1],
                        mode="markers",
                        marker=dict(color="orange"),
                        name= "test class 2", 
                    
                    )


    # adding blue class points in right plot
    correct_class1 = go.Scatter(
                        x = x_test[class1_correct,0],
                        y = x_test[class1_correct,1],
                        mode="markers",
                        marker=dict(color="blue"),
                        name = "class 1 correct"
                        
                    )

    # adding orange class points in right plot
    correct_class2 = go.Scatter(
                        x = x_test[class2_correct,0],
                        y = x_test[class2_correct,1],
                        mode="markers",
                        marker=dict(color="orange"),
                        name = "class 2 correct"
                        
                    )

    # adding misclassified points
    misclassified_pts = go.Scatter(
                        x = x_test[misclassified,0],
                        y = x_test[misclassified,1],
                        mode="markers",
                        marker=dict(color="red"), 
                        name = "mis-classified points"
                    )

    # line plot for the decision boundary 
    decision_boundary = go.Scatter( 
                        x = x_values,
                        y = desc_boundary,
                        mode = "lines",
                        line = dict(color="green"), 
                        name = "decision boundary"                    
    )


    # adding figure objects
    fig.add_trace(test_class1, row=1, col=1)
    fig.add_trace(test_class2, row=1, col=1)
    fig.add_trace(correct_class1, row=1, col=2)
    fig.add_trace(correct_class2, row=1, col=2)
    fig.add_trace(misclassified_pts, row=1, col=2)
    fig.add_trace(decision_boundary, row=1, col=2)

    # axes properties- labels and ranges 
    fig.update_xaxes(title_text="Feature 1", range=[-5, 5], row=1, col=1)
    fig.update_yaxes(title_text="Feature 2", row=1, col=1)

    fig.update_xaxes(title_text="Feature 1", range=[-5, 5], row=1, col=2)
    fig.update_yaxes(title_text="Feature 2", row=1, col=2)
    fig.update_layout(title_text="Figure 11")
    fig.show()




def interactive_plot(): 

    def widget_function(epochs=100, test_size=0.20, nsamples=1000): 
   
        # generate classification dataset 
        dataset = dts.make_classification(n_samples=nsamples, n_features=2,n_redundant=0,random_state=7)
        # split into test train sets 
        X = dataset[0]
        y = dataset[1]

        x_train, x_test, y_train, y_test = ms.train_test_split(X,y, test_size=test_size, random_state=10)


        perceptron = lm.Perceptron(random_state=12,max_iter=epochs)
        perceptron.fit(x_train, y_train)

        # get predicition and accuracy 
        y_pred = perceptron.predict(x_test)
        accuracy_score = metrics.accuracy_score(y_pred, y_test)


        # get decision boundary paramaters 
        w = perceptron.coef_[0]
        slope = -(w[0]/w[1])
        intercept = -(perceptron.intercept_/w[1])

        # scatter plot with decision boundary
        x_values = np.linspace(-5,5,1000)
        desc_boundary = slope*x_values+ intercept


        # correctly classified points
        class1_correct = np.intersect1d(np.where(y_pred==1), np.where(y_test==1))
        class2_correct = np.intersect1d(np.where(y_pred==0), np.where(y_test==0))
        correct_combined = np.append(class1_correct, class2_correct)
        misclassified = np.setdiff1d(np.arange(0,x_test.shape[0]), correct_combined)


        red_x = x_test[np.where(y_test ==1)[0]]
        blue_x = x_test[np.where(y_test ==0)[0]]

        fig = make_subplots(rows=1, cols=2)

        test_class1 = go.Scatter(
                            x = red_x[:,0],
                            y = red_x[:,1],
                            mode="markers",
                            marker=dict(color="blue"),
                            name="test class 1", 

                        )

        test_class2 = go.Scatter(
                            x = blue_x[:,0],
                            y = blue_x[:,1],
                            mode="markers",
                            marker=dict(color="orange"),
                            name= "test class 2", 

                        )

        correct_class1 = go.Scatter(
                            x = x_test[class1_correct,0],
                            y = x_test[class1_correct,1],
                            mode="markers",
                            marker=dict(color="blue"),
                            name = "class 1 correct"

                        )
        correct_class2 = go.Scatter(
                            x = x_test[class2_correct,0],
                            y = x_test[class2_correct,1],
                            mode="markers",
                            marker=dict(color="orange"),
                            name = "class 2 correct"

                        )

        misclassified_pts = go.Scatter(
                            x = x_test[misclassified,0],
                            y = x_test[misclassified,1],
                            mode="markers",
                            marker=dict(color="red"), 
                            name = "mis-classified points"
                        )
        decision_boundary = go.Scatter( 
                            x = x_values,
                            y = desc_boundary,
                            mode = "lines",
                            line = dict(color="green"), 
                            name = "decision boundary"                    
        )

        fig.add_trace(test_class1, row=1, col=1)
        fig.add_trace(test_class2, row=1, col=1)
        fig.add_trace(correct_class1, row=1, col=2)
        fig.add_trace(correct_class2, row=1, col=2)
        fig.add_trace(misclassified_pts, row=1, col=2)
        fig.add_trace(decision_boundary, row=1, col=2)
        

        fig.update_xaxes(range=[-4,4], title_text="Feature 2", row=1, col=2)
        fig.update_xaxes(range=[-4,4], title_text="Feature 1", row=1, col=1)
        fig.update_yaxes(range=[-4,4], title_text="Feature 2", row=1, col=2)
        fig.update_yaxes(range=[-4,4], title_text="Feature 1", row=1, col=1)
        
        fig.show()

        print("accuracy score {}".format(accuracy_score))
        return None


    im = interact_manual(widget_function, 
                    epochs=widgets.IntSlider(value=100, min=1, max=10000,step=5),
                  nsamples=widgets.IntSlider(value=200, min=100, max=10000, step=100), 
         test_size=widgets.FloatSlider(value=0.1, min=0.1, max=0.9, step=0.1))

    return im 
