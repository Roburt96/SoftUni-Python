function func(...nums){
    let negative_nums = 0;

    for (const num of nums){
        if (num < 0){
            negative_nums++;
        }
    }
    if (negative_nums === 0 || negative_nums === 2){
        console.log('Positive')
    }else {
        console.log('Negative')
    }
}

func(-6, -12, 14)
func(5, 12, -15)
func(-1, -2, -3)