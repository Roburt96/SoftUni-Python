function phoneBook(list){
    let phoneBook = {};

    list.forEach((str) => {
        let [name, phone] = str.split(' ');
        phoneBook[name] = phone

    });
    for(const [name, number] of Object.entries(phoneBook)){
        console.log(`${name} -> ${number}`);
    }

}

phoneBook(['Tim 0834212554',
 'Peter 0877547887',
 'Bill 0896543112',
 'Tim 0876566344'])