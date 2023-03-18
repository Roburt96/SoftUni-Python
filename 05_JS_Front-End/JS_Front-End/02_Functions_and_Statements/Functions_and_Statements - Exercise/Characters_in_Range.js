function func(start, end) {
    let asciiStart = Math.min(start.charCodeAt(0), end.charCodeAt(0));
    let asciiEnd = Math.max(start.charCodeAt(0), end.charCodeAt(0));
    let asciiRange = [];

  for (let i = asciiStart + 1; i < asciiEnd; i++) {
    asciiRange.push(String.fromCharCode(i));
  }

  console.log(asciiRange.join(' '));


}

func('a', 'd');
func('#', ':');