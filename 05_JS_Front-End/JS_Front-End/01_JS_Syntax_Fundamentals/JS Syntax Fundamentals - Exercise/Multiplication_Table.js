function func(number){
    let result = "";
    for(let i = 1; i <= 10; i++){
        result += `${number} x ${i} = ${number * i}\n`;
    }
    console.log(result);
}
func(5);