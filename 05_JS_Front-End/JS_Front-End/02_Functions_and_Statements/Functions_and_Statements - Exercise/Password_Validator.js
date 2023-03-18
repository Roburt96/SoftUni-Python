function func(pass){
    let message = [];
    let regex_string_digit = /^[a-zA-Z0-9]+$/;
    let regex_2_digit = /\d.*\d/;
    if (pass.length < 6 || pass.length > 10){
        message.push("Password must be between 6 and 10 characters");
        }if(!regex_string_digit.test(pass)){
            message.push("Password must consist only of letters and digits");
            }if(!regex_2_digit.test(pass)){
                message.push("Password must have at least 2 digits");
    }else{
        message.push("Password is valid");
    }


    console.log(message.join("\n"));


}
// ('logIn');
//func('MyPass123');
func('Pa$s$s');