# Header1 [Example](https://www.com)
* Point1 **Bold**
	+ Point2 *Italics*
		- Point3 ***Italic and Bold Text***
			1. Point4 ~~Strikethrough~~
```python
class Cab(Vehicle):
  def __init__(self, driver, wheels):
    Vehicle.__init__(self, driver, wheels, welcome=None, rate=None)
    if welcome: welcome(driver)
    self.rate=rate if rate else 75 # set default rate
if __name__ == "__main__":
  cab_1 = Cab('David', 4, lambda x:print(f"Hi, I'm Cab Driver {x}!"), rate=80)
```
```sql
SELECT employee.id
  ,AVG(DATEDIFF("SECOND", record.start_time, record.end_time)) AS record_duration_avg
FROM record
INNER JOIN employee ON record.employee_id = employee.id
GROUP BY employee.id -- average within employee id
```
```R
studentR<-setRefClass("studentR",
  fields=list(name="character", age="numeric"),
  methods=list(inc_age=function(x) { age <<- age+x; cat("age+:",age,"\n") })
)
sR<-studentR(name="John", age=21)
```
```json
{ "glossary": {
    "title": "example",
    "list": ["abc", "glossary"]
}}
```
```html
<!DOCTYPE html><html>
<head>
  <style> p { color: red; font-size: 160%; } </style>
  <script type = "text/javascript">
    const handler = { set: () => console.log('set something!') };
    const person = new Proxy({}, handler);
  </script>
</head>
<body><h1>A heading</h1></body>
</html>
```
```makefile
files := file1
some_file: $(files)
	echo "Look at this variable: " $(files)
	touch some_file
```