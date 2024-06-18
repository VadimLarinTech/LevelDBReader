# LevelDB Reader Chrome Extension

This project consists of a Chrome extension for storing key-value pairs using the `chrome.storage` API, and a Python script to fetch and display these values from the local LevelDB database.

**The script can be run directly or using Docker.**

## Project Structure

```plaintext
leveldbreader/
│
├── extension/
│   ├── manifest.json
│   ├── background.js
│   ├── popup.html
│   ├── popup.js
│
├── scripts/
│   ├── read_leveldb.py
│   ├── config.ini
│
├── Dockerfile
├── LICENSE
└── README.md
```

## Extension

### Files

- **`manifest.json`**: Describes the extension's metadata and permissions.
- **`background.js`**: Script for setting default values when the extension is installed.
- **`popup.html`**: HTML file for the extension's popup interface.
- **`popup.js`**: JavaScript file for handling user input and saving key-value pairs.

### How to Use

#### Load the Extension in Chrome:

1. Open Chrome and go to `chrome://extensions/`.
2. Enable "Developer mode" using the toggle in the top-right corner.
3. Click "Load unpacked" and select the `extension` directory.

#### Using the Popup:

1. Click on the extension icon to open the popup.
2. Enter a key and value, then click "Save" to store the pair.

#### Setting Default Values:

1. Uncomment the code in `background.js` if you need to set default values when the extension is installed.
2. The code is currently commented out to prevent overriding existing data.

## 🐍 Build Guide Using the Python Script

### Prerequisites

#### Installing Python, pip and plyvel

```sh
sudo apt install python3-pip
sudo apt-get install build-essential python3-dev libleveldb-dev
pip install plyvel
```

### Files

- **`read_leveldb.py`**: Script for reading data from the LevelDB database.
- **`config.ini`**: Configuration file for specifying the database path.

### Configuration

#### Find the Extension ID:

1. Open Chrome and go to `chrome://extensions/`.
2. Enable "Developer mode" using the toggle in the top-right corner.
3. Locate your extension and find the ID (a long string of letters and numbers).

#### Set the Database Path in `config.ini`:

```ini
db_path = /home/your-username/.config/google-chrome/Default/Sync Extension Settings/<your-extension-id>
```

### Running the Script

1. Ensure config.ini contains the correct database path.

2. Run the script to fetch a specific value:

```sh
python3 scripts/read_leveldb.py get "your_key"
```
3. Run the script to scan and display all key-value pairs:
```sh
python3 scripts/read_leveldb.py scan
```

### Command-Line Usage

#### Fetch a specific value:

```sh
python3 scripts/read_leveldb.py get <db_path> "your_key"
```

#### Scan and display all key-value pairs:

```sh
python3 scripts/read_leveldb.py scan <db_path>
```

## 🐳 Build Guide Using Docker

### Prerequisites

1. Ensure Docker is installed on your system. If not, follow the instructions at https://docs.docker.com/get-docker/.

### Using the Docker Image

#### Fetch a specific value by specifying the database path in the command:
```sh
sudo docker run --rm -v "/path/to/your/local/leveldb:/data" vadimlarintech/leveldbreader python3 scripts/read_leveldb.py get /data "your_key"
```
##### Example
```sh
sudo docker run --rm -v "/home/ash/.config/google-chrome/Default/Sync Extension Settings/fpdpjejapahidhmchgkkljaapifdlndj:/data" vadimlarintech/leveldbreader python3 scripts/read_leveldb.py get /data "1"
```
#### Scan and display all key-value pairs by specifying the database path in the command:
```sh
sudo docker run --rm -v "/path/to/your/local/leveldb:/data" your-dockerhub-username/leveldbreader python3 scripts/read_leveldb.py scan /data
```
##### Example
```sh
sudo docker run --rm -v "/home/ash/.config/google-chrome/Default/Sync Extension Settings/fpdpjejapahidhmchgkkljaapifdlndj:/data" vadimlarintech/leveldbreader python3 scripts/read_leveldb.py scan /data
```
# License

This project is licensed under the MIT License. See the LICENSE file for details.
