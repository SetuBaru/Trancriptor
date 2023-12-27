from moviepy.editor import VideoFileClip
from google.cloud import speech_v1p1beta1 as speech
import os
from datetime import datetime
from ErrorHandler import LogError
from Authenticate import ServiceAccKey as SAuth


# Initialising GCP SAK Environment
def Authenticate():
    try:
        SAuth()
        print("GCP Service Account key Added to current Environment Successfully!\n")
    except Exception as ServiceKeyAccessError:
        _tempError = f'Encountered {ServiceKeyAccessError} While attempting to Access Key'
        LogError(_tempError)
        return None


# Video Transcription Function (Takes Video Path & Language code as Input [Default Language English US]).
def Transcribe(video_path, _lang_code="en-US"):
    Authenticate()
    # 1. Sanitizing the input.
    try:
        video_path = str(video_path)
        _lang_code = str(_lang_code)
    except Exception as TranscriptionError:
        _tempError = f'Invalid Input! Encountered {TranscriptionError}, while processing input'
        LogError(_tempError)
        return None

    # 2. Ensuring Video File Exists in Path.
    if not (os.path.isfile(video_path)):
        _tempError = f'Video File Does Not Exist in path {video_path}'
        LogError(_tempError)
        return None

    print('Video File Loaded Successfully!\n')
    # 3. Performing Audio Extraction from Video File
    try:
        clip = VideoFileClip(video_path)
        audio = clip.audio
        print('Audio Extraction Completed Successfully! \n')
    except Exception as AudioExtractionError:
        _tempError = f'Encountered {AudioExtractionError} while attempting to Extract Audio Data!!'
        LogError(_tempError)
        return None

    # 4. Transcribe the audio using Google Speech-to-Text API
    try:
        client = speech.SpeechClient()
        operation = client.long_running_recognize(
            audio={"content": audio.raw_data},
            config={"language_code": _lang_code}  # Change language if needed
        )
        response = operation.result()
        print("File Transcribed Successfully!\n")
    except Exception as TranscriptionError:
        _tempError = f'Encountered {TranscriptionError}'
        LogError(_tempError)
        return None

    # 5. Generating Transcription file
    transcript = ""  # placeholder File
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Get Current Time
    file_name = f"transcript-{current_time}.txt"  # File Name modifier

    # 6. Populating the Transcript Local Variable with the Response from Google's STT API
    for result in response.results:
        transcript += result.alternatives[0].transcript + " "

        # Writing to Transcription File
        try:
            with open(f"transcript-{current_time}.txt", "w") as file:
                file.write(transcript)
            print(f"Source Transcribed Successfully to target:{file_name}\n")
            return file
        except Exception as FileWriteError:
            _tempError = f'Encountered {FileWriteError} while attempting to write to {file_name}!'
            LogError(_tempError)
            return None


# Main function Unit test Here!
if __name__ == '__main__':
    print('Welcome to the main file')
