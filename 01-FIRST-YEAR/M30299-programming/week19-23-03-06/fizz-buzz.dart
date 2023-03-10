void main(){
    for(int curVal = 1; curVal <=100; curVal++){
        String printStr = "";
        bool fb = false;

        if(curVal % 3 == 0){
            // multiple of three
            printStr += "Fizz";
            fb = true;
        }
        if(curVal % 5 == 0){
            printStr += "Buzz";
            fb = true;
        }
        if (!fb){
            printStr = curVal.toString();
        }

        print(printStr);
    }
}