function func(order, price){
    let result = 0.00;
    const possible_orders = {
        coffee: 1.50,
        water: 1.00,
        coke: 1.40,
        snacks: 2.00
    }
    if(order in possible_orders){
        result = price * possible_orders[order];
    }
    return result.toFixed(2);

}
console.log(func('water', 5));
console.log(func('coffee', 2));