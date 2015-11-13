# -------- Identifying changing market conditions ----
# Author: Ranaji Krishna.
# Date:   Sept. 23 2015.
# Notes:  The code was developed to identify 
#         different market regimes by using HMM.
# ---------- #


rm(list = ls(all = TRUE));  # clear all.
graphics.off();             # close all.

library("gdata")           # Importing excel data.
library("xts")
library("data.table")
library("zoo")
library("mondate")
library("grDevices")
library("scales")
library("ggplot2")
require("xlsx")
library("Matrix")
library("quantmod")
library("depmixS4")

# ====== Data ===== #
setwd('/Users/vashishtha/myGitCode/myProj/myCodeR/ML/HMM')   # Set directory.
EURUSD1d <- read.csv('EURUSD1d.csv', stringsAsFactor = TRUE) # Import data.

Date <- as.character(EURUSD1d[,1])
DateTS <- as.POSIXlt(Date, format = "%Y.%m.%d %H:%M:%S")     # Create date and time objects.
TSData <- data.frame(EURUSD1d[,2:5],row.names=DateTS)
TSData <- as.xts(TSData)                                     # Build our time series data set.
# ====== #

plot_TSData <- as.zoo(TSData)
myColors <- c("darkblue", "darkgreen","red","black")
pdf("plot_val.pdf")
plot(x = plot_TSData, ylab = "EURUSD", main = "Daily Values", col = myColors, screens = 1)
legend(x = "topleft", legend = c("Open","High","Low","Close"),
       lty = 1, col = myColors)
dev.off()

ATRindicator <-ATR(TSData[,2:4],n=14)            # Calculate the indicator.
ATR <-ATRindicator[,2]                           # Grab just the ATR.

LogReturns <- log(EURUSD1d$Close) - log(EURUSD1d$Open) # Calculate the logarithmic returns
ModelData <- data.frame(LogReturns,ATR)                # Create the data frame for our HMM model

ModelData<-ModelData[-c(1:14),]                  # Remove the data where the indicators are being calculated
colnames(ModelData) <- c("LogReturns","ATR")     # Name our columns

set.seed(1)
HMM <- depmix(list(LogReturns~1,ATR~1),data=ModelData,nstates=3,family=list(gaussian(),gaussian())) 
# We’re setting the LogReturns and ATR as our response variables, using the data frame we just built, 
# want to set 3 different regimes, and setting the response distributions to be gaussian.

HMMfit <- fit(HMM, verbose = FALSE) # Fit our model to the data set.
HMMpost <- posterior(HMMfit)        # Find the posterior odds for each state over our data set

browser()


