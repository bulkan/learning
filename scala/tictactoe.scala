class TicTacToe(val board: Array[String]) {
}



object Main {
  def main(args: Array[String]) {
    val b = new TicTacToe(Array("x", "o", "o"))
    println(b.board)

  }
}
