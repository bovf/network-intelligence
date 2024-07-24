# Network Intelligence

Network Intelligence is a Python application that gathers network connection information and checks it against a threat intelligence platform.

## Installation

Clone the repository:

```sh
git clone https://github.com/bovf/network-intelligence.git
cd network-intelligence
```

Install the package:

```sh
pip install .
```
## Adding to PATH

### On Linux and MacOS

1. Create a symlink:
   ```sh
   sudo ln -s /path/to/venv/bin/network-intelligence /usr/local/bin/network-intelligence
   ```

2. Verify the symlink:
   ```sh
   network-intelligence --help
   ```

### On Windows

1. Add the directory containing `network-intelligence` to the system PATH:
   - Open the Start Search, type in "env", and select "Edit the system environment variables".
   - In the System Properties window, click on the "Environment Variables" button.
   - In the Environment Variables window, scroll down to the "System variables" section, select the "Path" variable, and click "Edit".
   - Click "New" and add the path to the directory containing `network-intelligence`. For example, `C:\path\to\venv\Scripts`.
   - Click "OK" to close all the windows.

2. Verify the PATH update by opening a new Command Prompt and running:
   ```sh
   network-intelligence --help
   ```
## Configuration

### Obtain an API Key

1. Go to [AbuseIPDB](https://www.abuseipdb.com/).
2. Sign up for a free account if you don't already have one.
3. Once logged in, navigate to the [API key management page](https://www.abuseipdb.com/account/api).
4. Generate a new API key and copy it.

### Add the API Key to the Configuration

1. Encode your API key in base64:

    ```sh
    echo -n 'YOUR_ACTUAL_API_KEY' | base64
    ```

2. Copy the base64 encoded API key.
3. Open the `config.yaml` file in the project directory and add your encoded API key:

    ```yaml
    # config.yaml
    api_key: "BASE64_ENCODED_API_KEY"
    ```

## Usage

To run the application, specify the source of IP addresses:

For active connections:
```sh
sudo network-intelligence --source active
```

For connections from a log file:
```sh
network-intelligence --source log --logfile path/to/network_logs.txt
```

To display the help message:
```sh
network-intelligence --help
```

### Additional Options

- To save the results to a file, use the `--output` option:

    ```sh
    network-intelligence --source active --output results.json
    ```

- To display detailed reports, use the `--detailed` option:

    ```sh
    network-intelligence --source active --detailed
    ```

- Both options can be combined:

    ```sh
    network-intelligence --source active --output results.json --detailed
    ```

## Extending

To add a new threat intelligence platform, create a new connector in the `connectors` directory by extending the `BaseConnector` class and implementing the `check_ip` method.

## Screenshots

![Screenshot 1](documentation/screenshots/Screenshot1.png)
![Screenshot 2](documentation/screenshots/Screenshot2.png)
![Screenshot 3](documentation/screenshots/Screenshot3.png)
