function func(input){
    let first_num = Number(input[0]);
    let last_num = Number(input.slice(-1));  // slice take last element(-1)
    console.log(first_num + last_num);
}

func([20, 30, 40]);
