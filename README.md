## CSV to JSON Converter with Geocoding and get ward coordinates

This Python script reads a CSV file containing information about cities, districts, and wards in Vietnam, fetches their geographical coordinates using the HERE API, and outputs a hierarchical JSON structure.

## Features

- **CSV Parsing**: Reads a CSV file with columns for cities, districts, wards, and their codes.
- **Geocoding**: Uses the HERE API to get the latitude and longitude of each ward.
- **JSON Output**: Converts the parsed data into a hierarchical JSON format and saves it to a file.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `pandas`
  - `requests`

You can install the necessary Python packages using the following command:

```bash
pip install pandas requests
```
## Getting Started



### 1. Prepare Your CSV File

Ensure your CSV file (`input.csv`) is formatted as follows:

| Tỉnh Thành Phố   | Mã TP | Quận Huyện   | Mã QH | Phường Xã     | Mã PX  |
|------------------|-------|--------------|-------|---------------|--------|
| Thành phố Hà Nội | 01    | Quận Ba Đình | 001   | Phường Phúc Xá| 00001  |

- **`Tỉnh Thành Phố`**: The name of the city or province.
- **`Mã TP`**: The code of the city or province.
- **`Quận Huyện`**: The name of the district.
- **`Mã QH`**: The code of the district.
- **`Phường Xã`**: The name of the ward.
- **`Mã PX`**: The code of the ward.

Make sure the CSV file is saved as `input.csv` in the same directory as the script. The encoding should be UTF-8, and the column headers should be exactly as listed above.

### 2. Update API Key

Replace "YOUR_API_KEY_HERE" in the script with your actual HERE API key. You can obtain an API key from the HERE Developer Portal.

### 3. Run the Script
Run the script using Python:
```python
python main.py
```

