from VideoTranscription import Transcribe as Tb


def BasicTCLI(x=None, y=None):
    # x as video path, y as Input Language
    if x is None:
        x = input('Please Input Video Path')
        x = str(x)
    else:
        x = str(x)
    print(f'Video Path Selected is: {x}.\n')

    if y is None:
        y = input('Please Input Language:')
        y = str(y)
    if (y is not None) and (y.lower() == 'english' or 'english us' or 'eng'):
        y = "en-US"
    else:
        y = str(y)
    print(f'Language Selected is: {y}.\n')

    # Booting Transcriptor Service
    print('Booting Trancripter Service....\n')
    Tb(x, y)


if __name__ == "__main__":
    BasicTCLI()
