import scala.io.Source
import java.io._

class Vertex(p: Int, c: String, d: Int, n: List[Int]) {
  var parent: Int = p
  var colour: String = c
  var distance: Int = d
  var neighbours: List[Int] = n
  def addToNeighbours(newv: Int): Unit={
    neighbours=neighbours:::List(newv)
  }
}

object Q5{
  var graph: List[Vertex] = Nil
  def main(a: Array[String]): Unit ={
    readNodes()
  }
  def readNodes(): Unit ={
    val filelines=Source.fromFile("breadth-first-search-in.txt").getLines.toList
    var filestring=filelines
    val n: Int=filestring.head.toInt
    filestring=filestring.drop(1)
    for(i <- 0 to n-1){
      graph = graph:+new Vertex(-1, "", -1000, List(i))
    }
    var u: Int = filestring.head.toInt
    while(u!=(-1)){
      filestring=filestring.drop(1)
      var v: Int = filestring.head.toInt
      var uVertex: Vertex = graph(u)
      uVertex.addToNeighbours(v)
      var vVertex: Vertex = graph(v)
      vVertex.addToNeighbours(u)
      filestring=filestring.drop(1)
      u = filestring.head.toInt
    }
    filestring=filestring.drop(1)
    u = filestring.head.toInt
    filestring=filestring.drop(1)
    var v: Int = filestring.head.toInt
    initialise(u)
    var Q: List[Int] = List(u)
    bfs(Q)
    val fout: String="breadth-first-search-out.txt"
    var pathtov=getPath(u, v)
    if(pathtov.length==0){
         writeToFile(fout, List(-1))
    }
    else{
         var path=pathtov:::List(v)
         writeToFile(fout, path)
    }
  }
  def writeToFile(p: String, path: List[Int]): Unit={
    val pw = new PrintWriter(new FileWriter(p))
    for(j<-path){
      pw.println(j)
    }
    pw.close()
  }
  def getPath(u: Int, v: Int): List[Int]={
    if(v>0){
        if(u!=v){
            var p: Int = graph(v).parent
            getPath(u, p):::List(p)
        }
        else{
            List()
        }
    }
    else{
	List()
    }	
  }
  def bfs(Q: List[Int]): Unit ={
    if(Q.length > 0){
      var s: Vertex = graph(Q.head)
      var newQ = Q.drop(1)
      for(v <- s.neighbours.drop(1)){
        var vVertex: Vertex = graph(v)
        if(vVertex.colour == "WHITE"){
          vVertex.colour="GRAY"
          vVertex.distance=s.distance+1
          vVertex.parent=s.neighbours.head
          newQ=newQ:+v
        }
      }
      s.colour="BLACK"
      bfs(newQ)
    }
  }
  def initialise(u: Int): Unit ={
    if(u>=0) {
      for (v <- graph) {
        v.colour = "WHITE"
        v.parent = -1
        v.distance = -1
      }
      var source: Vertex = graph(u)
      source.colour = "GRAY"
      source.distance = 0
      source.parent = u
    }
  }
}
