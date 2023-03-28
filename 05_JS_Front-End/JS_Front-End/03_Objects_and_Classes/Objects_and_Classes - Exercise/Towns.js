function towns(arr){
    let result = [];
    for (let key of arr){
        let [town, latitude, longitude] = key.split(' | ');
        result.push({town, latitude, longitude});
    }
    for (let key of result){
        console.log(key)
    }

}

towns(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']
)