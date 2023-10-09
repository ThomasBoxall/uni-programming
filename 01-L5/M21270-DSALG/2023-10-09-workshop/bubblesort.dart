List<int> bubbleSort(List<int> data){
  bool sorted = false;
  while (!sorted){
    sorted = true;
    for(int i=0; i<data.length-1; i++){
      if(data[i] > data[i+1]){
        sorted = false;
        //bubble time
        int temp = data[i];
        data[i] = data[i+1];
        data[i+1] = temp;
      }
    }
    print(data);
  }
  return data;
}

void main(){
  print("Output ${bubbleSort([4,7,2,8,2,9,1])}");
}