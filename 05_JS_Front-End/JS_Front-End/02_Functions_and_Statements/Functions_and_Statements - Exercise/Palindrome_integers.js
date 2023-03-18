function func(arr){

    for (let i = 0; i < arr.length; i++){
        let numStr = arr[i].toString();
        let reversedNumStr = numStr.split('').reverse().join('');
        if (numStr === reversedNumStr){
            console.log('true');
        }else{
            console.log('false');
        }

    }

}

func([123,323,421,121])