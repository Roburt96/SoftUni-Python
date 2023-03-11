function func(array){
    let even_arr = [];
    let odd_arr = [];

    for(let i = 0; i < array.length; i++){
        if (array[i] % 2 === 0){
            even_arr.push(array[i]);
        }else {
            odd_arr.push(array[i]);
        }
    }
    const even_sum = even_arr.reduce((accumulator, value) => {
    return accumulator + value;}, 0);
    const odd_sum = odd_arr.reduce((accumulator, value) => {
    return accumulator + value;}, 0);

    console.log(even_sum - odd_sum);

}
func([1,2,3,4,5,6])
// func([3,5,7,9])
// func([2,4,6,8,10])
