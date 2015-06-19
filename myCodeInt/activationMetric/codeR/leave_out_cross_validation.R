leave_out_cross_validation <- function (data){
  
  predict   <- rep(1, dim(data)[1]);
  true_pos  <- rep(1, 101);
  true_neg  <- rep(1, 101);
  false_pos <- rep(1, 101);
  false_neg <- rep(1, 101);
  
  int_j <- 1;
  
  for (j in seq(0, 1, 1/10)){
    
    for (i in seq(1, dim(data)[1]) ) {
      
      tmpData <- data[-i,];
      
      regResults <- glm(bin_val ~ sum_tot_dur +  avg_daily_cmts + time_to_trial +
                         avg_daily_admins + avg_daily_cnvs, tmpData, family = quasipoisson()); 
      
      strVal <- matrix(c(data$sum_tot_dur[i], data$avg_daily_cmts[i], data$avg_daily_mails[i], 
                         data$time_to_trial[i], data$avg_daily_admins[i]), ncol=5) %*%
        matrix(c(regResults$coefficients['sum_tot_dur'], regResults$coefficients['avg_daily_cmts'], 
                 regResults$coefficients['time_to_trial'], regResults$coefficients['avg_daily_admins']), 
                 regResults$coefficients['avg_daily_cnvs']), ncol=1) + regResults$coefficients[1]
      
      strVal <- exp(strVal)/(1 + exp(strVal));
      
      #     newdata = data.frame(sum_tot_dur = data$sum_tot_dur[i], avg_daily_cmts = data$avg_daily_cmts[i], avg_daily_mails = data$avg_daily_mails[i], 
      #                          time_to_trial = data$time_to_trial[i], avg_daily_admins = data$avg_daily_admins[i]);
      #      prb = predict(regResults,newdata,type="response");  
      
      predict[i] <- ifelse(strVal > j, 1, 0);
    }
#     browser()
    data <- cbind(data, predict);
    tot_true  <- sum(ifelse (data$predict == data$bin_val, 1,0))/dim(data)[1];
    tot_false <- 1 - tot_true;
    true_pos[int_j]  <- (data$bin_val %*% data$predict)/dim(data)[1];
    true_neg[int_j]  <- tot_true - true_pos[int_j];
    false_pos[int_j] <- ((1 - data$bin_val) %*% data$predict)/dim(data)[1];
    false_neg[int_j] <- tot_false - false_pos[int_j];
    
    data <- data[,!names(data) %in% c('predict')];              # Drop columns
    int_j = int_j + 1;
    #i = 1;
  }
  
  conMat <- cbind(true_pos, true_neg, false_pos, false_neg);
  return(conMat);
}



