int linearSearch(List<int> data, int searchFor){
  int foundIndex = -1;

  for(int i=0; i<data.length; i++){
    if(data[i] == searchFor){
      foundIndex = i;
      break;
    }
  }

  return foundIndex;
}

void main(){
  print("Output: ${linearSearch([4,7,2,8,2,9,1], 10)}");
}