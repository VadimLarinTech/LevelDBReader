// popup.js
// This script handles the user input from the popup to save key-value pairs in chrome.storage.

document.getElementById('save').addEventListener('click', () => {
  const inputKey = document.getElementById('inputKey').value;
  const inputValue = document.getElementById('inputValue').value;

  if (inputKey && inputValue) {
    let data = {};
    data[inputKey] = inputValue;
    chrome.storage.sync.set(data, () => {
      console.log(`Value for key "${inputKey}" is set to "${inputValue}"`);
      alert(`Value saved: ${inputValue} for key: ${inputKey}`);
      document.getElementById('inputKey').value = ''; // Clear the key field
      document.getElementById('inputValue').value = ''; // Clear the value field
    });
  } else {
    alert('Please enter both key and value');
  }
});
