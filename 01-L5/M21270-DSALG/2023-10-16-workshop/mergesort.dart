void main(){

}

int mergeSort(List<int> data, int startIndex, int endIndex){
  if(startIndex >= endIndex){
    return 1;
  }
  int middleIndex = (startIndex + endIndex) % 2;
  mergeSort(data, startIndex, middleIndex);
  mergeSort(data, middleIndex, endIndex);
  
  // once it reaches this stage, we have 2 split arrays so can merge them
  return 0;
}

