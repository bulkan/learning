import scala.io._
import scala.actors._
import scala.actors.Actor._

object PageLoader {
  def getPageSize(url: String) = Source.fromURL(url).mkString.length
  def getPageSizeWithCount(url: String): List[Int] = {
    var html = Source.fromURL(url).mkString
    val size = html.length
    val reg = """(?i)<a[^>]""".r
    return List(size, reg.findAllIn(html).size)
  }

}

val urls = List(
  "http://www.amazon.com",
  "http://www.twitter.com",
  "http://www.google.com",
  "http://www.cnn.com"
)

def timeMethod(method: () => Unit) = {
  val start = System.nanoTime
  method()
  val end = System.nanoTime
  println("Method took " + (end-start)/1000000000.0 + " seconds")
}

def getPageSizeConcurrently() = {
  val caller = self

  for (url <- urls) {
    actor { caller ! (url, PageLoader.getPageSizeWithCount(url)) }
  }

  for(i <- 1 to urls.size) {
    receive {
      case (url, t) => 
      var l = t.asInstanceOf[List[Int]]
      val size  = l(0)
      val anchors = l(1)
      println("Size for " + url + ": " + size)
      println("Has " + ": " + anchors + " anchor tags")
    }
  }
}

println("Concurrent run")
timeMethod { getPageSizeConcurrently }

/*
  Bonus: make the sizer follow all the links on a give page and load them as well.
*/
