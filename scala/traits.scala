//import scala.collection.mutable.ArrayBuffer

trait Censor  {
  val wordPairs = Map(
      "Shoot" -> "Pucky",
      "Darn" -> "Beans"
  )
 
  def replaceWords(words: String): String = {
    /*
    wordPairs.foldLeft(words)((replaced, m) =>
        replaced.replaceAllLiterally(m._1, m._2)
      )*/
    words.split(" ").map(word => 
      wordPairs.getOrElse(word, word) 
    ) mkString(" ")

  }
}

class CensoredStrings(var s: String) extends Censor {
  def getString() = s
  def getReplacedString() = this.replaceWords(this.getString)
}

var cs = new CensoredStrings("Scala is Darn cool you know! Shoot this is nice")
println("Original: " + cs.getString)
println("Replaced: " +cs.getReplacedString)
