#Makeda Joseph
#05/08/2017






plot(cars, main="Cars Data from 1920's", xlab="Speed", ylab="Stopping Distance")
title(main = "Speed verses Stopping Distance")
m <- mean(cars$dist, na.rm = TRUE)
abline(h = m)