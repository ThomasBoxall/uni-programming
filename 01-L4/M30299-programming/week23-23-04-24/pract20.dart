void main() {
  // initListInfo();
  // initCapMarks();
  // printOrders();
  // print(average([47, 65, 34, 73, 0]));
  // moduleCreditPrint();
  // examScorePrint();
  print(gradeCalculator());
}

void initListInfo(){
  List<String> customers = ['Ştefan', 'Amy', 'Jamilla', 'Xiu', 'Amy'];
  listInfo(customers); // Size=5, first=Ştefan, last=Amy
  
  customers.add('Nadim');
  listInfo(customers); // Size=6, first=Ştefan, last=Nadim
}

void listInfo(List<String> list){
  print("Length: ${list.length}. First: ${list.first}. Last: ${list.last}");
}

void initCapMarks(){
  List<int> myMarks = [47, 65, 34, 73, 0];
  capMarks(myMarks);
  print(myMarks); // Should print: [40, 40, 34, 40, 0]
}

void capMarks(List<int> marks) {
  for (int x=0; x< marks.length; x++){
    marks[x] = (marks[x]>40)? 40: marks[x];
  }
}

void printOrders(){
    Map<String, String> orders = {
    // Key (name): Value (drink)
    'Ştefan': 'Espresso Frappuccino',
    'Amy T': 'Iced Coffee',
    'Jamillah': 'Caramel Frappuccino',
    'Xiu': 'Caffè Latte',
    'Amy E': 'Caramel Frappuccino'
  };

  for(String k in orders.keys){
    print("$k has ordered: ${orders[k]}");
  }  
}

double average(List<int> toAverage){
  int total = 0;
  for(int i=0; i<toAverage.length; i++){
    total += toAverage[i];
  }
  return total/toAverage.length;
}

void moduleCreditPrint(){
  Map<String, int> credits = {
    "Architecture & Operating Systems": 20,
    "Programming": 40,
    "Core Computing Concepts": 20,
    "Database System Development":20,
    "Networks": 20
  };

  for (String k in credits.keys){
    print("$k has ${credits[k]} credits");
  }
}

void examScorePrint(){
  Map<String, List<int>> marksMap = {
    "Architecture & Operating Systems" : [92],
    "Programming" : [100, 80, 94, 83, 100, 97, 100],
    "Core Computing Concept": [72],
    "Database Systems Development" : [75],
    "Networks": [86]
  };
  for(String k in marksMap.keys){
    print("In $k I got: ${listToStr(marksMap[k]!)}");
  }
}

String listToStr(List<int> listToConvert){
  String retVal = "";
  for(int current in listToConvert){
    retVal = retVal + current.toString() + " ";
  }
  return retVal;
}

String gradeCalculator(){
  Map<String, List<int>> marksMap = {
    "Architecture & Operating Systems" : [92],
    "Programming" : [100, 80, 94, 83, 100, 97, 100],
    "Core Computing Concepts": [72],
    "Database Systems Development" : [75],
    "Networks": [86]
  };
  Map<String, int> credits = {
    "Architecture & Operating Systems": 20,
    "Programming": 40,
    "Core Computing Concepts": 20,
    "Database Systems Development":20,
    "Networks": 20
  };
  double score = 0;
  for (String k in marksMap.keys){
    double moduleScore = 0;
    double assessmentWeighting = (100 / marksMap[k]!.length) / 100;
    for (int currentMark in marksMap[k]!){
      moduleScore += currentMark * assessmentWeighting;
    }
    print(moduleScore);
    // score += moduleScore;
    double moduleWeighting = credits[k]! / 100;
    score += (moduleScore * moduleWeighting);
  }
  if(score >= 70){
    return "1st";
  } else if (score >= 60){
    return "2:1";
  } else if (score >= 50){
    return "2:2";
  } else if (score >= 40){
    return "3rd";
  } else{
    return "fail";
  }
}