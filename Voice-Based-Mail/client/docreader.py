import pyttsx3

def read_document(file_name):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust the speech rate (words per minute) as desired

    try:
        with open(file_name, 'r') as f:
            # Read the content of the document
            content = f.read()

        # Use the pyttsx3 library to convert text to speech
        engine.say(content)
        engine.runAndWait()

    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied. Make sure you have proper file permissions.")

    except UnicodeDecodeError:
        print("Unable to decode the file. Make sure it is a valid text document.")

    except Exception as e:
        print("An error occurred:", str(e))

read_document("vmail/client/a.pdf")  # Assuming the file "a.txt" is in the same directory as the script
