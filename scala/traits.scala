import scala.collection.mutable.HashMap
import scala.collection.mutable.ArrayBuffer

object Main {
  def main(args: Array[String]) {
    if (args.length == 0 ) {
      println("Usage: scala traits.scala <pairs.txt>")
      return
    }

    class WordPairReader {
      val wordPairs = new HashMap[String, String]

      val source = io.Source.fromFile(args(0))
      val lines = source.mkString
      source.close()

      lines.split("\n").foreach(l => { 
          val pairs = l.split(',')
          this.wordPairs += pairs(0) -> pairs(1)
          }
      )

      this.wordPairs
    }


    trait Censor extends WordPairReader {
      def replaceWords(words: String): String = {
        var replaced = new ArrayBuffer[String]

        words.split(' ').foreach(w => {
            if (wordPairs.contains(w)) {
              val v = wordPairs(w)
              replaced.append(v)
            } else {
              replaced.append(w)
            }
          }
        )

        /*wordPairs.foreach{case (key, value) => 
            //println(key + "=>" + value)
            replaced=replaced.replaceAllLiterally(key, value)
        }*/
        replaced.mkString("\n")
      }
    }

    class CensoredStrings(var s: String) extends Censor {
    }



    var cs = new CensoredStrings("Scala is Darn cool you know! Shoot this is nice")
    println(cs.replaceWords(cs.s))
    //cs.s = cs.s.replaceAllLiterally("Darn", "Pucky")
    //cs.s = cs.s.replaceAllLiterally("Shoot", "Beans")
    println(cs.s)
  
  }
}
