

data<-read.csv("Restaurants.csv",sep = ",",header = T)

summary(data)
str(data)

quantile(data$councilDistrict,na.rm = T)

quantile(data$councilDistrict,probs = c(0.5,0.75,0.9))

#added na column
table(data$zipCode,useNA = "ifany")

#2d tables
table(data$zipCode,data$councilDistrict)


sum(is.na(data$councilDistrict))
any(is.na(data$councilDistrict))


all(data$zipCode>0)


#row and col sums

colSums(is.na(data))

all(colSums(is.na(data))==0)



#value with specific char

sum(data$zipCode=="21212")

table(data$zipCode%in%c("21212"))

#21212 or 21213
table(data$zipCode%in%c("21212","21213"))

#subset
data[data$zipCode%in%c("21212","21213"),]



#cross tabs

data("UCBAdmissions")
df=as.data.frame(UCBAdmissions)
summary(df)


xt<-xtabs(Freq~Gender+Admit,data = df)
xt

warpbreaks$replicate<-rep(1:9,len=54)
xt<-xtabs(breaks~.,data=warpbreaks)
xt
