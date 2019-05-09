const obj1 = { foo: 'bar', x:30 }
const obj2 = { foo: 'baz', y:10 }

const ssafy = { ...obj1 }
// { foo: 'bar', x: 30 }
const ssafy2 = { ...obj1, ...obj2 }
// { foo: 'baz', x: 30, y: 10 }
console.log(ssafy2)