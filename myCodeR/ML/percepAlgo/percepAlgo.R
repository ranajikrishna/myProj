percepAlgo <- function(pts){
  
# ------ Notes ------
#   Name: The Perceptron Learning Algo. 
#   Author: Ranaji Krishna.

#   Input: Data frame [n X 4] containing x-values, y-values, classification signs 
#          and estimated classification signs.
   
#   Output: Weights, No. iterations to converge and data frame with estimated 
#           classification signs populated.
# ----------
  
  w <- c(0,0,0);    # Initialise Weights.
  k <- 0;           # No. iterations.
  error <- TRUE;    # Track miss classification.
  
  while (error){
    error <- FALSE;
    pts$est <- apply(pts,1, function(x) sign(c(1,x[1:2]) %*% w));     # Compute estimated classification using weights.
    
    for(i in 1:nrow(pts)){
      if (pts$sign[i] != pts$est[i]){                                 # Check for mis classification.
        w <- w + pts$sign[i] * c(1, pts$x_value[i], pts$y_value[i]);  # Update weights.
        k <- k + 1;       # Iteration.
        error <- TRUE;    # For next iteration to pass.
      }
    }
  } 
  return (list(w,pts,k));
}