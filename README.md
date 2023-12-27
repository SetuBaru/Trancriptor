# Transcriptor Project

## Introduction

This project provides a Python-based solution to transcribe audio from video files using Google's Speech-to-Text API. It extracts audio from video files and generates transcripts in text format.

## Installation

### Prerequisites

- Python 3.x
- Google Cloud Service Account Key

### Setup Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/SetuBaru/Transcriptor.git
    cd Transcriptor
    ```

2. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Google Cloud Service Account Key:

    Place your `service_account_key.json` file inside the `/private` directory.

## Usage

1. **Basic Usage:**

    Run the `main.py` script and follow the prompts to transcribe a video file.

    ```bash
    python main.py
    ```

2. **Advanced Usage:**

    The `VideoTranscription.py` module provides a function `Transcribe` that can be imported and used in custom scripts or applications to transcribe video files programmatically.

    ```python
    from VideoTranscription import Transcribe

    # Usage example
    Transcribe("path/to/your/video.mp4", "en-US")
    ```

## Folder Structure
    /private
       service_account_key.json
    /cache
       ERROR_LOGS.txt
    main.py
    VideoTranscription.py
    ErrorHandler.py
    Authenticate.py
    README.md
    requirements.txt

## Dependencies

- `moviepy`
- `google-cloud-speech`

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
