function func(nums, array){
    let new_array = [];
    for(let i = 0; i < nums; i++){
        new_array.push(array[i]);
    }

    console.log(`${new_array.slice(0, nums).reverse().join(' ')}`);




}



func(3, [10, 20, 30, 40, 50]);
func(4, [-1, 20, 99, 5]);
func(2, [66, 43, 75, 89, 47]);