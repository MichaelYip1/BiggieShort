# Biggie_Short

Project 2 for the FinTech Bootcamp

* Team Mates
	* JC
	* Mike Yip
	* Miks

## Purpose

Our project is to predict buy/sell prices for iShares U.S. Real Estate ETF (IYR, created year 2000, 4th of June). The Case-Schiller Index, an older historical index, was used as a proxy for IYR after determining an 86% correlation between IYR and Case-Schille Index. We wish to create a bot that executes these trades for us. We will use:

    * a linear regression;
    * a deep neural network model;
    * a random forest algorithm model;
    * LSTM Model 
    * XG Boost Model 
to fit the following data and compare the performance of both models to determine which has sufficient predictive power. To predict this model, we will use 10 parameters from FRED & Quandl API. 

Additionally, we have built a trading bot that had buy and sell orders programmed for when the buy and sell signals were generated from our models using alpaca api and requests library implemented on a python script.
Our goal was to host it on an EC2 instance but only got to creating the virtual machine but the model was not completely set up yet.

The libraries used in this project include sklearn, pandas, hvplot, matplotlib, numpy, statsmodels, os, requests, load_dotenv, alpaca_trade_api, json, random, schedule, time, tensorflow, fredapi, quandl, xgboost, datetime.

## Please see PPT for results and conclusion. Thank you.


