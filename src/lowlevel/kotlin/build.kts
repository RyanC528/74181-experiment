fun main(){
    Runtime.getRuntime("kotlinc chip.kt control.kt -include-runtime -d main.jar")

    Runtime.getRuntime("java -jar main.jar")
}
