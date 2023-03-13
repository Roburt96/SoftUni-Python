function func(name, quantity, price) {
    this.name = name;
    this.quantity = quantity;
    this.price = price;
    let result = ''
    result += `I need $${(price * (quantity / 1000)).toFixed(2)} to buy ${(quantity / 1000).toFixed(2)} kilograms ${name}.`
    return result;
}
console.log(func('orange', 2500, 1.80))