import scala.io.Source
import java.io._

object Q4 {
  def main(a: Array[String]): Unit={
    val filelines=Source.fromFile("binary-search-tree-in.txt").getLines.toList
    var fl: List[String]=filelines
    val n: Int=filelines.head.toInt
    createbst(n, fl.drop(1), List(1), List(1))
  }
  def createbst(n: Int, fl: List[String], l: List[Int], ol: List[Int]): Unit={
    var nl: List[Int]=l
    var outl: List[Int]=ol
    if(n==(-1)){
      outl=ol.drop(1)
      writeToFile("binary-search-tree-out.txt",outl)
    }
    else{
      var m: Int=fl.head.toInt
      if(n==1){
        nl=l:::List(m)
      }
      else{
        if(l.contains(m)){
          outl=outl:+(1)
          if(n==0) {
            nl=l.filter(_!=m)
          }
        }
        else{
          outl=outl:+(0)
        }
      }
      var newn: Int=fl.drop(1).head.toInt
      createbst(newn, fl.drop(2), nl, outl)
    }
  }
  def writeToFile(p: String, l: List[Int]): Unit={
    val pw = new PrintWriter(new FileWriter(p))
    for(j<-l){
      pw.println(j)
    }
    pw.close()
  }
}
