
rm(list = ls(all = TRUE));  # clear all.
graphics.off();             # close all.


library("corpcor");         # inverse of covarisanvce matrix.
library("gdata");           # importing excel data.
library("xts");
library("data.table");
library("zoo");
library("mondate");
library("grDevices");

require("xlsx");
require("lmtest");
require("bstats");          # White Test.
require("leave_out_cross_validation");
library("fOptions");        # For GBSOptions.


# ====== Data =====
setwd('/Users/rkrishna/ranajiIntercomCode/activationMetric/sqlCode/');   # Set director.y
dataAll <- read.csv('activData_v3.csv', stringsAsFactor = TRUE);         # Import data.


# ---- Daily Average -----
sub_id = 5675;
dataAll$sum_tot_dur[which(dataAll$old_id < sub_id)] = dataAll$sum_tot_dur[which(dataAll$old_id < sub_id)]/30;    # 30- day trial.
dataAll$sum_tot_dur[which(dataAll$old_id > sub_id)] = dataAll$sum_tot_dur[which(dataAll$old_id > sub_id)]/14;    # 14- day trial.
dataAll$sum_tot_dur[which(is.na(dataAll$old_id))] = dataAll$sum_tot_dur[which(is.na(dataAll$old_id))]/14;        # 14- day trial.   
# -------- #

dataAll[is.na(dataAll)] <- 0;                         # Convert NA to 0.
#dataAll <- na.omit(dataAll);

drops <- c('first_payment','old_id','avg_daily_msgs');               # Drop columns.
# 'sub_trial_st','trial_ed','sessions_app_id',

colnames <- c('app_id', 'sum_tot_dur','tot_users','avg_daily_users', # Colnames. ,'avg_daily_msgs'
              'avg_daily_cnvs','avg_daily_cmts','avg_daily_mails',
              'avg_daily_admins','time_to_trial','second_payment');

data <- dataAll[,!names(dataAll) %in% drops];              # Drop columns
data <- data[colnames];                                    # Re-order columns.
null_app_id <- data[which(is.na(data$avg_daily_cnvs)), 1]; # App ids with NULL entries in converstaions.
#data <- data[!data$app_id %in% null_app_id, ];             # Drop rows with NA in conversations.


# ---- Normalise Daily Comments, Conversations and  mails by total users -----
#browser()
data[which(data$avg_daily_users != 0), c(5,7)] = data[which(data$avg_daily_users != 0), c(5,7)]/data$avg_daily_users[which(data$avg_daily_users != 0)];
#data[which(data$avg_daily_admins != 0), 6] = data[which(data$avg_daily_admins != 0), 6]/data$avg_daily_admins[which(data$avg_daily_admins != 0)];

# ---- Normalise sum_tot_dur by total admins -----
data[which(data$avg_daily_admins != 0), 2] = data[which(data$avg_daily_admins != 0), 2]/data$avg_daily_admins[which(data$avg_daily_mails != 0)];
# -------- #


# ====== Universe =====
corr <- data.frame(matrix(0, c( (dim(data)[2] - 2 ) , 2)));   # Store correlation values.
row.names(corr) <- colnames[2: (dim(data)[2] - 1)];          # Name rows.
colnames(corr) <- "Correlation Values";    # Name cols.

# ------ Plots -------
pdf(file = ifelse(TRUE, "activMetric_plot1.pdf"));  # Save plot.
#X11();
par(mfrow= c(1,1)); int <- 1; 

for (i in 2 : (dim(data)[2] - 1) ){  
  corr[int,1] <- cor(data[,i],data$second_payment);     # Compute correlation.
  plot(data[,i], data[ , dim(data)[2]], xlab = colnames(data)[i], ylab = colnames(data)[dim(data)[2]]);   # Plot 
  int <- int + 1;
}
dev.off();

# ===== Delete Outliers =====

dur_app_id <- data[which(data$sum_tot_dur > 2e5), 1];        # App ids with total duration > 1e7.
data <- data[!data$app_id %in% dur_app_id, ];                # Drop rows with NA in conversations.

tot_users_app_id <- data[which(data$tot_users > 1.5e6), 1];    # App ids with average daily user > 2e4.
data <- data[!data$app_id %in% tot_users_app_id, ];               # Drop rows with NA in conversations.

user_app_id <- data[which(data$avg_daily_users > 5e4), 1];    # App ids with average daily user > 2e4.
data <- data[!data$app_id %in% user_app_id, ];               # Drop rows with NA in conversations.

