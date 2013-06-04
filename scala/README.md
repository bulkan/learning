
Regular Expressions 
===================

You can convert any String into a regex by calling .r on it

```
scala> var reg = """(bulkan.*)"""
reg: java.lang.String = (bulkan.*)

scala> reg.r
res0: scala.util.matching.Regex = (bulkan.*)

scala>
```


var vs val
==========

var is to define mutable variables and val is for immutables (constants). Try to use var if possible as it 
helps with concurency later on.


Notes
=====

foldLeft is like the bread and butter ? for terse Scala code that deals with collections
