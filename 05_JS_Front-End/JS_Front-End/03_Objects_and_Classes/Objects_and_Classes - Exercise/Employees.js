function func(arr) {
    let result = [];

    for (let key of arr){
        const person = {
            name: key,
            number: key.length
        }
        result.push(person);
    }
    for (let key of result){
        console.log(`Name: ${key.name} -- Personal Number: ${key.number}`);
    }



}

func([
'Silas Butler',
'Adnaan Buckley',
'Juan Peterson',
'Brendan Villarreal'
]);