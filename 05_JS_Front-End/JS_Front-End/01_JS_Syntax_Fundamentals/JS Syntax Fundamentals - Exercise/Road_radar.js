function func(speed, area){
    let speed_diff = 0;
    let result = '';
    const areaLimit = {
        motorway: 130,
        interstate: 90,
        city: 50,
        residential: 20
    }
    switch (area) {
        case 'motorway':
            if(speed <= areaLimit[area]){

                result = (`Driving ${speed} km/h in a ${areaLimit[area]} zone`);break;
            }else if (speed > areaLimit[area]){
                speed_diff = speed - areaLimit[area];
                if (speed_diff <= 20){
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - speeding`);break;
                }else if(speed_diff <= 40){
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - excessive speeding`);break;
                }else{
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - reckless driving`);break;
                }
            }break;
        case 'city':
            if(speed <= areaLimit[area]){

                result = (`Driving ${speed} km/h in a ${areaLimit[area]} zone`);break;
            }else if (speed > areaLimit[area]){
                speed_diff = speed - areaLimit[area];
                if (speed_diff <= 20){
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - speeding`);break;
                }else if(speed_diff <= 40){
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - excessive speeding`);break;
                }else{
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - reckless driving`);break;
                }
            }break;
        case 'interstate':

            if(speed <= areaLimit[area]){
                result = (`Driving ${speed} km/h in a ${areaLimit[area]} zone`);break;
            }else if (speed > areaLimit[area]){
                speed_diff = speed - areaLimit[area];
                if (speed_diff <= 20){
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - speeding`);break;
                }else if(speed_diff <= 40){
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - excessive speeding`);break;
                }else{
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - reckless driving`);break;
                }
            }break;
        case 'residential':

            if(speed <= areaLimit[area]){
                result = (`Driving ${speed} km/h in a ${areaLimit[area]} zone`);break;
            }else if (speed > areaLimit[area]){
                speed_diff = speed - areaLimit[area];
                if (speed_diff <= 20){
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - speeding`);break;
                }else if(speed_diff <= 40){
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - excessive speeding`);break;
                }else{
                    result = (`The speed is ${speed_diff} km/h faster than the allowed speed of ${areaLimit[area]} - reckless driving`);break;
                }
            }break;
        }
        return result;




}

console.log(func(40, 'city'));
console.log(func(21, 'residential'));
console.log(func(120, 'interstate'));
console.log(func(200, 'motorway'));