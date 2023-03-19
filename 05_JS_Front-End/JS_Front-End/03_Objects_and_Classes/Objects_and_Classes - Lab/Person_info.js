function personInfo(firstname, lastname, age){
    const person = {
        firstname: firstname,
        lastname: lastname,
        age: age
    }
    console.log(`firstName: ${person.firstname}\nlastName: ${person.lastname}\nage: ${person.age}`);
}

personInfo("Peter", "Pan", 20);