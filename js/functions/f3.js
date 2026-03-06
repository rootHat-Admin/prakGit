function isAdult(age) {
    if (age >= 18) {
        console.log("Adult");
    } else {
        console.log(`Minor , Because ${age} age Den`);
    }
}

let Den_Age = isAdult(16);
console.log(Den_Age)