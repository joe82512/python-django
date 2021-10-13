// 類別 //

// 建立
class Car{
    constructor(brand){
        this.brand = brand
    }

    c_model(model){
        this.model = model
        console.log(this.brand, this.model)
    }
}
//實體化
let c = new Car('BMW')
c.c_model('320i')



// 繼承
console.log('========================================')
class Suv extends Car{
    constructor(brand, l=5, w=2, h=1.75){
        super(brand)
        this.l=l; this.w=w; this.h=h; //添加
        this.brand = brand+':' //覆寫
    }

    c_space(){
        return this.l*this.w*this.h //添加新函數
    }
}
let s = new Suv('BMW',5,2,1)
s.c_model('X5')
console.log(s.c_space())



// 封裝
console.log('========================================')
let _hp = new WeakMap() //設定私有變數
class Private_car extends Suv{
    constructor(brand, l, w, h, hp=400){
        super(brand, l, w, h)
        _hp.set(this, hp) //添加私有變數
    }

    c_hp(){
        console.log(String(_hp.get(this)), 'hp !') //使用私有變數
    }
}
let p = new Private_car('BMW',5,2,1)
p.c_model('X3')
p.c_hp() //預設值輸出
p._hp = 100; p.c_hp(); //修改屬性 _hp 後輸出仍為400




// 多型 -> 繼承的覆寫