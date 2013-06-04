object Main {
  def main(args: Array[String]) {
    var myStrings = Array("bulkan", "savun", "evcimen")

    if (args.length > 0) {
      myStrings = args
    }

    print("Given strings: ")
    myStrings.foreach(s => print(s + ", "))

    // Using foldLeft to calculate sum strings in List
    var stringSum = myStrings.foldLeft(0)((sum, value) => sum + value.length)
    println()
    println("Sum of strings: " + stringSum)
  }
}
