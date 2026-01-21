const add = (a, b) => a + b;

console.log(add(5, 3));

console.log("---------------------------------");

function multiply(a, b = 2) {
    return a * b;
}

console.log(multiply(5));
console.log(multiply(5, 3));

console.log("---------------------------------");
function createUser(name, age) {
    return {
        name: name,
        age: age, 
        isAdult: age >= 18
    };
}

console.log(createUser("Bob, 20"));

console.log("---------------------------------");

function sumArray(numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sumArray([1, 2, 3, 4]));