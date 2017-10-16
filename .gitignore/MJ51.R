#Makeda Joseph
#05/01/2017


list.files("nycHistPop.csv")
help("read.csv")
pop <- read.csv("~/Desktop/nycHistPop.csv", skip=5)
barplot(names=pop$Year, pop$Bronx)
mean(pop$Bronx)
print(pop)
help(mean)
mean(pop$Bronx, na.rm = TRUE)
m <- mean(pop$Bronx, na.rm = TRUE)
abline(h = m)