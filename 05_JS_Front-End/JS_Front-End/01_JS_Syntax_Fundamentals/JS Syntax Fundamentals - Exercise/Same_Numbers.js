function func(number) {
    number = number.toString()
    let first_num = number[0]
    let equal_numbers = ""
    let sum_numbers = 0

    for (let i = 0; i < number.length; i++) {
        if (first_num === number[i]){
            equal_numbers += "1"
        }
        sum_numbers += parseInt(number[i])
    }
    if (equal_numbers.length === number.length){
        console.log(`true\n${sum_numbers}`)
    } else {
        console.log(`false\n${sum_numbers}`)
    }
}

func(2222222);