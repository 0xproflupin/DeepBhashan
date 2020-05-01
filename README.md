# DeepBhashan
# DeepBhashan



Preparing the dataset : 
In the folder named dataset text_files, chapter wise are present.  Run the script Preparing_jsons.py to prepare the json files. After creating the json files manually fine tune them to ensure proper matching of the text with the audio files in jsons. Once done with jsons, run the script Preparing_csvs.py to prepare csvs for each chapter. Merge all csvs to create a final one and then using Splitting_data.py seperate it into training, testing and validation data with a split ratio of 70:20:10. For seperating wav files in each csv seperately use Splitting_wav_files.py.
