// Allows fast calculation on the sum of elements in a given
// range (contiguous segments of array)

// Example - [6, 3, -2, 4, -1, 0, -5]
// Prefix Sum Array - [6, 9, 7, 11, 10, 10, 5]

// you take the previous element and add it to the current
// element

let array = [6, 3, -2, 4, -1, 0, -5];

for (let i = 1; i < array.length; i++) {
    array[i] = arra[i] + array[i - 1];
}
