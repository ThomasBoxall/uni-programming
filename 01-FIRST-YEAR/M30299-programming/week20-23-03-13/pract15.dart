// Practical 15

void main(){
  // print(eurosToPounds(30));
  // print(fahrenheitToCelsius(75));
  print(costToFill(147.6).toStringAsFixed(2) + "p");
}

double eurosToPounds(double euros){
  return 0.84 * euros;
}

double fahrenheitToCelsius(double fahrenheit){
  return ((fahrenheit - 32) * 5) / 9;
}

double costToFill(double priceOfLitre){
  double sizeOfCarTank = 9 * 4.54609;
  return sizeOfCarTank * priceOfLitre;
}