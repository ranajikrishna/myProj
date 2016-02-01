
#
# Author: Ranaji Krishna
# Date: October 9 2015.
# Notes: The code was developed for the following problem:
#
# Assume that we have a data matrix X with the following model:
#                   X = As * Bs * T + An * Bn * T + Z
# where,
#   * X is a real m×n matrix.
#   * Z isarealm×narei.i.dsamplesofazeromeanGaussianprocess∼N(0,σ). An is an unknown m × d 
#     matrix, where we do not know the exact value of d, but d << m,n.
#   * Bn is an unknown n × d matrix.
#   * As is an unknown m × q matrix, where q is known, and q << m,n. Also we know that each 
#     column of As is in the column span of a known matrix S.
#   * Bs is an unknown n×q matrix. But we know that each row of Bs has at most one non-zero element.
#   * It is assumed that span(An) ̸⊂ span(As).
# 
# The goal is to find a computation efficient method to estimate As and Bs.
# Show the performance of their algorithm, with the following simulation parameters:
#         • Entries of As are derived from the class of random staircase functions, of integer 
#           step heights , and width 32. In the Matlab notation: 
#                       kron(randi(8, m/32, 1), ones(32, 1))
#         • Rows of Bs are zero except for possibly one random location where it is one.
#         • Entries of Bn are i.i.d samples from a Gaussian process of a given variance.
#         • Columns of An are random traces of a random walk process.
#         • m=256,q=4,d=16,n=1024.
# Simulations results should show the sensitivity of the proposed solution with respect to variance 
# of entries of An , the variance of Z. Additionally, it will be interesting to show simulation results 
# for sensitivity with d and q.

# ---------- #


rm(list = ls(all = TRUE));  # clear all.
graphics.off();             # close all.


# --- Initializing variables ----
m <- 256
q <- 4
d <- 16
n <- 1024 
sigma2 <- c(0.01, 0.1, 0.5, 0.9, 1, 1.3)  # Different variances.
# qVal <- seq(2,7)                        # Values of q.
# dVal <- seq(14,18)                      # Values of d.
sigma2_An <- 0.01                         # Variance in An.
sigma2_Bn <- 0.01                         # Variance in Bn.
sigma2_Z <- 1                             # Varience in Z.
# ------

N = 100                                              # Number of iterations.
rms <- matrix(0, N, length(sigma2))                  # Store Root-Mean-Square (rms) for N iterations.
all_rms <- matrix(0, length(sigma2), length(sigma2)) # Store rms for different variances.

itr_varZ <- 0
itr_varA <- 0
for (sigma2_An in sigma2){     # Iterate for variance in An.
  
  itr_varA <- itr_varA + 1     # Count for variance in An.
  
  for (sigma2_Z in sigma2) {   # Iterate for variance in Z.
    
    itr_varZ <- itr_varZ + 1   # Count for variance in Z.
    
    for (itr in seq(1, N)){
      
      # Create matrix As.
      As <- apply(as.array(seq(1, q)), 1, 
            function(x) kronecker(runif(m/32, 1, 8), rep(1, 32)))     
      
      # Create matrix Bs.
      Bs <- t(apply(as.array(seq(1, n)), 
            1, 
            function(x) rev(as.integer(intToBits(sample(c(0, 2^(seq(0, (q-1)))))[3])))[(32-q+1): 32]))
      
      Q <- As%*%t(Bs)         # Actual matrix for performance comparison.
      
      
      x0 <- cumsum(c(0, rnorm(m*d*2, 0, sigma2_An)))                 # Simulate Random Walk.
      rand_trace <- as.array(sample(seq(1, length(x0)-m+1))[1:d])    # Random trace initiliaze.
      An <- apply(rand_trace, 1, function(x) x0[x:(x+m-1)])          # Create matrix An.
      
      # Create Matrix Bn
      Bn <- apply(as.array(seq(1, d)), 1, function(x) rnorm(n, 0, sigma2_Bn)) 
      
      #set.seed(4*itr)
      Z <- matrix(rnorm(n*m, 0, sigma2_Z), nrow = m)      # Compute matrix Z.
      X = As%*%t(Bs) + An%*%t(Bn) + Z                     # Compute matrix X.
      
      svd1 <- svd(X)                      # Singular Value Decomposition.
      U <- svd1$u                         # Matrix U.
      D <- svd1$d                         # Matix D.
      V <- svd1$v                         # Matrix V.
      As_sv <- U[,1:q] %*% diag(D[1:q])   # Estimated matrix As.
      Bs_sv <- V[,1:q]                    # Estimated matrix Bs.
      Q_sv  <- As_sv%*%t(Bs_sv)           # Estimated matrix Qs  for performance comparison.
      
      rms[itr, itr_varZ] <- sqrt(sum((Q-Q_sv)^2))/(n*m)     # Root-Mean-Square (rms).
    }
    
  }
  all_rms [itr_varA,] <- colMeans(rms)    # Store rms.
  itr_varZ <- 0
}

