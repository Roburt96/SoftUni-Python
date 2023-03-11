function func(num_one, num_two, operation) {

    let result;
    switch (operation) {
        case '+': result = num_one + num_two; break;
        case '-': result = num_one - num_two; break;
        case '*': result = num_one * num_two; break;
        case '/': result = num_one / num_two; break;
        case '%': result = num_one % num_two; break;
        case '**': result = num_one ** num_two; break;
    }
    console.log(result);

}

func(5, 6, '+')