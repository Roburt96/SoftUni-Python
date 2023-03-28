function store(arr_one, arr_two){
    let result = {}
     function addProducts (list){
        for (i = 0; i < list.length; i+=2){
            let [name, quantity] = [list[i], list[i+1]]
            if (name in result){
                result[name] += parseInt(quantity)
            } else {
                result[name] = parseInt(quantity)
            }
        }
     }
     addProducts(arr_one)
     addProducts(arr_two)
    for (let [key, value] of Object.entries(result)) {

        const product = {
            name: key,
            quantity: value,
            printInfo: function (){
                console.log(`${this.name} -> ${this.quantity}`)
            }
        }
        product.printInfo()
    }
}

store([
'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
],
[
'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
])