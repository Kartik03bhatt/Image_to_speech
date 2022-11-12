import tkinter as tk
import os
import sys
from tkinter import filedialog #used for creating window
from tkinter.filedialog import askopenfile
 #gives permission to open a file
from PIL import Image, ImageTk
import boto3 #for using aws textract services
from tempfile import gettempdir
from contextlib import closing
from tkinter import filedialog
from tkinter.filedialog import askopenfile

# this will convert the string we get from textract to audio using polly
def convert(result):
    aws_console= boto3.session.Session(profile_name='kartik_aws')  # programetically login aws IAM user
    client=aws_console.client(service_name='polly',region_name='ap-south-1')  #create a client that intract with aws service
    response=client.synthesize_speech(Engine='standard',OutputFormat='mp3',Text=result,VoiceId='Matthew')
    print(response)
    if "AudioStream" in response:
        with closing(response['AudioStream']) as stream:
            output=os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(stream.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("Could not find the stream")
        sys.exit(-1)
    if sys.platform=='win32':
        os.startfile(output)

wind=tk.Tk() #creating window
wind.geometry("550x430")
wind.title("Image to Audio using AWS services")
wind['background']='#2D383C'
my_font1=('times',18,'bold',)
l1=tk.Label(wind,text="Upload an Image to Read ", width=30,font=my_font1,background='#2D383C',cursor='man',fg='#0783B6',pady=10) #creating label
l1.pack()
b1=tk.Button(wind,text="Upload",width=30,command=lambda:uploadfile(),borderwidth=10)#creating button
b1.pack()

def uploadfile():
    aws_mag_con=boto3.session.Session(profile_name='kartik_aws')
    client=aws_mag_con.client(service_name='textract',region_name='ap-south-1')
    global img
    f_types=[('Jpg Files',"*.jpg")]
    filename=filedialog.askopenfilename(filetype=f_types)
    img=Image.open(filename)#opening image
    img_resize=img.resize((450,225))
    img=ImageTk.PhotoImage(img_resize)
    imgbytes=get_image_byte(filename)
   
    b2=tk.Button(wind,image=img,pady=10,borderwidth=5)
    b2.pack()
    
    response=client.detect_document_text(Document={'Bytes':imgbytes})
    string = str()
    for item in response['Blocks']:
          if item['BlockType']=='LINE':
              print(item['Text'])
              result =str(item['Text'])
              string = string + " " + result
    convert(string)



def get_image_byte(filename):
    with open(filename,'rb') as imgfile:
              return imgfile.read()



wind.mainloop()