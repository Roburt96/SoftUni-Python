function func(num, elem_1, elem_2, elem_3, elem_4, elem_5) {
    let number = Number(num);
    const arr = Array.from({ length: 5 }, (_, i) => {
      switch (i) {
        case 0:
          return elem_1;
        case 1:
          return elem_2;
        case 2:
          return elem_3;
        case 3:
          return elem_4;
        case 4:
          return elem_5;
        default:
          return null;
      }
    });
    for (let i = 0; i <= arr.length; i++) {
        let command = arr[i];
        let cur_num = number;
      switch (command){
        case 'chop': console.log(cur_num /= 2); break;
        case 'dice': console.log(Math.sqrt(cur_num)); break;
        case 'spice': console.log(cur_num + 1); break;
        case 'bake': console.log(cur_num *= 3); break;
        case 'fillet': console.log(cur_num -= cur_num * 0.80); break;
      }

    }
}

// func('32', 'chop', 'chop', 'chop', 'chop', 'chop');
func('9', 'dice', 'spice', 'chop', 'bake', 'fillet');