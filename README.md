# photo-KP-label

GUI application for windows built entirely with python and tkinter for use on a pipeline construction project to rename photos taken with a phone with the 'chainage' they were taken at. Chainage is the distance from the beginning of the project and is the primary method of communicating location in the field. By renaming the photos, they are more easily organized and referenced. Chainage is determined through geospatial analysis of the project shapefile and accessing the metadata of the photo file.

![image](https://user-images.githubusercontent.com/71047303/167641006-5c79592a-ac57-46e8-bbe6-9240ffdc4ed8.png)

Compile the application using the `pyinstaller` package

```bash
pyinstaller --add-data="project_data;project_data" --onefile --noconsole  image_chainages.py
```
