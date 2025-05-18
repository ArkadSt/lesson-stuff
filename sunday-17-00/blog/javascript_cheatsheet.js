// JAVASCRIPT CHEAT SHEET

const { response } = require("express");

// сообщения в консоль
console.log("Hello world!"); // информация
console.warn(' test %s', "sdfkjl.txt") // внимание
console.error(new Error("oops: some error %d" )) // ошибка

// ---------------------------------------------------------------
// объявление переменных

let num11 = 1; // block scoped

// if (1==1){
//     let a = 5
// }
// console.log(a) // так нельзя

const num12 = 2; // переменная которой можно присвоить значение только один раз
// num12 = 3; // так нельзя

var num33 = 3 // function scoped


// if (1==1){
//     var b = 5
// }
// console.log(b) // так можно

// типы данных
let string1 = "string";
let num1 = 1;
let boolean1 = true;
let array1 = [1,"string",2,3, true];
let null1 = null;
let undefined1 = undefined;
let object1 = {
    "name": "Aleks",
    "surname": "Tkatsenko",
    "telephone": null
};


// арифметические операции
let ten = 5 + 5
// ten == 10
let one = 10 / 10
// one == 1
let fourtysix = 50 - 4 
// fourtysix == 46
let sixty = 30 * 2
// sixty == 60
let sixteen = 2**4
// sixteen = 2 * 2 * 2 * 2 = 16 
let ziro = 4 % 2 
// 4 / 2 = 0   =>  4 == 2 + 2  === 0



// Boolean операторы (то что даёт True/False)
1 > 0 // True
// 3 > 4 // False

 
 2 < 3 // True
 3 < 2 // False 
 5 != "6" // True
//  5 != 5 False

5 !== "5" // False
5 !== "6" // True


 6 >= 7 // True
 6 >= 5 // False


 5 <= 6 // True
//  5 <= 5 True

 4 == 4 // True
 //  4 == "4" // True
 
 4 === 4 // True
//  4 === "4" False


 
 


// функции
// возвращающие 
// не возвращающие
let sum = sum()

function sum(num1, num2){
    return num1 + num2  // возвращает значение
}

function print(a){
    console.log(a) // возвращает undefined
}

const sum = function(){
    return "Hellow world";  // возвращает значение
}



const sum = (num1, num2) => {
    return num1 + num2  // возвращает значение
}

const sum = (num1,num2) => num1+num2 // возвращает значение

const answer = a => console.log(`Our: ${a}`)


fetch().then(response => response.json())

// условные операторы
// if/else
if (2 > 1) { // это правда (true)
    console.log("2 больше чем 1"); // выполниться это
} else {
    console.log("2 не больше чем 1");
}

if (4 < 3) { // это неправда (false)
    console.log("4 меньше чем 3");
} else {
    console.log("4 не меньше чем 3");
}

// while/for


// switch


// работа с массивами
// получение элемента по индексу
// замена элемента по индексу
// добавление элемента
// удаление элемента

// двумерные массивы (матрицы)


// работа с объектами
// получение значение по ключу
// замена значения по ключу
// удаление ключа (и значения)
// 

// тернарные выражения

5 < 5 ? console.log("1") : console.log("2")
// Anser: 2



// работа с HTML

// получение элемента по Id

// получение элементов по классу

// создание нового элемента

// добавление элемента к другому в качестве child

// как удалить элемент

// как дать элементу класс

// изменение аттрибутов элемента



// классы (JavaScript классы, не CSS)

class Car {
    constructor(name, year){
        this.name = name;
        this.year = year;
    }
}
const car1 = new Car("Audi", 2001)
const car2 = new Car("BMW", 2001)


// Асинхронность
// async/await

// fetch API




