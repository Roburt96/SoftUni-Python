function func(people, type_grp, week_day){
    const prices = {
        Students: {
            Friday: 8.45,
            Saturday: 9.80,
            Sunday: 10.46
        },
        Business: {
            Friday: 10.90,
            Saturday: 15.60,
            Sunday: 16
        },
        Regular: {
            Friday: 15,
            Saturday: 20,
            Sunday: 22.50
        }
    }
    let price = prices[type_grp][week_day];
    let totalPrice = price * people;
    switch (type_grp) {
        case 'Students':
            if (people >= 30){
                totalPrice *= 0.85; break;
            }break;
        case 'Business':
            if (people >= 100){
                totalPrice -= 10 * prices[type_grp][week_day]; break;
            }break;

        case 'Regular':
            if (people >= 10 && people <= 20){
                totalPrice *= 0.95; break;
            }break;
        default:
            break;
    }
    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

func(40,
"Regular",
"Saturday");