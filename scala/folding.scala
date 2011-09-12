object Main {
  def main(args: Array[String]) {
    var myStrings = List("bulkan", "savun", "evcimen")
    var stringSum = myStrings.foldLeft(0)((sum, value) => sum + value.length)
    println("Sum of strings: " + stringSum)

  }
}
