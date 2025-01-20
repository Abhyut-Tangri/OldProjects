
let i=0;

/*while (i<=5)
{

    console.log( 'The number is ' +i);
    i++

}*/   


do{

    console.log('the number is ' +i);
    i++;}
while(i<5)

console.log(i);

var number1 =22;
var number2 =24;

if(number1==number2)

{

console.log('Correct! Both numbers are equal')

}else {

     console.log('Incorect! These to numbers are not equivalent')   

}

let MyArray=[]
MyArray=[2 ,2,3,4,5,6,7,8,9,]


if (MyArray[0]==MyArray[1] && MyArray[2]==MyArray[3])
{

    console.log('Correct! One of the conditions are met');


}else if (MyArray[2]<0)
{ar
    console.log('Incorrect!');

} else {

    console.log('None of the conditions are correct ');
}

/*while (i<=5)
{

console.log('The number is ' +i);
i++;
}*/

do {

console.log('The number is ' +i)

}while(i<1)



console.log(i);

for (i=0;  i<5;i++)
{

console.log('For Loop: The number is '+i);

}

switch (new Date().getDay()) {
    case 0:
      day = "Sunday";
      break;
    case 1:
      day = "Monday";
      break;
    case 2:
       day = "Tuesday";
      break;
    case 3:
      day = "Wednesday";
      break;
    case 4:
      day = "Thursday";
      break;
    case 5:
      day = "Friday";
      break;
    case 6:
      day = "Saturday";
  }

  console.log(day)

var x= 1;

switch (x){
  case 0:
    text = "off";
    break;
    case 1:
    text = "On";
    break;
  default:
  text = "No value found";
}

console.log(text);