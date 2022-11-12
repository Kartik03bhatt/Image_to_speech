# Text_to_speech_from_image
This Python application can read text from image using AWS services like AMAZON POLLY and AMAZON TEXTRACT.\n
This python script use boto3 to communicate with AWS to use services. In AWS, Amazon Textract extract text from image and store it in a string and 
Amazin Polly will convert this string to audio.

# Requirement
Any OS system with Python compiler and Amazon CLI installed.

# How to run code:
 * First of all configure your AWS account using CLI (its better if it is named profile than default). 
 * To configure follow these docs: 
      * https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html
      * https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
 * Now go to code and in line no. 16 and change the profile name from 'kartik_aws' to your profile name you just set up.
 * Just save the code and you are ready to go.
