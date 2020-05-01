# DeepBhashan
## DeepBhashan - Personalised Speech Recognition Using Deep Neural Networks

## About : 
Speech recognition problem can be solved using traditional ways like HMMs. With increased computational power and bigger datasets we can get better accuracy on DNN than HMM. 
Broad Structure:
* Speech 
* Feature Extraction using pre trained base model 
* Fine Tuning Encoder Network(LSTM/RNNs)  
* Fine tuning English LM for Hindi Speech  
* Repeating Tasks for Multiple Users.

## Pre-processing data : 

We have taken hindi audiobook from librivox, which had 33 chapters of about 20-25 mins along with their mp3's and text files. Each hindi-typed text file has been converted to english data using google translate API using the script ***csv_mapping_EnglishToHindi.py*** Each sentence has been seperated indivisually and special characters and uni-codes have been removes from the text.
Aeneas library has been used to preprocess the text files and generate a json syncmap for corresponding text and audio files.



## Preparing the dataset : 

In the folder named dataset -> text_files, chapter wise are present. Run the script ***Preparing_jsons.py*** to prepare the json files. After creating the json files manually fine tune them to ensure proper matching of the text with the audio files in jsons. Once done with jsons, run the script ***Preparing_csvs.py*** to prepare csvs for each chapter. Merge all csvs to create a final one and then using ***Splitting_data.py*** seperate it into training, testing and validation data with a split ratio of 70:20:10. For seperating wav files in each csv seperately use ***Splitting_wav_files.py***.
