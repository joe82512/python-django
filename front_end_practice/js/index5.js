// this 的指向

console.log(this) //全域: 輸出 Window

// 一般函數
function addsquare(a, b){
    console.log(this) //window
    return (a+b)**2
}
let result = addsquare(1, 2)
let r_call = addsquare.call(undefined,1, 2) //call寫法
console.log(result, result.a, typeof result)

// 構造函數: 含有屬性的function
function addsquare2(a, b){
    console.log(this) //addsquare2
    this.a = a
    this.b = b
    this.c = (a+b)**2
}
let result2 = new addsquare2(1, 2) //用 new 實體化構造
console.log(result2, result2.a, result2.c, typeof result2)

// 箭頭函數
let result3 = () => console.log(this)
result3()



// 類別內的 this
console.log('========================================')
class Test{
    test() {console.log(this)} //Test
}
let t = new Test()
// 一般調用函數: func(p1, p2)
t.test()
t.test(t)
t.test('A')
// call 調用函數: func.call(context, p1, p2) -> context 即 this
t.test.call()
t.test.call(t)
t.test.call('A')



// 物件內的 this
console.log('========================================')
let obj1 = {
    func1: function() {console.log(this)},
    other: 'A'
}

obj1.func1() //調用 obj1: this 等於 obj1
obj1.func1.call(obj1) //用call還原

let bar1 = obj1.func1 //直接調用 obj1 內的 func1: this 指向外部
bar1()
bar1.call(undefined) //用call還原



console.log('========================================')
value = 0
let obj2 = {
    value: 1,
    func2: function() {console.log(this.value)}
}

obj2.func2() //調用 obj2 : this 指向 obj2 內的 value
obj2.func2.call(obj2) //用call還原
let bar2 = obj2.func2 //直接調用 obj2 內的 func2 : this 指向外部的 value
bar2()
bar2.call(undefined) //用call還原



// this 的修改方式: call, apply, bind
console.log('========================================')
let result4 = function(a, b) {console.log(this, a, b)}
result4(1, 2)
result4.call('call', 1, 2)
result4.apply('apply', [1, 2])
let new_result4 = result4.bind('bind')
new_result4(1,2)
new_result4.call('call', 1, 2) //this 指向鎖死為'bind'