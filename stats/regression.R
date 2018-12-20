#Cartpole

#Read Data
rl_data <- read.csv('../output_data/CartPole-v0.csv')
rl_data$X <- NULL

#Regression Model
model <- lm(BEST_DURATION ~ MEAN_TD_ERROR + MEAN_CORRELATION + MEAN_TD_ERROR*MEAN_CORRELATION, data=rl_data) 
summary(model)

#Acrobot-v1
#Read Data
rl_data <- read.csv('../output_data/Acrobot-v1.csv')
rl_data$X <- NULL

#Regression Model
model <- lm(BEST_DURATION ~ MEAN_TD_ERROR + MEAN_CORRELATION + MEAN_TD_ERROR*MEAN_CORRELATION, data=rl_data) 
summary(model)


#MountainCar-v0
#Read Data
rl_data <- read.csv('../output_data/MountainCar-v0.csv')
rl_data$X <- NULL

#Regression Model
model <- lm(BEST_DURATION ~ MEAN_TD_ERROR + MEAN_CORRELATION + MEAN_TD_ERROR*MEAN_CORRELATION, data=rl_data) 
summary(model)


