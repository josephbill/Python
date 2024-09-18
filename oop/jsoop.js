class Car {
    constructor(make,model){
    //   4. this refers to the newly created instance
      this.make = make
      this.model = model
      this.isEngineOn = false
    }

    // method / 
    startEngine(){
        if(!this.isEngineOn){
            this.isEngineOn = true
            console.log(`${this.make} engine is switched on`)
        } else {
            console.log(`${this.make} engine is already on`) 
        }
    }

}

const myCar = new Car("Jeep","Renegade")
myCar.startEngine()

// this as a keyword refers to the context in which a function is executed
console.log(this)
// 1. when outside a function this points to the global execution context in a strict mode. 
// global object {}
function showThis(){
    console.log(this)
}
showThis()
// 2. when inside a function this points to the global execution context in a non-strict mode. 
const obj = {
    name: "Joseph", 
    greet: function(){
        console.log(this.name)
    }
}
obj.greet()
// 3. When a function is called as method of an obj, this refers to the obj
// the method belongs to

// 5. Arrow function context 
// arrow function do not have a reference to this : if you need a reference use named or anonymous function
const globalcontext = typeof window !== 'undefined' ? 'window': global;
globalcontext.n_ame = "alice"
const obja = {
    // block scope
    n_ame: "Joe", 
    greet: () => {
            console.log(this.n_ame)
        }
       
    }


obja.greet()

