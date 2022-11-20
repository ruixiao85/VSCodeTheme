# Header1
## Header2
### Header3
#### Header4
##### Header5
###### Header6
paragraph
* point1 **bold**
	* point2 *italics*
		* point3 ***Italic and Bold Text***
			* point4 ~~Strikethrough~~

* [Python example](https://www.listendata.com/2019/08/python-object-oriented-programming.html)
```python
class Vehicle:
    minimumrate = 50
    def __init__(self,driver,wheels,seats,kms,bill):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats
        self.running = kms
        self.bill = bill

    def rateperkm(self):
        return self.bill/self.running

class Cab(Vehicle):
    minimumrate = 75
    def __init__(self,driver,wheels,seats,kms,bill,cabtype):
        Vehicle.__init__(self,driver,wheels,seats,kms,bill)
        self.category = cabtype


class Bus(Vehicle):
    minimumrate = 25
    def __init__(self,driver,wheels,seats,kms,bill,color):
        Vehicle.__init__(self,driver,wheels,seats,kms,bill)
        self.color = color

if __name__ == "__main__":
    cab_1 = Cab('Prateek', 4, 3, 50, 700, 'SUV')
    cab_1.category
    cab_1.rateperkm()

    bus_1 = Bus('Dave', 4, 10, 50, 400, 'green')
    bus_1.color
    bus_1.rateperkm()
```

* [R example](https://www.datamentor.io/r-programming)
```R
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
```

* [json example](https://json.org/example.html)
```json
{
  "glossary": {
    "title": "example glossary",
    "GlossDiv": {
      "title": "S",
      "GlossList": {
        "GlossEntry": {
          "ID": "SGML",
          "SortAs": "SGML",
          "GlossTerm": "Standard Generalized Markup Language",
          "Acronym": "SGML",
          "Abbrev": "ISO 8879:1986",
          "GlossDef": {
            "para": "A meta-markup language, used to create markup languages such as DocBook.",
            "GlossSeeAlso": ["GML", "XML"]
          },
          "GlossSee": "markup"
        }
      }
    }
  }
}
```

* [SQL example](https://www.sqlshack.com/learn-sql-sql-query-examples/)
```sql
-- the difference between AVG call duration per employee and AVG call duration
SELECT
  single_employee.id,
  single_employee.first_name,
  single_employee.last_name,
  single_employee.call_duration_avg,
  single_employee.call_duration_avg - avg_all.call_duration_avg AS avg_difference
FROM (
  SELECT
    1 AS join_id,
    employee.id,
    employee.first_name,
    employee.last_name,
    AVG(DATEDIFF("SECOND", call.start_time, call.end_time)) AS call_duration_avg
  FROM call
  INNER JOIN employee ON call.employee_id = employee.id
  GROUP BY
    employee.id,
    employee.first_name,
    employee.last_name
) single_employee
INNER JOIN (
  SELECT
    1 AS join_id,
    AVG(DATEDIFF("SECOND", call.start_time, call.end_time)) AS call_duration_avg
  FROM call
) avg_all
ON avg_all.join_id = single_employee.join_id;
```

* [makefile example](https://makefiletutorial.com/)
```makefile
files := file1 file2
some_file: $(files)
	echo "Look at this variable: " $(files)
	touch some_file
file1:
	touch file1
file2:
	touch file2
clean:
	rm -f file1 file2 some_file
```