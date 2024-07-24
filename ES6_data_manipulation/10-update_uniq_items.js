export default function updateUniqueItems(map) {
    // Check if the input is a Map
    if (!(map instanceof Map)) {
      throw new Error('Cannot process');
    }
  
    // Iterate over the map entries
    for (const [key, value] of map.entries()) {
      // Check if the quantity is 1 and update it to 100
      if (value === 1) {
        map.set(key, 100);
      }
    }
  }
  