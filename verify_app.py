import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
import subprocess
import os

# Function to run C++ Script
def runAlgorithm(args, function) -> str:
    '''Runs the C++ program for the given function'''
    print(args)
    if function == 'algo':
        command = ['./algo.exe', str(args).strip()]
    elif function == 'huffman':
        command = ['./huffman.exe', str(args).strip()]
    # Add more conditions for additional algorithms if needed

    result = subprocess.run(command, stdout=subprocess.PIPE, check=True)
    output = result.stdout.decode().strip()

    print(output)

    return output

# Function to create Output Window
def createOutputWindow(OutputVal) -> None:
    '''Displays the output on a different Window'''
    outputWindow = tk.Toplevel()
    outputWindow.title('Compression Output-')
    outputWindow.geometry("500x500")
    outputText = scrolledtext.ScrolledText(outputWindow, wrap=tk.WORD, width=60, height=25)
    outputText.pack(fill=tk.BOTH, expand=True)
    outputText.insert(tk.END, OutputVal)

def runGUI() -> None:
    # create the main window
    root = tk.Tk()

    # set the window title
    root.title("Zipit (File Zipper)!")
    
    # set the window dimensions
    root.geometry("600x400")

    # set the background color of the main window
    root.configure(bg="blue")

    # Load background image
    img_path = r"C:/Users/Hp/Desktop/Zipit!/resize_image.png"
    img = Image.open(img_path)
    img = img.resize((400, 300))
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.place(x=0, y=0, relwidth=1, relheight=1)

    # Frames
    inputFrame = tk.Frame(root)
    inputFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

    buttonFrame = tk.Frame(root, padx=20, pady=20, bg="lightblue")  # Set background color for the button frame
    buttonFrame.pack(fill=tk.BOTH, expand=True)

    # Widget

    # Widget for inputFrame
    inputLabel = tk.Label(inputFrame, text="Enter Text")  # Set background color for the input label
    inputLabel.pack(side=tk.TOP)
    inputEntry = tk.Text(inputFrame, width=60, height=12, xscrollcommand=True)
    inputEntry.pack(side=tk.TOP, padx=5, pady=5)

    # Button Commands
    def runAlgorithmButton(algorithm) -> None:
        inputText = inputEntry.get("1.0", "end-1c")
        output = runAlgorithm(inputText, algorithm)
        createOutputWindow(output)

    def quitButtonCommand() -> None:
        root.destroy()

    # Buttons for buttonFrame
    runAlgoButton = ttk.Button(buttonFrame, text='Lempel Ziv', command=lambda: runAlgorithmButton('algo'))
    runAlgoButton.pack(side=tk.LEFT, padx=10)

    runHuffmanButton = ttk.Button(buttonFrame, text='Huffman', command=lambda: runAlgorithmButton('huffman'))
    runHuffmanButton.pack(side=tk.LEFT, padx=10)

    quitButton = ttk.Button(buttonFrame, text='Quit', command=quitButtonCommand)
    quitButton.pack(side=tk.RIGHT, padx=10)

    # run the main event loop
    root.mainloop()

if __name__ == "__main__":
    # Compile C++ programs using subprocess.run
    compile_algo = subprocess.run(['g++', 'algo.cpp', '-o', 'algo.exe'])
    compile_huffman = subprocess.run(['g++', 'huffman.cpp', '-o', 'huffman.exe'])

    # Check if compilation was successful before running the GUI
    if compile_algo.returncode == 0 and compile_huffman.returncode == 0:
        runGUI()
    else:
        print("Compilation error. Check your C++ code.")
