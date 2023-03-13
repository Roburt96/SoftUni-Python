function func(number){
    if(number % 4 === 0 && number % 100 !== 0 || number % 400 === 0){
        console.log("yes");
    }
    else{
        console.log("no");
    }
}
func(2003);