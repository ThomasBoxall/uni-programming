void main(){
  print(gcd(34346, 8));
}

int gcd(int n1, int n2){
  if (n1 == n2){ return n1; }
  else if (n1 < n2){ return gcd(n2-n1, n1); }
  else{ return gcd(n1 - n2, n2); }
}