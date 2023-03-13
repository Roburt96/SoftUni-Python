function func(start, end) {
    let sum = 0;
    let arr_nums = [];
    for (let i = start; i <= end; i++) {
        arr_nums.push(i);
        sum += i;
    }
    console.log(arr_nums.join(' '));
    console.log(`Sum: ${sum}`);
}

func(5, 10);