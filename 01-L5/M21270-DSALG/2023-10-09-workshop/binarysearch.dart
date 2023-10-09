int binarySearch(List<int> data, int searchFor){
  int foundIndex = -1;

  int top = data.length;
  int bottom = 0;
  
  while(top > bottom){
    int middle = ((top + bottom) / 2).round();
    if (searchFor == data[middle]){
      foundIndex = middle;
      break;
    } else if(searchFor > data[middle]){
      bottom = middle + 1;
    } else if(searchFor < data[middle]){
      top = middle - 1;
    }else{
      break;
    }
  }

  
  return foundIndex;
}

void main(){
  print("Output: ${binarySearch([1,2,2,4,7,8,9], 2)}");
}