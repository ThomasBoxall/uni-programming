List<int> selectionSort(List<int> data){
  int sortedEnd = -1;
  int unsortedStart = 0;
  int unsortedEnd = data.length;

  while(sortedEnd != unsortedEnd - 1){
    int toMoveIndex = unsortedStart;
    for (int i = unsortedStart; i<unsortedEnd; i++){
      if(data[i] < data[toMoveIndex]){
        //current is candidate for movement
        toMoveIndex = i;
      }
    }
    // print(toMoveIndex);
    
    unsortedStart++;
    sortedEnd++;

    int temp = data[sortedEnd];
    data[sortedEnd] = data[toMoveIndex];
    data[toMoveIndex] = temp;

    // print(data);
  }


  return data;
}

void main(){
  print(selectionSort([2,4,5,1,6,8,1,44,87,3,6,23,68,3,23,1345,67876,54,2345,678,122,3,221,1,12,46,57,34,57,68,3]));
}