import scala.io.Source
import java.io.File
import java.io.PrintWriter

object Q1{
  def findMax(l: List[Int]): Int={
    val sl:List[Int]=l.sorted
    val r:List[Int]=sl.reverse
    val max:Int=r.head
    max
  }
  def rff():Unit={
    val filelines=Source.fromFile("int-list-in.txt").getLines.toList
    val n: Int=filelines(0).toInt
    var lststring=filelines.drop(1)
    var lst = List(0)
    for(i<-1 to n){
      val ele: Int=lststring.head.toInt
      lststring=lststring.drop(1)
      lst=lst:::List(ele)
    }
    val maxInt: String=findMax(lst.drop(1)).toString
    val fout: String="maximum-out.txt"
    writeToFile(fout, maxInt)
  }
  def writeToFile(p: String, s: String): Unit={
    val pw = new PrintWriter(new File(p))
    try pw.write(s) finally pw.close()
  }
  def main(a: Array[String]): Unit={
    rff()
  }
}