# ----- Save variables ----
# save(pVal, file="pval_An.Rda")
# save(xSqr, file="xsqr_An.Rda")
# save(rms, file="rms_An.Rda")
# save(rms, file="rms_Z.Rda")
# save(rms, file="rms_q.Rda")
# save(rms, file="rms_d.Rda")
# save(all_rms, file="all_rms.Rda")



# ==== Plots ==== 
setwd('/Users/vashishtha/myGitCode/')                       # Set directory

pdf("sen_A.pdf")
ggplot(data.frame(all_rms[, 1], all_rms[, 2], all_rms[, 3], all_rms[, 4], all_rms[, 5], all_rms[, 6]), aes(sigma2, colour=)) + 
  geom_line(aes(y=all_rms[, 1], color = "Var. Z = 0.01")) + 
  geom_point(aes(y=all_rms[, 1], color ="")) +
  geom_line(aes(y=all_rms[, 2], color ="Var. Z = 0.10")) + 
  geom_point(aes(y=all_rms[, 2], color ="")) +
  geom_line(aes(y=all_rms[, 3], color ="Var. Z = 0.50")) + 
  geom_point(aes(y=all_rms[, 3], color ="")) +
  geom_line(aes(y=all_rms[, 4], color ="Var. Z = 0.90")) + 
  geom_point(aes(y=all_rms[, 4], color ="")) +
  geom_line(aes(y=all_rms[, 5], color ="Var. Z = 1.0")) + 
  geom_point(aes(y=all_rms[, 5], color ="")) +
  geom_line(aes(y=all_rms[, 6], color ="Var. Z = 1.3")) + 
  geom_point(aes(y=all_rms[, 6], color ="")) +
  scale_color_manual(values=c("black","red","blue","magenta","dark green","yellow", "brown")) +
  labs(x=expression('Variance of A'["n"]), y="rms") + 
  ggtitle(bquote('Sensitivity to '*A[n]*' '))
dev.off()


pdf("sen_Z.pdf")
ggplot(data.frame(all_rms[, 1], all_rms[2, ], all_rms[3, ], all_rms[4, ], all_rms[5, ], all_rms[6, ]), aes(sigma2, colour=)) + 
  geom_line(aes(y=all_rms[1, ], color = 'Var. An = 0.01')) + 
  geom_point(aes(y=all_rms[1,], color ="")) +
  geom_line(aes(y=all_rms[2, ], color ="Var. An = 0.10")) + 
  geom_point(aes(y=all_rms[2, ], color ="")) +
  geom_line(aes(y=all_rms[3, ], color ="Var. An = 0.50")) + 
  geom_point(aes(y=all_rms[3, ], color ="")) +
  geom_line(aes(y=all_rms[4, ], color ="Var. An = 0.90")) + 
  geom_point(aes(y=all_rms[4, ], color ="")) +
  geom_line(aes(y=all_rms[5, ], color ="Var. An = 1.0")) + 
  geom_point(aes(y=all_rms[5, ], color ="")) +
  geom_line(aes(y=all_rms[6, ], color ="Var. An = 1.3")) + 
  geom_point(aes(y=all_rms[6, ], color ="")) +
  scale_color_manual(values = c("black", "red", "blue", "magenta", "dark green", "yellow", "brown")) +
  labs(x=expression('Variance of Z'), y = "rms") + 
  ggtitle(bquote('Sensitivity to Z'))
dev.off()



