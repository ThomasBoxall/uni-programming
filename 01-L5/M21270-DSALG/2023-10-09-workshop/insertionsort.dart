List<int> insertionSort(List<int> data){
  for(int i=0; i<data.length; i++){
    int itemToMove = data[i];
    int indexHole = i;

    while(indexHole > 0 && data[indexHole-1] > itemToMove){
      data[indexHole] = data[indexHole - 1];
      indexHole--;
    }
    data[indexHole] = itemToMove;
    print(data);
  }
  return data;
}

void main(){
  print(insertionSort([18,6,9,1,4,15,12,5,6,7,11]));
}