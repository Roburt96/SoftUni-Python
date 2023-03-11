function func(num_one, num_two, num_three) {
    let result;

    if (num_one > num_two && num_one > num_three) {
        result = num_one;
    } else if (num_two > num_one && num_two > num_three) {
        result = num_two;
    }else {
        result = num_three;
    }
    console.log(`The largest number is ${result}`);
}

func(5, -3, 16);
func(-3, -5, -22.5)