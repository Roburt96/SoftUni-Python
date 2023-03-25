function convert(obj) {
    const obj_items = JSON.parse(obj)
    for(let key in obj_items) {
        console.log(`${key}: ${obj_items[key]}`);
    }
}

convert('{"name": "George", "age": 40, "town": "Sofia"}')