pdf("signal.pdf")
ggplot(data.frame(X[, 10]), aes(seq(1, m), colour=)) + 
  geom_line(aes(y = X[,10], color = "Signal")) + 
  scale_color_manual(values = c("black")) +
  labs(x= "Count", y = "Value") + 
  ggtitle("Signal") + 
  theme(plot.title = element_text(size=14)) + 
  annotate("text", x=200, y=1, label = "sigma[Z]^2 == 1", col = "black", fontsize=2, fontface = "italic", parse=T) +
  annotate("text", x=209, y=0, label = "sigma[A[n]]^2 == 0.01" , col = "black", fontsize=2, fontface = "italic", parse=T)
dev.off()


pdf("svd_perf.pdf")
ggplot(data.frame(Q[, 10], Q_sv[, 10]), aes(seq(1, m), colour=)) + 
  geom_line(aes(y = Q[,10], color = "Actual")) + 
  geom_line(aes(y = Q_sv[, 10], color = "Estimated")) + 
  scale_color_manual(values = c("black", "red")) +
  labs(x = "Count", y = "Value") + 
  ggtitle("Actual Vs Estimated")  + 
  annotate("text", x=200, y=1, label = "RMS = 1.25e-2", col = "black", fontsize=2, fontface = "italic")
dev.off()


pdf("sen_q.pdf")
load("rms_q.Rda")
ggplot(data.frame(colMeans(rms)), aes(seq(2, 7), colour=)) + 
  geom_line(aes(y = colMeans(rms), color ="")) + 
  geom_point(aes(y = colMeans(rms), color ="")) +
  scale_color_manual(values = c("black")) +
  labs(x = "q", y = "Rms") + 
  annotate("text", x=5, y=0.00025, label = "sigma[A[n]]^2==0.01", col="black", fontsize=2, fontface="italic", parse=T) +
  annotate("text", x=4.8, y=0.000235, label = "sigma[Z]^2==1", col="black", fontsize=2, fontface="italic", parse=T) +
  ggtitle(bquote('Sensitivity to q'))
dev.off();


pdf("sen_d.pdf")
load("rms_d.Rda")
ggplot(data.frame(colMeans(rms)), aes(seq(14, 18), colour=)) + 
  geom_line(aes(y = colMeans(rms), color ="")) + 
  geom_point(aes(y = colMeans(rms), color ="")) +
  scale_color_manual(values = c("black")) +
  labs(x="d", y="Rms") + 
  annotate("text", x=17.5, y=0.0002775, label = "sigma[A[n]]^2 == 0.01", col = "black", fontsize=2, fontface = "italic", parse = T) +
  annotate("text", x=17.4, y=0.000277, label = "sigma[Z]^2 == 1", col = "black", fontsize=2, fontface = "italic", parse = T) +
  ggtitle(bquote('Sensitivity to d'))
dev.off();


pdf("com_perf.pdf")
k = 10
ggplot(data.frame(Q[, k], Q_sv[, k]), aes(seq(1, m), colour=)) + 
  geom_line(aes(y = Q[,k], color = "Actual")) + 
  geom_line(aes(y = Q_sv[,k], color = "SVD")) + 
  scale_color_manual(values = c("black", "red", "blue","green")) +
  labs(x = "Count", y = "Value") + 
  ggtitle("Actual Vs Estimated")  + 
  annotate("text", x=200, y=1, label = "RMS = 1.25e-2", col = "black", fontsize=2, fontface = "italic")
dev.off()


pdf("sample_graph.pdf")
par(mfrow = c(4,1)) 
p1 <- plot(An%*%t(Bn)[,1], t="l")
p2 <- plot(As%*%t(Bs)[,1], t="l")
p3 <- plot(Z[, 1], t = "l")
p4 <- plot(X[, 1], t = "l")
p5 <- plot(X[, 1]-(An%*%t(Bn))[, 1],t="l")
dev.off()


pdf("SVD_perf.pdf")
for (k in seq(1,m)){
  p <- ggplot(data.frame(Q[, k], Q_sv[, k]), aes(seq(1, m), colour =)) + 
    geom_line(aes(y=Q[, k], color = "Actual")) + 
    geom_line(aes(y=Q_sv[, k], color = "SVD")) + 
    scale_color_manual(values = c("black", "red")) +
    labs(x = "Count", y = "Value") + 
    ggtitle("Actual Vs Estimated")  + 
    annotate("text", x=200, y=1, label = "RMS=1.25e-2", col="black", fontsize=2, fontface="italic")
  print(p)
}
dev.off()

