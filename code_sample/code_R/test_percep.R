
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


rm(list = ls(all = TRUE))  # clear all.
graphics.off()             # close all.

tot_itr <- 100             # Total no. iterations.
store_prb <- as.data.frame(matrix(NA, tot_itr, 5))
colnames(store_prb) <- c("x1_value", 
                         "x2_value", 
                         "y_value", 
                         "classify", 
                         "verify")


# ===== Construct data ====
no_pts <- 10

# ----- Random data pts. for the separating line ---
pt_a <- runif(2, -1, 1)
pt_b <- runif(2, -1, 1)

# ----- Plot the data pts. & separating line ---
plot(-1:1, -1:1, 'n')
points(pt_a, pt_b, type = 'n')  # Plot data pts.
fit <- lm( pt_b ~ pt_a)
abline(lm(pt_b~pt_a), col = 'blue')          # Plot Separating line.

pts <- as.data.frame(matrix(NA, no_pts, 4))  # Data frame.
colnames(pts) <- c("x1_value",
                   "x2_value",
                   "y_value",
                   "classify")

# --- Generate the sample data pts. --- 
pts$x1_value <- runif(no_pts, -1, 1)
pts$x2_value <- runif(no_pts, -1, 1)
# Assign signs (+ve above the line).
pts$y_value <- sign(pts$x2_value - 
                  (fit$coefficients[2] * pts$x1_value + fit$coefficients[1]))

# ----- Plot the sample data ---
up  <- subset(pts, pts$y_value == 1)
dwn <- subset(pts, pts$y_value == -1)
points(up$x1_value, up$x2_value, col = 'green')
points(dwn$x1_value, dwn$x2_value, col = 'red')

# ===== Learning =====
source('~/myGitCode/ML/homeWorks/homeWork1/percepAlgo.R')
val <- percepAlgo(pts)            # Perceptron Learning Algo. - parse data frame of sample pts. and signs.
cat("Weights: ", val[[1]],"\n")   # Computed weights.
w <- val[[1]]

for (j in 1:tot_itr){
  store_prb[j, 1:2] <- runif(2, -1, 1)    # Out-of-sample pts.
  store_prb$y_value[j] <- sign(store_prb$x2_value[j] - 
                          (fit$coefficients[2]*store_prb$x1_value[j] + fit$coefficients[1])) # Assign Sign (+ve above).
  
  store_prb$classify[j] <- sign(c(1, 
                                  store_prb$x1_value[j], 
                                  store_prb$x2_value[j]) %*% w)    # Estimate Sign.
  
  store_prb$verify[j] <- as.numeric(store_prb$y_value[j] == store_prb$classify[j])           # Check Sign.
}

prb <- 1-sum(store_prb$verify)/tot_itr # Percentage of mis classification.
cat("Percentage of mis-classification: ", prb, "%\n")
avIte <- val[[3]] # Av. iterations to converge.
cat("Average no. iterations to converge: ", avIte)
