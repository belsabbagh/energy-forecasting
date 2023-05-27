# Notes

## Stuff to do

- Calculate correlation between different energy consumptions and productions for each country.
  - To prove that there is a relationship between the different energy sources.
- Forecast energy consumption and production for each country.
  - Calculate forecasting errors and stuff.

## Abstract

In a world where energy is becoming more and more important, it is crucial to be able to forecast energy consumption and production. This can give decision makers an advantage when deciding how to allocate resources and have a deeper insigt into the potential future of the environment given the current trends in energy production and consumption. This study aims to compare the performance of different time series forecasting models and develop a framework for efficiently dealing with historical energy data and applying better preprocessing and analysis on it to fine-tune the models. We have found that neural networks outperform other models in terms of forecasting accuracy despite them being more computationally expensive than other projective forecasting techniques. We have also found that results are best when each country's data is treated individually rather than applying a generalized preprocessing technique on all countries.

## Introduction

The last 30 years have seen great changes in how the world uses and produces energy. Not only does the world produce more energy because of the increasing demand, but also the world is starting to vary its energy sources and moving to cleaner, more sustainable energy sources. With our knowledge of how energy production and consumption changed over the last 30 years, we want to forecast what the future for energy may look like. We will be looking at five major energy sources that the world relies on: coal, petroleum, natural gas, nuclear, and renewable energy. The data collected from the Energy Information Administration (EIA) shows the energy consumption and production for each of these sources for all countries in the world. This data is collected from 1980 to 2021. To forecast the energy consumption and production for each country, we will require solid knowledge of the history of these countries within the set time period as not all countries existed for this entire time period.

In this paper, we will be forecasting energy consumption and production for different countries using different models and comparing their performance. This study should distinguish the differnet forecasting models and their performance on different datasets. We will be looking at the energy consumption and production for each of these sources for different countries. We will be using different forecasting models to forecast the energy consumption and production for each country. We will then compare the performance of these models and see which one is the best for forecasting energy consumption and production. We will be using prior knowledge of the history of these countries to fill the missing values for the energy consumption and production for each country. For example, Germany's data from before 1990 will be missing because Germany was split into two countries, East Germany and West Germany. So, we will be filling the missing values for Germany's energy consumption and production from 1980 to 1990 using the sum of the data from East Germany and West Germany. Other examples of missing data would be descendants of the Soviet Union and South Sudan gaining its independence in 2012. After we have filled all the data and grouped the data by country, we can run an analysis on each country's resource production and consumption to decompose the time series and identify its patterns. We will then use this analysis to tune each model to each country's data. We will then forecast the energy consumption and production for each country using each model. We will then compare the performance of each model and share our findings on which models performed best given specific key performance indicators.


## Error Metrics

We will be using three different error metrics to compare the performance of the different models. These error metrics are the mean squared error (MSE), root mean squared error (RMSE), and mean absolute error (MAE). The MSE is the average of the squared differences between the actual values and the predicted values. The RMSE is the square root of the MSE. The MAE is the average of the absolute differences between the actual values and the predicted values. The MSE and RMSE are more sensitive to outliers than the MAE. The MAE is more robust to outliers than the MSE and RMSE. The MSE and RMSE are more commonly used than the MAE. The MSE and RMSE are more sensitive to outliers than the MAE. The MAE is more robust to outliers than the MSE and RMSE. The MSE and RMSE are more commonly used than the MAE. The MSE and RMSE are more sensitive to outliers than the MAE. The MAE is more robust to outliers than the MSE and RMSE. The MSE and RMSE are more commonly used than the MAE. The MSE and RMSE are more sensitive to outliers than the MAE. The MAE is more robust to outliers than the MSE and RMSE. The MSE and RMSE are more commonly used than the MAE. The MSE and RMSE are more sensitive to outliers than the MAE. The MAE is more robust to outliers than the MSE and RMSE. The MSE and RMSE are more commonly used than the MAE.

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$
$$RMSE = \sqrt{MSE}$$
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

## Conclusion

In this paper, we have concluded that deep learning-based models are able to outperform other models in terms of forecasting accuracy. We have also concluded that the performance of the models is majorly dependent on the country's data. It is simply not possible to achieve good results without treating each country individually in terms of preprocessing, analysis, and model tuning. Each country requires it's own preprocessing methodology as well as its own model tuning. However, additive models seem to generally perform well on most data compared to multiplicative models. Deep learning models were more adaptive in the sense that they did not need any hyperparameter tuning for them to give good results on most countries.


## Weighted Average

The weighted average method is a simple projective forecasting method that assigns weights to the historical data and uses these weights to forecast the future values. The weights are assigned to the historical data based on how recent the data is. The more recent the data is, the higher the weight assigned to it. The weights can be set manually for each timestamp or can be a function of the current time. The weights are assigned in a way that the sum of the weights is equal to 1.
$$\hat{y}_{t+h|t} = \sum_{i=1}^{n}w_iy_{t+h-i}$$


## Exponential Smoothing

$$FIT_t = F_t + T_t$$
$$F_{t} = \alpha y_{t} + (1 - \alpha)FIT_{t-1}$$
$$T_{t} = \beta(F_{t} - F_{t-1}) + (1 - \beta)T_{t-1}$$
