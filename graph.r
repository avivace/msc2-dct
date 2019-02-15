library(ggplot2)
setwd('~/uni/mcs/mcs2-jpg/')
dataset = read.csv('times.csv', sep=",", fileEncoding="latin1")
dataset_scipy = read.csv('times_scipy.csv', sep=",", fileEncoding="latin1")

dataset$scipyTime = dataset$scipyTime*250
fun.1 <- function(x) x^2 + x

 

a = ggplot() + geom_line(data=dataset, aes(x = n, y= myTime), color="red") +
           geom_line(data=dataset, aes(x = n, y= scipyTime), color="darkgreen") +
           geom_smooth(data=dataset, aes(x = n, y= scipyTime), method = "lm") +
           ylab("Time(s)") + xlab("Size") +
           stat_function(fun=function(x)x^3/400000, geom="line", aes(colour="x^3/ 4*10^6"))

           #ylim(0, 5)

      

b = ggplot() + geom_line(data=dataset_scipy, aes(x = n, y= scipyTime), color="darkgreen") +
         stat_function(fun=function(x)log(x), geom="line", aes(colour="log(x)"))
#ylim(0, 5)

a
