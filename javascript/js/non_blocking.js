// const nothing = () => {}

// console.log('start sleeping')
// setTimeout(nothing, 3000) // non-block callback stack
// console.log('end of program')

// python code 처럼 동작하게 하려면
const logEnd = () => {
    console.log('end of program')
}
console.log('start sleeping')
setTimeout(logEnd, 3000)

function first() {
    console.log('first')
}

function second() {
    console.log('second')
}

function third() {
    console.log('third')
}
first()
setTimeout(second, 1000)
third()

// 이벤트 루프
// 시간의 흐름에 따라 코드의 수행을 처리, 그 때마다 JS엔진을 작동시킴

// func1() 를 호출했을 때 func1, func3, func2 순으로 출력
function func1() {
    console.log('func1')
    func2()    
}

function func2() {     
    setTimeout(() => console.log('func2'), 1000) 
    func3()
}

function func3() {
    console.log('func3') 
}

func1()