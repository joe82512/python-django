/*
多行註解: JavaScript ES6
<1> JS有分號(;), 但部分可以省略, 新的編譯器會自動加上
<2> JS為原型物件導向, 新版本將 function 包裝成 class
*/
console.log('hello world !') //單行註解: 輸出
x = '分號'; console.log(x);



// 變數賦值 //
x1 = 1 //變數賦值
x2 = 1.0
y = '1.00'
z = true 
console.log(typeof(x1), typeof x2, typeof y, typeof z) //資料型態
console.log('必須要括弧:',typeof(x3=123), typeof(x1==x2))

n = null; u = undefined; s = Symbol();
console.log(typeof n, typeof u, typeof s)

a = 6+1 //加
b = 3-1 //減
c = a*b
d = a/b //除
d1 = parseInt(a/b) //商
d2 = a%b //餘數
e = a**b //次方
console.log(c, d, d1, d2, e) //數字運算

f = y + 'abcdefg'
console.log(f, f[4], f.slice(1,-2)) //字串擷取

console.log(Number(z),String(x1),Boolean(y)) //型態轉換



// 陣列與物件 //
console.log('========================================')
A = [x1, x2, y, z] //陣列 Array
console.log(A)
console.log(A[1]) //取值
console.log(A.slice(1,3))
console.log(A.concat([0, '0'])) // A不受影響
A.push(false)
console.log(A) // A被更新
console.log(typeof A)

O = {
    o1: x1,
    o2: x2,
    o3: y,
    o4: z
} //物件 Object
console.log(O)
console.log(O.o4) //取值
OO = {o1: 0, o5: false}
Object.assign(O, OO) // O被更新
console.log(O)
console.log(typeof O)