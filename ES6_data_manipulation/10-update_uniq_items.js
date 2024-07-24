export default function updateUniqueItems(map) {
  for (const [key, value] of map.entries()) {
    // Check if the quantity is 1 and update it to 100
    if (value === 1) {
      map.set(key, 100);
    }
  }
}
