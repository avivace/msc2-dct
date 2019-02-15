library(ggplot2)
setwd('~/uni/mcs/mcs2-jpg/')
dataset = read.csv('times.csv', sep=",", fileEncoding="latin1")
dataset_scipy = read.csv('times_scipy.csv', sep=",", fileEncoding="latin1")

dataset$scipyTime = dataset$scipyTime*250
fun.1 <- function(x) x^2 + x

 

a = ggplot() + geom_line(data=dataset, aes(x = n, y= myTime), color="red", size=1) +
           geom_line(data=dataset, aes(x = n, y= scipyTime), color="darkgreen", size=1) +
           geom_smooth(data=dataset, aes(x = n, y= scipyTime), method = "lm") +
           ylab("Time(s)") + xlab("Size") +
           stat_function(fun=function(x)x^3/400000, geom="line", aes(colour="x^3/ 4*10^6"), size=1) +
           theme(text = element_text(size=20))

           #ylim(0, 5)

      

b = ggplot() + geom_line(data=dataset_scipy, aes(x = n, y= scipyTime), color="darkgreen",size=1) +
         stat_function(fun=function(x)log(x)*x^2/200000000, geom="line", aes(colour="log(x)*x^2/ 2*10^10"),size=1) +
  ylab("Time(s)") + xlab("Size")+
  theme(text = element_text(size=20))
#ylim(0, 5)

a
b