export default function appendToEachArrayValue(array, appendString) {
  for (const [index, value] of array.entries()) {
    array[array.indexOf(value)] = appendString + value;
  }

  return array;
}
