from aeneas.executetask import ExecuteTask
from aeneas.task import Task

# create Task object
config_string = u"task_language=en|is_text_type=plain|os_task_file_format=json"
task = Task(config_string=config_string)
for i in range(2,34):

	task.audio_file_path_absolute = "chap" + str(i) + ".mp3"
	task.text_file_path_absolute = "c" + str(i) + ".txt"
	task.sync_map_file_path_absolute = "chap" + str(i)  + "_syncmap.json"

	# process Task
	ExecuteTask(task).execute()

	# output sync map to file
	task.output_sync_map_file()