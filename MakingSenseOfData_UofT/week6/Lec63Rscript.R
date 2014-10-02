#Set working directory
setwd('/Users/benitez/Dropbox/coursera/statistics/week6')

#Read data
skeleton = read.table('SkeletonsMatchedPairsData.txt', header=T)

#Attach variable names
attach(skeleton)

#Take a look at the first few observations
head(skeleton)

mydifference = SucheyBrooksError - DiGangiError
cbind(mydifference, Difference)
mydifference == Difference

mean(Difference, na.rm=T) #na.rm=T removes NA from the dataset
sd(Difference, na.rm=T)

#One sample t-test on the differences
t.test(Difference, mu=0, alternative='two.sided')

#Two sample paired t-test
t.test(SucheyBrooksError, DiGangiError, paired=T, mu=0, alternative='two.sided')