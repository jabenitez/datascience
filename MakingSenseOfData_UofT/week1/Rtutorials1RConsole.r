
R version 2.15.2 (2012-10-26) -- "Trick or Treat"
Copyright (C) 2012 The R Foundation for Statistical Computing
ISBN 3-900051-07-0
Platform: x86_64-apple-darwin9.8.0/x86_64 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

[R.app GUI 1.53 (6335) x86_64-apple-darwin9.8.0]

> setwd("/Users/benitez/learn/coursera/statistics/week1")
> data = read.table('LifeExpRegion.txt')
> region = data[,3]
> table(region)
region
Amer  EAP EuCA MENA  SAs  SSA 
  39   30   50   21    8   49 
> counts = table(region)
> relfreq = counts/sum(counts)
> region_names = c("Americas", "E.Asia&Pc", "Eur&C.As", "M.E&N.Afr",
+ "S.Asia", "S-S.Africa") 
> barplot(counts, col=rainbow(6), names.arg = region_names, main = "World Regions: Bar Chart")
> barplot(relfreq, col=rainbow(6), names.arg = region_names, main = "World Regions: Relative Frequencies")
> pie(counts, col=rainbow(6), label = region_names, main = "World Regions: Pie Chart")
> 
> 
> 
> skeleton = read.table('SkeletonData.txt', header=TRUE)
> attach(skeleton)
> sex_counts = table(Sex)
> sex_freq = sex_counts/sum(sex_counts)
> sex_names = c('Male', 'Female')
> barplot(sex_counts, col=rainbow(2), names.arg = sex_names, main='Skeleton Sex Bar Chart')
> barplot(sex_freq, col=rainbow(2), names.arg = sex_names, main='Skeleton Sex Relative Frequencies')
> pie(sex_counts, col=rainbow(2), label=sex_names, main='Skeleton Sex Main Pie Chart')
> BMI_counts = table(BMI)
> BMI_freq = BMI_counts/sum(BMI_counts)
> BMI_names = c('Normal', 'Obese', 'Overweight', 'Underweight')
> barplot(BMI_counts, col=rainbow(4), names.arg=BMI_names, main='Skeleton Mass Category Bar Chart')
> barplot(BMI_freq, col=rainbow(4), names.arg=BMI_names, main='Skeleton Mass Category Relative Frequencies')
> pie(BMI_counts, col=rainbow(4), label=BMI_names, main='Skeleton Mass Category Pie Chart')
> 