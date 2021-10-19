import kotlin.math.abs

fun main(args: Array<String>) {
    var cases = readLine()!!.toInt()
    for (c in 0 until cases) {
        dance()
    }

}

fun dance() {
    val count = readLine()!!.toInt()
    var posX = 0
    var posY = 0
    var facing = 0
    for (move in 0 until count) {
        val (instr, x) = readLine()!!.split(" ")
        val num = x.toInt()
        when (instr) {
            //using normal % in kotlin with negatives gives a negative answer 
            "CW" -> facing = Math.floorMod(facing + (num / 90),4)
            "CCW" -> facing =Math.floorMod(facing - (num / 90),4)
            "N" -> posY -= num
            "S" -> posY += num
            "E" -> posX += num
            "W" -> posX -= num
            "F", "B" -> {
                val amount = if (instr == "F") num else -num
                //  0
                // 3 1
                //  2
                when (facing) {
                    0 -> posY -= amount
                    2 -> posY += amount
                    1 -> posX += amount
                    3 -> posX -= amount
                }
            }
            else -> {
               println("something went wrong")
            }
        }
//        println("$facing, $posX, $posY")
    }
    println(abs(posX) + abs(posY))
}