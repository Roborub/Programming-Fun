let enteredInteger = 0;
let totalEven = 0, totalOdd = 0, i;

while (enteredInteger >= 0){
    enteredInteger = 0;
    enteredInteger = Number(prompt("Please enter an integer. Enter -1 to end."));

    if (enteredInteger >= 0){
        i = enteredInteger % 2
        if (i == 0){
            totalEven = totalEven + 1;    
        }
        else if (i != 0){
            totalOdd = totalOdd + 1;    
        }
    }
}