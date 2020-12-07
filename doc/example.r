## https://www.datamentor.io/r-programming


# Reference Class
studentR<-setRefClass("studentR",
  fields=list(name="character", age="numeric", GPA="numeric"),
  methods=list( # non-local assignment operator <<-
    inc_age=function(x) { age <<- age+x; cat("age up:",age,"\n") },
    dec_age=function(x) { age <<- age-x; cat("age down:",age,"\n") }
  )
)
sR2<-sR<-studentR(name="John", age=21, GPA=3.5)
sR$name<-"Jay"; print(sR2$name) # "John" -> "Jay"
sR$inc_age(5) # 21 -> 26
sR$dec_age(50) # set to negative age

studentRintl <- setRefClass("studentRintl",
  contains="studentR",
  fields=list(country="character"),
  methods=list(
    dec_age = function(x) { # override base class
      if ((age - x)<0) stop("Age cannot be negative")
      age <<- age-x; cat("age down:",age,"\n")
    }
  )
)
(sRi<-studentRintl(name="Daniel", age=21, GPA=3.5, country="Finland"))
sRi$dec_age(5)
sRi$dec_age(50)

# S3 class
student3<-function(name,age,gpa){
  value<-list(name=name,age=age,GPA=gpa)
  class(value)<-"student3"
  return(value)
}
print.student3<-function(o){
  cat("Name:", o$name, "\n")
  cat("Age:", o$age, "years old\n")
  cat("GPA:", o$GPA, "\n")
}
student3intl<-function(name,age,gpa,country){
  value<-student3(name,age,gpa)
  value[["country"]]=country
  class(value) <- c("student3intl","student3")
  return(value)
}
s3=student3intl("Jane", 29, 4.0, "French")
s3 # call print.student3(), country not printed
print.student3intl<-function(object){
  print.student3(object)
  cat("Country:", object$country, "\n")
}
s3 # call print.student3intl(), country printed


# S4 class
print.student4<-function(object) {
  cat("Name:", object@name, "\n")
  cat("Age:", object@age, "years old\n")
  cat("GPA:", object@GPA, "\n")
}
student4<-function(name,age,gpa){
  setClass("student4", slots=list(name="character", age="numeric", GPA="numeric"))
  setMethod("show", "student4", print.student4)
  return(new("student4",name=name,age=age,GPA=gpa))
}
(s4<-student4("John", 25, 3.5)) # print 3 rows
print.student4intl<-function(object) {
  print.student4(object)
  cat("Country:", object@country, "\n")
}
student4intl<-function(name,age,gpa,country){
  setClass("student4intl", contains="student4", slots=list(country="character"))
  setMethod("show", "student4intl", print.student4intl)
  return(new("student4intl",name=name,age=age,GPA=gpa,country=country))
}
(s4i<-student4intl("John", 25, 3.5, "UK")) # print 4 rows

