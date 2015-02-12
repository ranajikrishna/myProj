
#   Name:   Testing the Perceptron Learning Algo.
#   Author: Ranaji Krishna.
#
#   Notes:  The code tests the PL algo. by creating and 
#           random data pts. and tagging them as +1 and -1.
#           It then calls the PLA fxn. "percepAlgo" to classify the
#           points as +ve or -ve.
#
#           The dataframe "pts" contains the x- and y- coordinates of 
#           the points, the sign assigned to the point (+ve or -ve) and
#           the classification estimated using the PLA. Out-of-sample points are
#           generated, signed and classified. 
#
# ----------


rm(list = ls(all = TRUE));  # clear all.
graphics.off();             # close all.

tot_itr <- 100;             # Total no. iterations.
store_prb <- as.data.frame(matrix(NA,tot_itr, 5));
colnames(store_prb) <- c("x_value","y_value","sign","est","check");


# ===== Construct data ====
no_pts <- 100;

# ----- Random data pts. for the separating line ---
pt_a <- runif(2,-1,1);
pt_b <- runif(2,-1,1);

# ----- Plot the data pts. & separating line ---
plot(-1:1,-1:1,'n');
points(pt_a,pt_b,type ='n');  # Plot data pts.
fit <- lm( pt_b ~ pt_a);
abline(lm(pt_b~pt_a),col ='blue');          # Plot Separating line.

pts <- as.data.frame(matrix(NA,no_pts,4));  # Data frame.
colnames(pts) <- c("x_value","y_value","sign","est");

# --- Generate the sample data pts. --- 
pts$x_value <- runif(no_pts,-1,1);
pts$y_value <- runif(no_pts,-1,1);
# Assign signs (+ve above the line).
pts$sign <- sign(pts$y_value - (fit$coefficients[2] * pts$x_value + fit$coefficients[1]));

# ----- Plot the sample data ---
up  <- subset(pts,pts$sign==1);
dwn <- subset(pts,pts$sign==-1);
points(up$x_value,up$y_value,col='green');
points(dwn$x_value,dwn$y_value,col='red');

# ===== Learning =====
source('~/myGitCode/ML/homeWorks/percepAlgo.R');
val <- percepAlgo(pts); # Perceptron Learning Algo. - parse data frame of sample pts. and signs.
cat("Weights: ", val[[1]],"\n");        # Computed weights.
w <- val[[1]];

for (j in 1: tot_itr){
  store_prb[j,1:2] <- runif(2,-1,1);      # Out-of-sample pts.
  store_prb$sign[j] <- sign(store_prb$y_value[j] - (fit$coefficients[2] * store_prb$x_value[j] + fit$coefficients[1])); # Assign Sign (+ve above).
  store_prb$est[j] <- sign(c(1,store_prb$x_value[j],store_prb$y_value[j]) %*% w); # Estimate Sign.
  store_prb$check[j] <- as.numeric(store_prb$sign[j] == store_prb$est[j]);        # Check Sign.
}

prb <- 1- sum(store_prb$check)/tot_itr; # Percentage of mis classification.
cat("Percentage of mis-classification: ", prb, "%\n");
avIte <- val[[3]]; # Av. iterations to converge.
cat("Average no. iterations to converge: ",avIte);
