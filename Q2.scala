import scala.io.Source
import java.io.File
import java.io.PrintWriter

object Q2{
  def main(a: Array[String]): Unit={
    inpout()
  }
  def inpout():Unit={
    val filelines=Source.fromFile("factorial-in.txt").getLines.toList
    var n: Int=filelines.head.toInt
    val f: Int=fact(n)
    val fs: String=f.toString
    val p: String="factorial-out.txt"
    writeToFile(p,fs)
  }
  def writeToFile(p: String, s: String): Unit={
    val pw = new PrintWriter(new File(p))
    try pw.write(s) finally pw.close()
  }
  def fact(num: Int): Int={
    if(num>1){
      num*fact(num-1)
    }
    else{
      1
    }
  }
}