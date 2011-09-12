class Censor {
  var wordPairs = Map[String, String]()

  val source = io.Source.fromFile("pairs.txt")

  source.getLines.foreach(l => { 
      val pairs = l.split(',')
      wordPairs += pairs(0) -> pairs(1)
      }
  )

  def replaceWords(words: String): String = {
    // When iterating over a Map you get a tuple of (key, value)
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
println("Replaced: " + cs.getReplacedString)
