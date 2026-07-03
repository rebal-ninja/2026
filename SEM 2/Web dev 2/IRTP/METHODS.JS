// METHODS

// PUSH - ADDS ELEMEENTS TO THE END OF AN ARRAY 

let colours = ["red","blue","green"];
colours.push("black");
console.log(colours)


// POP() - REMOVES THE LAST ELEMENT FORM THE ARRAY

// let colours = ["red","blue","green"]
colours.pop("black")
console.log(colours)

// UNSHIFT()- ADDS THE ELEMENT TO THE BEGINNING OF THE ARRAY

// let colours = ["red","blue","green"];
colours.unshift("yellow");
console.log(colours)

// SHIFT() - REMOVES AN ELEMENT FROM THE BEGINNING OF THE ARRAY 
colours.shift();
console.log(colours)

// INDEXOF()- FIND THE ELEMENT FROM A SPECIFIC ELEMENT OF AN ARRAY
index = colours.indexOf("blue");
console.log(index);


// INCLUDES() - CHECKS IF THE ARRAY CONTAINS A SPECIFIC ELEMENT 
includes = colours.includes("red")
console.log(includes)

// MAP() - CREATE A NEW ARRAY OF AN EXISTING ARRAY AND APPLIES A FUNCTION ON IT 
let nums = [1,2,3,4]
let doubled = nums.map(nums => nums*2)
console.log(doubled)

// CONCAT() - MERGE TO OR MORE ARRAY 
arr1 = [1,2,3,4]
arr2 = [5,6,7]
console.log(arr1.concat(arr2))

// JOIN() - COMBINES ALL ELEMENTS OF AN ARRAY INTO ONE SINGLE STRING 
console.log(colours.join("-"))

// SORT() - SORTS THE ELEMENTS OF ARRAY IN ASCENDING ORDER 
sort = [1,3,6,8,7,5,3]
console.log(sort.sort((a, b) => a - b)
)


// SLICE() EXTRACTS A SECTION OF ARR AND RETURNS A NEW ARRAY 
console.log(sort.slice(1,5))


// SPLICE() - ADD OR REMOVE ELEMENTS FROM AN ARRAY 
console.log(sort.splice(2,3))


// MIN()- FINDS THE MIN VALUE IN THE ARRAY 
console.log(Math.min(...sort))

// MAX()- FINDS THE MAX VALUE IN THE ARRAY 
console.log(Math.max(...sort))

// REVERSE() - REVERSE THE GIVEN ARRAY 
number=[1,22,3,4,5,]
console.log(number.reverse())