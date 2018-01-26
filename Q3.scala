import scala.io.Source
import java.io._

object Q3{
  def main(a: Array[String]): Unit={
    val filename="int-list-in.txt"
    val filelines: List[String]=Source.fromFile(filename).getLines.toList
    var n: Int=filelines.head.toInt
    var lstString = filelines.drop(1)
    var lst: List[Int]=List(0)
    for(line <- lstString){
      var ele: Int=line.toInt
      lst=lst:+ele
    }
    lst=lst.drop(1)
    val unlst: List[Int]=findunique(lst)
    val f: String="unique-out.txt"
    writeToFile(f,unlst)
  }
  def writeToFile(p: String, l: List[Int]): Unit={
    val pw = new PrintWriter(new FileWriter(p))
    var lststr: List[String]=List("Hey")
    for(i<-l){
        lststr=lststr:::List(i.toString)
    }
    lststr=lststr.drop(1)
    for(j<-lststr){
      pw.println(j)
    }
    pw.close()
  }
  def findunique(l: List[Int]): List[Int]={
    var nl: List[Int]=List()
    for(i<-l){
      if(!(nl.contains(i))){
        nl=nl:+i
      }
    }
    nl
  }
}
