// 函數 //

//一般寫法
function addsquare(a, b){
    return (a+b)**2
}
result = addsquare(1, 2)
console.log(result, typeof result)

//直接指派變數為function
console.log('========================================')
result1 = function addsquare1(a, b){
    return (a+b)**2
}
console.log(result1(1,2), typeof result1)

//匿名函數
console.log('========================================')
result2 = function (a, b){
    return (a+b)**2
}
console.log(result2(1, 2), typeof result2)

//箭頭函數:
console.log('========================================')
/* 使用限制
1. 無引數仍須保留 ()
2. 若腳本超過一行仍須用{ return}
3. 架構與一般函數不同, 箭頭函數內沒有this
3. 注意有牽扯到 this 的函數, call, apply, bind 無法覆蓋
4. 沒有 new, prototype, yield -> 不能建立構造函數
*/
result3 = (a, b) => (a+b)**2
console.log(result3(1, 2), typeof result3)



// 宣告: var let const
console.log('========================================')
var x = 1; let y = 2; const z = 3;
var x = 11 //重複宣告
//let y = 22 //Uncaught SyntaxError: Identifier 'y' has already been declared
//const z = 33 //Uncaught SyntaxError: Identifier 'z' has already been declared
x = 111; y = 222;
//z = 333 //Uncaught TypeError: Assignment to constant variable.

// 作用域 function
console.log('========================================')
test1 = () => {
    t1=1; var t2=1; let t3=1; const t4=1;
}
console.log(test1())
console.log(t1) //t1==1
//console.log(t2) //Uncaught ReferenceError: t2 is not defined
//console.log(t3) //Uncaught ReferenceError: t3 is not defined
//console.log(t4) //Uncaught ReferenceError: t4 is not defined

// 作用域 區塊
console.log('========================================')
//var tt2=123; let tt3=123; const tt4=123; //先定義並不影響if內的變數
i = 3
if (i==3) {
    tt1=1; var tt2=1; let tt3=1; const tt4=1;
}
console.log(tt1) //tt1=1
console.log(tt2) //tt2=2 -> var 已定義
//console.log(tt3) //Uncaught ReferenceError: tt3 is not defined
//console.log(tt4) //Uncaught ReferenceError: tt4 is not defined