# msgs_app_id <- data[which(data$avg_daily_msgs > 200), 1];    # App ids with NULL entries in converstaions.
# data <- data[!data$app_id %in% msgs_app_id, ];               # Drop rows with NA in conversations.

cnvs_app_id <- data[which(data$avg_daily_cnvs > 1), 1];   # App ids with NULL entries in converstaions.
data <- data[!data$app_id %in% cnvs_app_id, ];               # Drop rows with NA in conversations.

cmts_app_id <- data[which(data$avg_daily_cmts > 5), 1];    # App ids with NULL entries in converstaions.
data <- data[!data$app_id %in% cmts_app_id, ];               # Drop rows with NA in conversations.

mails_app_id <- data[which(data$avg_daily_mails > 0.5), 1];  # App ids with NULL entries in converstaions.
data <- data[!data$app_id %in% mails_app_id, ];              # Drop rows with NA in conversations.

admins_app_id <- data[which(data$avg_daily_admins > 20), 1]; # App ids with NULL entries in converstaions.
data <- data[!data$app_id %in% admins_app_id, ];            # Drop rows with NA in conversations.


# ------ Plots -------
corr_clean <- data.frame(matrix(0, c((dim(data)[2] - 2), 2)));    # Store correlation values.
row.names(corr_clean) <- colnames[2 : (dim(data)[2] - 1) ];         # Name rows.
colnames(corr_clean) <- "Correlation Values";   # Name cols.

pdf(file = ifelse(TRUE, "activMetric_plot2.pdf"));  # Save plot.
#X11();
par(mfrow= c(1,1)); int <- 1; 
for (i in 2 : (dim(data)[2] - 1) ){  
  corr_clean[int,1] <- cor(data[,i],data$second_payment);     # Compute correlation.
  plot(data[,i], data[ , (dim(data)[2])], xlab = colnames(data)[i], ylab = colnames(data)[ (dim(data)[2]) ]);   # Plot 
  int <- int + 1;
}
dev.off();

# ===== Regression ======
# regResults <- glm(data$second_payment ~ data$sum_tot_dur + data$avg_daily_admins  + data$avg_daily_cmts 
#                 + data$time_to_trial  + data$avg_daily_cnvs , data, family = quasipoisson()); 

# data$avg_daily_msgs + data$avg_daily_cnvs + data$avg_daily_cmts + data$avg_daily_mails + + data$time_to_trial + data$avg_daily_user

bin_val <- data$second_payment; 
data <- cbind(data,bin_val);
data$bin_val[data$bin_val != 0] <- 1;

regResults <- glm(data$bin_val ~ data$sum_tot_dur + data$avg_daily_admins  + data$avg_daily_cmts 
                  + data$time_to_trial  + data$avg_daily_cnvs , data, family = quasipoisson()); 
#+ data$tot_users + data$avg_daily_users + data$avg_daily_mails


# regResults <- glm(data$bin_val ~ data$sum_tot_dur +  data$avg_daily_cmts + data$avg_daily_mails + 
#                    data$time_to_trial +  data$avg_daily_admins, data, family = binomial(link=logit)); 
#  + data$tot_users + data$avg_daily_user + data$avg_daily_cnvs +


source('/Users/rkrishna/ranajiIntercomCode/activationMetric/codeR/leave_out_cross_validation.R');   # Set directory

cfusionMat <- leave_out_cross_validation(data[1:10,]);




browser()

# --- Test for normality of errors ---
shapiro.test(as.matrix(regResults$residuals[1:5000]));


# --- Heteroskedasticity Test ----
bptest(data$second_payment ~ data$sum_tot_dur + data$tot_users + data$avg_daily_user + data$avg_daily_cnvs + data$avg_daily_cmts +
         data$avg_daily_mails + data$avg_daily_admins + data$time_to_trial, data = data);

# --- Test for Serially correlated errors ----
bgtest(data$second_payment ~ data$sum_tot_dur + data$tot_users + data$avg_daily_user + data$avg_daily_cnvs + data$avg_daily_cmts +
         data$avg_daily_mails + data$avg_daily_admins + data$time_to_trial, data = data);

# ---- Adjusting for Heteroskedasticity in Error ----

#vcovHC(regResults);
#coeftest(regResults, vcov = vcovHC);


#CTRL + SHIFT + C
