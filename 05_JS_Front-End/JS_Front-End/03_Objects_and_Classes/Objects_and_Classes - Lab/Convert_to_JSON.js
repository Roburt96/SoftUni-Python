function convert(f_name, l_name, h_color){
    let obj = {
        firstName: f_name,
        lastName: l_name,
        hairColor: h_color
    }
    console.log(JSON.stringify(obj))

}

convert('George', 'Jones', "Brown")