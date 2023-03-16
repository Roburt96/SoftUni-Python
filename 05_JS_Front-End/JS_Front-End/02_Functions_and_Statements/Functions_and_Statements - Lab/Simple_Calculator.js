function func(num_one, num_two, operation){
    let result;
    switch(operation){
        case 'add':
            result = num_one + num_two;
            break;
        case 'subtract':
            result = num_one - num_two;
            break;
        case 'multiply':
            result = num_one * num_two;
            break;
        case 'divide':
            result = num_one / num_two;
            break;
    }
    return result;
}
console.log(func(5, 5, 'multiply'));