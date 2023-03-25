function meetings(arr) {
  let meetings = {};

  arr.forEach((str) => {
    let [weekday, name] = str.split(' ');

    if (meetings[weekday]) {
      console.log(`Conflict on ${weekday}!`);
    } else {
      meetings[weekday] = name;
      console.log(`Scheduled for ${weekday}`);
    }
  });

  for (const [weekday, name] of Object.entries(meetings)) {
    console.log(`${weekday} -> ${name}`);
  }
}
meetings(['Monday Peter',
 'Wednesday Bill',
 'Monday Tim',
 'Friday Tim'])