// 條件判斷式 //
x1 = 1; x2 = 1.0; y = '1.00'; z = true;
console.log(x1==x2, y==z) //相等 (不含型態)
console.log(x1===x2, y===z) //嚴格相等 (含型態)
n = null; u = undefined;
console.log('null & undefined', n==u, n===u) //等價, 但不相等
s1 = Symbol('S'); s2 = Symbol('S');
console.log('symbol', s1==s2, s1===s2) //不等價

// if
console.log('========================================')
if (x1==10) {
    console.log('x等於10')
}
else if (x1>10) {
    console.log('x大於10')
}
else {
    console.log('x小於10')
}

// switch
console.log('========================================')
switch (x1) {
    case 1:
        console.log('x等於1')
        //break //不加break的話會暴力進行下個 case
    case 2:
        console.log('x等於2')
        break
    case 3:
        console.log('x等於3')
        break
    default:
        console.log('x等於0')
        break
}

// try & catch
console.log('========================================')
try {
    errorfunction('correct')
}
catch(err) {
    console.log(err.name, '->', err.message)
}



// 迴圈 //
console.log('========================================')
for (i=0; i<5; i=i+1) {
    console.log(i)
}

j = 0
while (j<5) {
    console.log(j)
    j = j+1
    if (j==3) {
        break
    }
}