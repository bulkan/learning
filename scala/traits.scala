trait Censor  {
  val wordPairs = HashMap(
      "Shoot" -> "Pucky",
      "Darn" -> "Beans"
  )
 
  def replaceWords(words: String): String = {
    wordPairs.foldLeft(words)((replaced, m) =>
        replaced.replaceAllLiterally(m._1, m._2)
      )
  }
}

class CensoredStrings(var s: String) extends Censor {
  def getString() = this.s
  def getReplacedString() = this.replaceWords(this.getString)
}

var cs = new CensoredStrings("Scala is Darn cool you know! Shoot this is nice")
println("Original: " + cs.getString)
println("Replaced: " +cs.getReplacedString)