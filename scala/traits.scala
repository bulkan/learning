import scala.collection.mutable.ArrayBuffer

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

    var replaced = new ArrayBuffer[String]
    words.split(" ").map(word => {
        if (wordPairs.contains(word))
          replaced.append(wordPairs(word))
        else
          replaced.append(word)
      }
    )

    replaced.mkString(" ")

  }
}

class CensoredStrings(var s: String) extends Censor {
  def getString() = s
  def getReplacedString() = this.replaceWords(this.getString)
}

var cs = new CensoredStrings("Scala is Darn cool you know! Shoot this is nice")
println("Original: " + cs.getString)
println("Replaced: " +cs.getReplacedString)
